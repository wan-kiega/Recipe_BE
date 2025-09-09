### **API Terminal Walkthrough with `curl`**

This guide provides a step-by-step walkthrough of the Recipe API using the command-line tool `curl`. You will perform all key actions, including user authentication and recipe management, directly from your terminal.

**Base URL:**
Before you begin, set the `BASE_URL` environment variable to the address of your deployed API.

```bash
export BASE_URL="https://yourappname.up.railway.app/"
```

-----

#### **1. User Registration**

Register a new user account.

```bash
curl -X POST "$BASE_URL/api/auth/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "StrongPass123!"
  }'
```

  * **Expected Success:** `201 Created` with a JSON object containing the user's `username` and `email`.
  * **Expected Error:** `400 Bad Request` if the username already exists or the data is invalid.

-----

#### **2. Login and Obtain JWT Token**

Log in with your new user credentials to get an `access` token for authenticated requests.

```bash
curl -X POST "$BASE_URL/api/auth/jwt/create/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "StrongPass123!"
  }'
```

  * **Expected Success:** `200 OK` with a JSON object containing `access` and `refresh` tokens.

**Save the Access Token:**
Store the returned `access` token in an environment variable to use in subsequent requests.

```bash
export ACCESS_TOKEN="<paste_your_access_token_here>"
```

-----

#### **3. Create a Recipe (Authenticated)**

Use the saved token to create a new recipe.

```bash
curl -X POST "$BASE_URL/api/recipes/" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Chocolate Cake",
    "description": "Rich and moist chocolate cake",
    "ingredients": ["flour", "sugar", "eggs", "cocoa powder"],
    "instructions": "Mix ingredients and bake at 180C for 40 minutes.",
    "category": "Dessert",
    "preparation_time": 20,
    "cooking_time": 40,
    "servings": 6
  }'
```

  * **Expected Success:** `201 Created` with the full JSON data of the newly created recipe, including its `id`.
  * **Expected Error:** `401 Unauthorized` if no `Authorization` header is provided.

-----

#### **4. List All Recipes**

Retrieve a list of all recipes. This endpoint does not require authentication.

```bash
curl "$BASE_URL/api/recipes/"
```

  * **Expected Success:** `200 OK` with a JSON array of all public recipes.

-----

#### **5. Retrieve a Specific Recipe**

Fetch the details of a single recipe using its ID.

```bash
curl "$BASE_URL/api/recipes/1/"
```

  * **Expected Success:** `200 OK` with the JSON data for the recipe with `id=1`.
  * **Expected Error:** `404 Not Found` if the recipe ID does not exist.

-----

#### **6. Update a Recipe (Owner Only)**

Modify a recipe. This requires authentication and ownership of the recipe.

```bash
curl -X PUT "$BASE_URL/api/recipes/1/" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Chocolate Cake",
    "description": "Even richer and more delicious",
    "ingredients": ["flour", "sugar", "eggs", "cocoa powder", "butter"],
    "instructions": "Mix, bake, and enjoy.",
    "category": "Dessert",
    "preparation_time": 25,
    "cooking_time": 35,
    "servings": 8
  }'
```

  * **Expected Success:** `200 OK` with the updated JSON data.
  * **Expected Error:** `403 Forbidden` if you are not the owner of the recipe.

-----

#### **7. Delete a Recipe (Owner Only)**

Delete a recipe using its ID. This also requires authentication and ownership.

```bash
curl -X DELETE "$BASE_URL/api/recipes/1/" \
  -H "Authorization: Bearer $ACCESS_TOKEN"
```

  * **Expected Success:** `204 No Content`.
  * **Verification:** A subsequent `GET /api/recipes/1/` request will return a `404 Not Found` error.

-----

### **Common Error Testing**

Here are examples to demonstrate the API's validation and error handling.

#### **Invalid Email Registration**

```bash
curl -X POST "$BASE_URL/api/auth/users/" \
  -H "Content-Type: application/json" \
  -d '{"username":"baduser","email":"not-an-email","password":"StrongPass123!"}'
```

  * **Expected Response:** `400 Bad Request` with an error message like `"Enter a valid email address."`.

#### **Weak Password Registration**

```bash
curl -X POST "$BASE_URL/api/auth/users/" \
  -H "Content-Type: application/json" \
  -d '{"username":"weakpass","email":"weak@example.com","password":"123456"}'
```

  * **Expected Response:** `400 Bad Request` with an error message like `"This password is too common."`.
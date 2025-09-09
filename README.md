# Django Recipe API

This is a robust backend API for managing and sharing recipes. It provides a secure platform for users to create, view, and manage their own recipes, while offering powerful search and filtering capabilities for all users. The API is built with Django and Django REST Framework, ensuring a scalable and production-ready solution.

-----

### **Key Features**

  * **User Authentication:** Secure user registration and login using **JSON Web Tokens (JWT)**.
  * **Recipe Management:** Authenticated users can perform full CRUD (Create, Read, Update, Delete) operations on their own recipes.
  * **Recipe Attributes:** Each recipe includes a **title**, **description**, **ingredients**, **instructions**, **category**, and other relevant details.
  * **Search & Filtering:** Users can search recipes by **title**, **category**, or **ingredients**, and filter them by **preparation time**, **cooking time**, or **number of servings**.
  * **Ownership Enforcement:** Recipes are linked to their creators, ensuring only the owner can modify or delete a recipe.
  * **Admin Dashboard:** Admins can manage all users and recipes through the built-in Django admin interface.

-----

### **Technologies Used**

  * **Python 3.11+**
  * **Django 5+**
  * **Django REST Framework**
  * **Djoser** (for authentication endpoints)
  * **djangorestframework-simplejwt** (for JWT support)
  * **django-filter** (for advanced filtering)
  * **PostgreSQL** (production database)
  * **SQLite** (development database)

-----

### **Getting Started**

Follow these steps to set up the project locally for development.

#### **1. Clone the Repository**

```
git clone <repository-url>
cd recipe_be
```

#### **2. Set Up a Virtual Environment**

It's highly recommended to use a virtual environment to manage dependencies.

```
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

#### **3. Install Dependencies**

Install all the required Python packages.

```
pip install -r requirements.txt
```

> **Note:** If you don't have a `requirements.txt` file, you can install the dependencies listed in the documentation:
> `pip install django djangorestframework djoser djangorestframework-simplejwt django-filter psycopg2-binary dj-database-url`

#### **4. Run Migrations**

Apply the database migrations to set up the necessary tables.

```
python manage.py makemigrations
python manage.py migrate
```

#### **5. Create an Admin User**

Create a superuser to access the Django admin dashboard at `http://127.0.0.1:8000/admin/`.

```
python manage.py createsuperuser
```

#### **6. Run the Development Server**

```
python manage.py runserver
```

The API will now be running at `http://127.0.0.1:8000/`.

-----

### **API Endpoints**

All API endpoints are prefixed with `/api/`.

#### **Authentication Endpoints (`/api/auth/`)**

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/users/` | Register a new user. |
| `POST` | `/jwt/create/` | Log in and receive a JWT token. |
| `POST` | `/jwt/refresh/` | Refresh an expired access token. |

#### **Recipe Endpoints (`/api/recipes/`)**

| Method | Endpoint | Description | Authentication |
| :--- | :--- | :--- | :--- |
| `GET` | `/recipes/` | Retrieve a list of all recipes. | Optional |
| `POST` | `/recipes/` | Create a new recipe. | **Required** |
| `GET` | `/recipes/{id}/` | Retrieve a single recipe by its ID. | Optional |
| `PUT` | `/recipes/{id}/` | Update an existing recipe. | **Required** (Owner) |
| `DELETE` | `/recipes/{id}/` | Delete a recipe. | **Required** (Owner) |

-----

### **Authentication**

All recipe management endpoints require a JWT access token. After logging in, include the token in your request headers like this:

```
Authorization: Bearer <your_access_token>
```

-----

### **Testing the API**

You can test the API endpoints using tools like **Postman** or **Insomnia**. The project includes a Postman collection (`recipe_api.json`) that you can import to test all the core functionalities, including user registration, login, and recipe CRUD operations.

-----

### **Deployment**

This project is configured for seamless deployment on platforms like **Render** or **Railway**.

1.  **Configure Environment Variables:**
      * **`SECRET_KEY`**: Your Django secret key.
      * **`DEBUG`**: Set to `False` for production.
      * **`DATABASE_URL`**: The connection string for your PostgreSQL database.
2.  **Run Migrations on Production Server:** After deployment, run `python manage.py migrate` to apply migrations to the production database.

-----

### **Testing APIs in this project**

This project is deployed on Railway and the API actio

### **Author**

This project was created as a walkthrough for building a backend API with Django.

For any questions or issues, please feel free to reach out or fork and make a PR.


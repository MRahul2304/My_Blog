# Django Blog Project

A simple blog application built with Django, featuring categories, posts, and an about section.

## Features

- **Post Management**: Create, read, update, and delete blog posts.
- **Category Management**: Organize posts by categories.
- **About Us Page**: A dedicated page for information about the blog.

## Requirements

- Python 3.x
- Django 5.x
- MySQL

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database:**

   Make sure you have MySQL installed and create a database named `blog`.

5. **Set up your Django settings:**

   Update the `DATABASES` section in `myweb/settings.py` with your MySQL credentials.

6. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the server:**

   ```bash
   python manage.py runserver
   ```

9. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage posts and categories.
- Explore the blog features on the main page.

## Contributing

Contributions are welcome! Please create a pull request or open an issue for discussion.

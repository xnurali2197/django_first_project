# Django Blog Project

A Django-based web application featuring a blog system with user authentication and profile management.

## Project Structure

```
├── blog/               # Blog application
├── main/              # Main project configuration
├── templates/         # HTML templates
├── manage.py          # Django management script
└── requirements.txt   # Project dependencies
```

## Features

- User Authentication (Login/Register)
- User Profile Management
- Blog System
- Responsive Templates
- Contact and About Pages

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the admin interface at: `http://localhost:8000/admin`
- View the blog at: `http://localhost:8000`
- Register new users at: `http://localhost:8000/register`
- Login at: `http://localhost:8000/login`

## Templates

- `base.html` - Base template with common layout
- `index.html` - Homepage
- `login.html` - User login
- `register.html` - User registration
- `profile.html` - User profile
- `about.html` - About page
- `contact.html` - Contact page

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

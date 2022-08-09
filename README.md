# ✨ To run this application 

## 👉 Create the virtual environment using command 

### ✨ For Windows

```
    python -m venv env
```
#### 👉 To activate the environment 

```
    env\Scripts\activate
```

### ✨ For Linux

```
    python -m venv env
```
#### 👉 To activate the environment

```
    . env\bin\activate
```


### 👉 Once environment is ready install the required pacakges using the command 

```
    pip install -r requirements.txt
```
### 👉 For creating django application use the command 

```
    django-admin startproject Project 
```
> This will create one folder having and inside that folder it create our project that having the manage.py file.

```
    django-admin startproject Project .
```
> This will create folder and manage.py file it not create one extra folder.

### 👉 After installation to run the make migration and migrate command

#### 👉 For makemigration
```
    python manage.py makemigrations
```
> Django will make migrations for any change to your models or field 

#### 👉 For migrate
```
    python manage.py migrate
```
> Whenever you code up a new model, you also generate a migration to create the necessary table in the database for that we have to run migration command.


#### 👉 For run the localhost

```
    python manage.py runserver
```
> This command will run the django Project in port 8000 and the webpages will server at <a>http://127.0.0.1:8000/</a>

> For stop the server use ctrl+c

#### 👉 For creating any new app in the existing project we use the command

```
    python manage.py startapp app_name
```


## ✨ Code-base structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- Project/                               # Implements app configuration
   |    |-- asgi.py                        # ASGI stands for Asynchronous Server Gateway interface
   |    |-- settings.py                    # Defines Global Settings
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |    |-- wsgi.py                        # Start the app in production and wsgi stand for Web Server Gateway Interface
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

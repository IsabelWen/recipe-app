# Recipe App
## Project description
A recipe app with a MySQL database at the server side, and the client side renders HTML- and CSS-based pages via the Django framework. This application lets the users sign up and create their own content. The user can create and edit recipes, including their ingredients, cooking time, and difficulty level.

## Project dependencies
* Django (4.2.11)
* pillow (10.2.0)
* pandas (2.0.3)
* matplotlib (3.7.5)
* django-environ (0.11.2)

## Link to app
Hosted on Netlify: 

## Key Features
* Allow for user authentication, login, and logout.
* Let users search for recipes according to ingredients.
* Automatically rate each recipe by difficulty level.
* Receive user input and handle errors appropriately.
* Display more details on each recipe if the user asks for that.
* Add user recipes to an database.
* Include a Django Admin dashboard for working with database entries.
* Show statistics and visualizations based on trends and data analysis

## Technical Requirements
* Works on Python 3.6+ installations and Django version 3.
* Handles exceptions or errors that arise during user input, for example, then displays user-friendly error messages.
* Connects to a PostgreSQL database hosted locally on the same system (an SQLite database is needed during the development of your application).
* Provides an easy-to-use interface, supported by simple forms of input and concise, easy-to-follow instructions. Menus containing features like login and logout must be presented neatly—with concise and easy-to-follow prompts.
* Code with proper documentation and automated tests is uploaded on GitHub. A “requirements.txt” file is provided, containing the requisite modules for the project.

## Set up this App
1. Clone this repository.
2. Navigate to the recipe-app folder and run ```pip install -r requirements/dev.txt```
3. Setup Database by configuring ```DATABASES``` in the ```settings``` folder in ```dev.py``` for development and in ```prod.py``` for production. 
4. Run migrations with ```python manage.py migrate```
5. Create a superuser by running ```python manage.py createsuperuser```
6. Run ```python manage.py runserver``` to check out the app in your browser under ```http://127.0.0.1:8000```


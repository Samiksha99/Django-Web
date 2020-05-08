# deployapp
Getting Started

Prerequisites

virtualenv,
postgresql

Initialize the project
Create and activate a virtualenv:

virtualenv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
NOTE: After installing dependencies, pip-tools is also installed. You can now use it to manage package dependencies of your project.

'''
Add a new package to requirements.in and run the following command to auto-update requirements.txt file
'''
pip-compile requirements.in

'''
Run the following command to sync your virtualenv
'''
pip-sync

For more details, https://github.com/nvie/pip-tools

Migrate, create a superuser, and run the server:

1.python manage.py migrate

2.python manage.py makemigrations {{cookiecutter.project_name}}

python manage.py createsuperuser

3.python manage.py runserver

Setting up Heroku

Deployment to heroku requires a Procfile which is present in the main directory. This can always be changed on need basis.

Following steps need to be undertaken to deploy to heroku

1.Create an account on heroku if not already.

2.Create a heroku app - you could either use the heroku dashboard to do this or the heroku cli.

3.Install Heroku cli - documentation

create a heroku app using cli

1.Use heroku login and enter your credentials.

2.Run heroku create {app-name} to create your app on heroku. This would give you the app deployment url and the apps git url. documentation.

Deployment to heroku:

1.Add the heroku git url using git remote add heroku {heroku-git-url} (required only for the first time).

2.To deploy a build, run git push heroku HEAD:master . This should push all changes to heroku which can be viewed at the app url. 

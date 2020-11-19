import os
import sys
import time

urls = 'urls.py'
forms = 'forms.py'
templates = 'templates'

def app():
    app_name = input('choose an app name: ')
    if os.path.isdir('./' + app_name):
        print(app_name + ' exists')
    else:
        comando_app = 'python manage.py startapp ' + app_name
        os.system(comando_app)
        os.chdir(app_name)
        fileURLS = open(urls, 'w+')
        fileURLS.write('./' + app_name)
        fileFORMS = open(forms, 'w+')
        fileFORMS.write('./' + app_name)
        os.mkdir(templates)
        os.chdir(templates)
        inner_templates = app_name
        os.mkdir(inner_templates)
        quit()

def project():
    print('choose a name for your project: ')
    proj_name = input()
    if os.path.isdir('./' + proj_name):
        print('ERROR: folder "' + proj_name + '" exists')
        project()
    else:
        comando = 'django-admin startproject ' + proj_name
        try:
            os.system(comando)
            print('creating file...')
            time.sleep(2)
            os.chdir(proj_name)
        except ValueError:
            print('an error occurred...')

        
        no = 'n'
        yes = 'y'
        question = input('create a superuser? [y][n] choose no: ') 
        if question == no:
            print('superuser NOT CREATED')
            try:
                app()
            except ValueError:
                print('an error occurred...')
        elif question == yes:
            admin_creation = 'python manage.py createsuperuser'
            os.system(admin_creation)
            print('superuser CREATED')
            try:
                app()
            except ValueError:
                print('an error occurred...')
        else:
            print('ERROR occurred')

project()
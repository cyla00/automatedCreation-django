import os
import sys
import time
from app_creation import app
from superuser_creation import superuser_creation

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
            try:
                app()
                path_root = os.path.dirname(os.getcwd())
                os.chdir(f'{path_root}')
                print(os.getcwd())
                superuser_creation()
                print('quitting...')
                time.sleep(2)
                quit()
            except Exception as err:
                print(f'ERROR occurred: {err}')
        except Exception as err:
            print(f'ERROR occurred: {err}')

        else:
            print('ERROR occurred')
<<<<<<< HEAD
#!C:\Users\APP\ECサイト２\venv\Scripts\python.exe
=======
#!C:\Users\APP\ECサイト\venv\Scripts\python.exe
>>>>>>> 82bd51fffd2fdb865204538b313e3f53fced89ea
# When the django-admin.py deprecation ends, remove this script.
import warnings

from django.core import management

try:
    from django.utils.deprecation import RemovedInDjango40Warning
except ImportError:
    raise ImportError(
        'django-admin.py was deprecated in Django 3.1 and removed in Django '
        '4.0. Please manually remove this script from your virtual environment '
        'and use django-admin instead.'
    )

if __name__ == "__main__":
    warnings.warn(
        'django-admin.py is deprecated in favor of django-admin.',
        RemovedInDjango40Warning,
    )
    management.execute_from_command_line()

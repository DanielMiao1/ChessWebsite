import os
import sys

try: import django
except ModuleNotFoundError: os.system("pip3 install django")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChessWebsite.settings')
from django.core.management import execute_from_command_line
execute_from_command_line(["", "runserver"])

#!./.venv/bin/python3

import subprocess, time, os, platform, sys
from dotenv import load_dotenv

load_dotenv()

debug = os.getenv("DEBUG", True) == 'True'
args = sys.argv

if len(args) == 2:
	port = int(args[1])
	use_gunicorn = False

elif len(args) == 3:
	port = int(args[1])
	use_gunicorn = tuple(args[2])
else:
	port = 8090
	use_gunicorn = False

try:
	if platform.system() == 'Windows':
		print("Starting application...\n")
		subprocess.run(['git', 'pull'])
		print("\nRunning migrations and starting server...\n")
		subprocess.run(['./.venv/Scripts/python.exe', 'manage.py', 'makemigrations'])

		subprocess.run(['./.venv/Scripts/python.exe', 'manage.py', 'migrate'])
		print(f"Starting server on http://127.0.0.1:{port}\n")
		subprocess.run(['./.venv/Scripts/python.exe', 'manage.py', 'runserver', f'0.0.0.0:{port}'])
	else:
		print("Starting application...\n")
		subprocess.run(['git', 'pull'])
		subprocess.run(['./.venv/bin/python3', 'manage.py', 'collectstatic', '--no-input'])
		print("\nRunning migrations and starting server...\n")
		subprocess.run(['./.venv/bin/python3', 'manage.py', 'makemigrations'])

		subprocess.run(['./.venv/bin/python3', 'manage.py', 'migrate'])
		print(f"Starting server on http://127.0.0.1:{port}\n")
		if not use_gunicorn:
			subprocess.run(['./.venv/bin/python3', 'manage.py', 'runserver', f'0.0.0.0:{port}'])
		else:
			subprocess.run(['./.venv/bin/gunicorn', 'hex_web.wsgi', '--workers 3', '--reload'])

except KeyboardInterrupt:
	print('\n\nStopping server and exiting program')
	print('Server stopped, database saved')

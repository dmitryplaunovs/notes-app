# Notes web app

A simple [web application](https://medium.com/@essentialdesign/website-vs-web-app-whats-the-difference-e499b18b60b4) created with [Django](https://www.djangoproject.com/), a [Python](https://www.python.org/)-based web framework, for taking notes.

<img src="Demo.gif" width="700">

## Requirements

- Python version 3.6+ to run a Python server on your device ([download here](https://www.python.org/downloads/))

## How to install

1. Pull the repository
2. Open the Command Prompt and navigate to the repository's root directory
3. Run `pip install -r requirements.txt` and wait until all necessary modules are installed

## How to view

1. Run `python manage.py runserver` in the Command Prompt in the repository's root directory
2. View the app at `http://127.0.0.1:8000/`

For quicker access you can create a shortcut that will run these 2 steps on a single click.
The app will also run automatically, if you deploy it to a web server.

## Notes app or blog app

Depending on whether users should be able to see or modify other users' posts (in case this application gets deployed on a web server), this app can be easily converted between a blog and a note-taking app.

To do this, there are 2 files where some lines of code need to be commented out and some need to be uncommented (which is explained in comments):
- `blog/views.py`
- `blog/templates/blog/post_detail.html`

## Django topics covered

- Authentication
- Models, views and templates
- Static files
- Forms and form validation
- File upload with drag-and-drop
- Pagination
- Search
- Signals
- 403, 404 and CSRF error handling

## License

[Unlicensed](https://unlicense.org) (You can use the app anyway you want for free and without attribution).

🙂

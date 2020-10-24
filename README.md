# Notes web app

A simple [web application](https://medium.com/@essentialdesign/website-vs-web-app-whats-the-difference-e499b18b60b4) created with [Django](https://www.djangoproject.com/), a [Python](https://www.python.org/)-based web framework, for taking notes.

![A notes app](Demo.gif)

## Requirements

- Python version 3.6+ or higher to run a Python server on your device ([download here](https://www.python.org/downloads/))

## How to view / install

1. Pull the repository
2. Open the Command Prompt and navigate to the repository's root directory
3. Run `pip install -r requirements.txt` and wait until all necessary modules are installed
4. Run `python manage.py runserver`
5. View the app at `http://127.0.0.1:8000/`

##### Notes

You will need to run a local server every time you want to launch the app (repeating the steps 2, 4 and 5), but for a quicker access you can create a shortcut that will do all these steps just on a single click.
If you deploy the app to a web server, then it will run automatically on its web address.

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

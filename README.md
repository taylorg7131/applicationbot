# Job Application Bot

## Overview

**The Job Application Bot** is a Python-based web application that allows users to search for jobs on Indeed, select jobs from the search results, and apply for them automatically. Users can register, log in, and manage their job applications through a web interface.

## Features

- User registration and login
- Job search using Indeed
- Select and apply to jobs from search results
- Email notifications for job applications

## Setup and Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/job-application-bot.git
cd job-application-bot
```
2. **Create and activate a virtual environment**

```bash
python3 -m venv job-bot-env
source job-bot-env/bin/activate
```
3. **Install the dependencies**

```bash
pip install -r requirements.txt
```
4. **Run the application**

```bash
python app.py
```

## Usage

- Navigate to `http://127.0.0.1:5000` in your web browser.
- Register for a new account or log in with an existing account.
- Enter the job keyword and location to search for jobs.
- Select the jobs you want to apply for and submit the form.

## Project Structure

- `app.py`: Main Flask application file.
- `models.py`: User model and in-memory user store.
- `forms.py`: Flask-WTF forms for login and registration.
- `templates/`: HTML templates for the web application.
- `static/`: Static files (CSS, JavaScript, images).

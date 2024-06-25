# app.py

## Overview

This is the main Flask application file for the Job Application Bot. It defines the routes, views, and integrates with Flask-Login for user authentication.

## Routes

- `/`: Main page for job search (requires login).
- `/results`: Page displaying job search results and allowing users to select jobs to apply for (requires login).
- `/login`: Login page.
- `/register`: Registration page.
- `/logout`: Logout route.

## Functions

- `scrape_indeed_jobs(keyword, location)`: Scrapes job listings from Indeed based on the provided keyword and location.
- `load_user(user_id)`: Loads a user by ID for Flask-Login.

# models.py

## Overview

This file defines the `User` class and a simple in-memory user store for managing user registration and authentication.

## Classes

- `User`: Represents a user in the application.
  - `get(user_id)`: Retrieves a user by ID.
  - `find_by_username(username)`: Finds a user by username.
  - `register(id, username, password)`: Registers a new user.

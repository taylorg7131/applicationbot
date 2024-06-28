# User Storage Documentation

## Overview

This document explains how user data is stored and managed in the Job Application Bot using a simple in-memory storage.

## User Model

### Overview

- **Attributes**: Each user has an ID, username, and password.
- **Methods**: Includes methods to register a user, find a user by username, and retrieve a user by ID.

### Storage

- **In-Memory Store**: Users are stored in a Python dictionary where keys are user IDs and values are user objects.

## User Registration and Login

### Registration

- **Process**: Checks if the username already exists. If not, it registers the user.

### Login

- **Process**: Validates the provided username and password. Logs in the user if credentials are correct.

## Routes

- **/register**: Handles user registration.
- **/login**: Handles user login.
- **/logout**: Handles user logout.

## Summary

This documentation provides a basic overview of how user storage is managed using an in-memory store in the Job Application Bot.

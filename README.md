# Hashira Hub

Hashira Hub is a web-based Kanban/task board application designed to help users manage their tasks and projects efficiently. The application allows users to create boards for different projects, add columns to represent different stages of tasks, and manage tasks and subtasks within these columns. Users can also upload files to tasks and add comments, facilitating better collaboration and organization.

## Features

- User Registration and Authentication
- User Profile Management
- Board Management
- Column Management
- Task and Subtask Management
- File Uploads for Tasks
- Commenting System for Tasks
- Task Notifications
- Responsive Design for Desktop and Mobile Use
- Admin Dashboard
- User Role Management
- Security Measures

## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/my_flask_project.git
   cd my_flask_project
   ```

2. **Install Poetry:**

   If you don't have Poetry installed, you can install it using the following command:

   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install dependencies:**

   ```sh
   poetry install
   ```

4. **Create a `.env` file:**

   ```sh
   cp .env.sample .env
   ```

5. **Run the project:**

   ```sh
   poetry run flask run
   ```

## Maintaining the `.env` and `.env.sample` files

1. **Update the .env.sample file:**

   Whenever you add or update environment variables in the .env file, run the following script to synchronize the .env.sample file:

   ```sh
   poetry run python update_env_sample.py
   ```

2. **Automate the update process:**

   We have set up a pre-commit hook using pre-commit to automate the update process. This ensures that .env.sample is always in sync with .env before any commit is made.

   Install pre-commit:

   ```sh
   poetry add pre-commit --dev
   ```

   Install the pre-commit hook:

   ```sh
   poetry run pre-commit install
   ```

   Run pre-commit for all files (first-time setup):

   ```sh
   poetry run pre-commit run --all-files
   ```

   Now, whenever you commit changes, the pre-commit hook will run and update the .env.sample file if necessary.

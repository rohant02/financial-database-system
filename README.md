# Financial Database System

This project is the final submission for a 300-hour Python Web Development course. It is a comprehensive financial database system designed to manage various financial operations.

## Features

- **User Management**: Handle user registration, login, and profile management.
- **Account Management**: Manage bank accounts, including creation, deletion, and updates.
- **Transactions**: Record and view transactions for different accounts.
- **Loans**: Apply for and manage loans.
- **Database**: SQLite3 is used for the database.

## Prerequisites

- Python 3.6 or higher
- Django 3.1 or higher

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/rohant02/financial-database-system.git
    cd financial-database-system
    ```

2. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    python manage.py migrate
    ```

5. **Run the server:**

    ```bash
    python manage.py runserver
    ```

## Usage

After starting the server, navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser. You can register a new user, log in, and start managing your financial operations.

## Project Structure

- `accounts/`: Handles account-related functionalities.
- `bank_system/`: Main app directory.
- `loans/`: Manages loan-related operations.
- `transactions/`: Handles transactions between accounts.
- `users/`: Manages user-related functionalities.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django's command-line utility for administrative tasks.
- `requirements.txt`: List of dependencies.

## API Endpoints

### User Management

- **Register**: `/api/register/`
- **Login**: `/api/login/`
- **Profile**: `/api/profile/`

### Account Management

- **Create Account**: `/api/accounts/create/`
- **Delete Account**: `/api/accounts/delete/<id>/`

### Transactions

- **Add Transaction**: `/api/transactions/add/`
- **View Transactions**: `/api/transactions/view/`

### Loans

- **Apply for Loan**: `/api/loans/apply/`
- **View Loans**: `/api/loans/view/`

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are reviewed actively.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

This project was built as part of a comprehensive Python Web Development course. Special thanks to the course instructors and peers for their guidance and support.


# Learn Pydantic 

This project demonstrates the use of Pydantic for data validation and settings management in Python. It includes a `User` model with custom validation and a `Settings` class for environment-based configuration.

## Features
- **User Model** (`main.py`):
  - Validates user data (e.g., `id`, `name`, `email`, `age`, `password`).
  - Enforces constraints like positive `id`, valid `age`, and matching passwords.
  - Uses custom validators for non-empty names and password matching.
  - Handles validation errors gracefully.
- **Settings Management** (`settings.py`):
  - Loads configuration from a `.env` file (e.g., `API_KEY`, `DEBUG`).
  - Uses `pydantic_settings` for robust environment variable handling.

## Prerequisites
- Python 3.8+
- `pydantic` and `pydantic-settings` libraries

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:imsnto/learn-pydantic.git
   cd pydantic
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install pydantic pydantic-settings
   ```
4. Create a `.env` file in the project root with the following:
   ```
   API_KEY=your-api-key
   DEBUG=False
   ```

## Usage
1. Run the main script to test user validation:
   ```bash
   python main.py
   ```
   Example output:
   ```
   {'id': 1, 'name': 'T', 'email': None, 'age': 10, 'password': '12345678', 'confirm_password': '12345678'}
   Done
   ```
2. Run the settings script to check configuration:
   ```bash
   python settings.py
   ```
   Example output:
   ```
   API KEY: your-api-key
   Type of DEBUG: <class 'bool'>
   ```

## Project Structure
```
├── .env                   # Environment variables (not tracked)
├── .gitignore             # Git ignore file
├── main.py                # User model with Pydantic validation
├── settings.py            # Settings management with pydantic-settings
└── README.md              # Project documentation
```

## Notes
- The `.env` file is ignored by Git for security. Ensure it exists locally with valid values.
- The `.idea/` directory (for JetBrains IDEs) is also ignored in `.gitignore`.
- Validation errors in `main.py` are caught and displayed with details.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.
## Resources
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [Pydantic Settings](https://pydantic-docs.helpmanual.io/usage/settings/)
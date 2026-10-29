# Flask Assignment Collection

This repository contains a set of Flask exercises and example projects collected as part of a learning assignment. It includes basic examples, intermediate projects (SQLite, login, RESTful APIs, error handling), and real-time apps (chat, updates) along with templates and static assets.

## Repository structure

- Flask_Assignment/: collection of example scripts and sub-projects
  - Basic_1.py ... Basic_5.py — simple Flask examples/demos
  - Intermediate_1.py — intermediate-level example
  - Intermediate_2_SQLIte/ — SQLite example
  - Intermediate_3_Flask_login/ — user authentication example
  - Intermediate_4_RESTFUL_API/ — RESTful API example
  - Intermediate_5_Handling_Errors/ — error handling examples
  - Real_time_1_chat_app/ — real-time chat example
  - Real_time_2_updates/ — real-time updates example
  - static/ — static assets
  - templates/ — Jinja2 templates
- requirements.txt — Python dependencies


## Purpose

The project is intended to teach and demonstrate building web applications with Flask, covering beginner to intermediate topics such as routing, templating, forms, persistence (SQLite), authentication, RESTful APIs, error handling, and real-time WebSocket-based features.


## Installation

1. Clone the repository:

   git clone https://github.com/ChetanFernandes/Flask.git
   cd Flask

2. Create and activate a Python virtual environment (recommended):

   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate   # Windows (PowerShell)

3. Install dependencies:

   pip install -r requirements.txt


## Running examples

Basic examples (single-file demos):

- Run a basic example directly:

  python Flask_Assignment/Basic_1.py

Repeat for Basic_2.py ... Basic_5.py.

Intermediate projects and apps:

- Many of the subdirectories contain standalone Flask apps. Typical steps:

  cd Flask_Assignment/Intermediate_4_RESTFUL_API
  # either run the module or set FLASK_APP if applicable
  python app.py
  # or
  export FLASK_APP=app.py
  flask run

- Check each subdirectory for a README or instructions inside the folder for specific run commands.

Real-time apps:

- The real-time (chat/updates) examples may require running with a WebSocket-enabled server such as Flask-SocketIO. Example:

  python Flask_Assignment/Real_time_1_chat_app/app.py

- Ensure dependencies for SocketIO are installed (e.g., flask-socketio).


## Usage examples

- Browse to http://127.0.0.1:5000 after starting a Flask app to interact with it in the browser.
- Use curl or HTTP clients to test RESTful endpoints in the REST API example, e.g.:

  curl http://127.0.0.1:5000/api/items


## Detected license

No LICENSE file was found in the repository root. This repository currently has no explicit license. If you want the code to be reusable by others, add a license (e.g., MIT, Apache-2.0, GPL-3.0). Example: create a `LICENSE` file with the license text and add a short license section here.


## Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repository
2. Create a topic branch: git checkout -b feature/your-feature
3. Make changes and commit
4. Open a Pull Request describing your changes

Please include tests or usage notes for new features and follow Python/Flask best practices.


## Security

If you find a security issue, please open an issue or contact the repository owner directly. Avoid committing secrets (API keys, passwords) into the repository.


## Contact

Repository owner: https://github.com/ChetanFernandes


---

*This README was generated automatically. If you want me to commit it to the repository directly, reply with explicit confirmation and provide the method of authorization (e.g., a GitHub token or ask me to create a branch + PR instead).*

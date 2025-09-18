### VIRTUAL ENVIRONMENT MANAGEMENT

This project does not commit the .venv/ folder to version control. The .venv directory contains a full copy of the Python interpreter, platform-specific binaries, and installed packages. It can easily exceed hundreds of megabytes, and its contents differ depending on the operating system (Windows vs. Linux vs. macOS).

Instead, this repository tracks a requirements.txt file, which specifies all Python dependencies needed to reproduce the environment. This follows common software engineering practice and ensures that collaborators can create a clean, reproducible environment on their own systems.

## SETUP INSTRUCTIONS

Ensure Python 3.9+ is installed (same version used during development).

Create a new virtual environment in the project root:
python -m venv .venv

Activate the virtual environment:

Windows (PowerShell):

```..venv\Scripts\Activate```

macOS/Linux (bash/zsh):

```source .venv/bin/activate```

Install all required dependencies:

```pip install -r requirements.txt```

Run the Django development server:

```python manage.py runserver```

## RATIONALE

Tracking only requirements.txt ensures a lightweight repository and consistent dependency management across environments. Each contributor recreates .venv locally, avoiding platform-specific conflicts.

@echo off

@rem Set the Python path.
set PYTHON_PATH="python"

@rem Set the environment name.
set ENV_NAME="env"

@rem Create a Python environment.
if not exist %ENV_NAME% (
    %PYTHON_PATH% -m venv %ENV_NAME%
)

@rem Activate the Python environment.
call .\%ENV_NAME%\Scripts\Activate.bat

@rem Run the main.py file.
%PYTHON_PATH% main.py

@rem Deactivate the Python environment.
deactivate
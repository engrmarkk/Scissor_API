#! /bin/bash

# Create a virtual environment if the directory does not exist
if [ ! -d "env" ]; then
  python3 -m venv env
fi

echo "Detected OS: $OSTYPE"

# Case statement to handle different OS types
case "$OSTYPE" in
  darwin*)  # macOS
    echo "macOS detected"
    # Activate the virtual environment
    source env/bin/activate
    export FLASK_APP=app_config.py
    ;;

  linux*)   # Linux
    echo "Linux detected"
    # Activate the virtual environment
    source env/bin/activate
    export FLASK_APP=app_config.py
    ;;

  msys*|cygwin*)  # Windows (MSYS/Cygwin)
    echo "Windows detected"
    # Activate the virtual environment
    source env/Scripts/activate
    export FLASK_APP=app_config.py
    ;;

  *)         # Unknown OS
    echo "Unknown OS type: $OSTYPE"
    exit 1
    ;;
esac

# Install dependencies
#pip3 install -r requirements.txt

# Run migration if the migration directory does not exist
if [ ! -d "migrations" ]; then
  python3 -m flask db init
fi

python3 -m flask db migrate
python3 -m flask db upgrade

echo "Server running...."
python3 app_config.py

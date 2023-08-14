# install requirements.txt for project
# Usage: source setup.sh

# create virtual environment
python3 -m venv assignment_1_lanAna_venv

# activate virtual environment
source ./assignment_1_lanAna_venv/bin/activate

# Install requirements
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

# Install language model
python3 -m spacy download en_core_web_md # Medium sized model

# run the code
python3 main.py

# Extra: Type ```python3 main.py --help``` to see the help message for the adjustable parameters

# Deactivate virtual environment
deactivate
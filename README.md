# chemical-formula-finder

## Chemical Formula Finder
A web application that allows users to search for chemical information using names or identifiers. This app retrieves comprehensive details about chemicals including their IUPAC names, common names, molecular weights, and structural formulas.

# Features
Chemical Lookup: Enter any chemical name to find its information
Detailed Information Display:
IUPAC Name
Common Name/Synonyms
Molecular Weight
Chemical Formula
Molecular Structure Visualization: View the 2D structure of the compound
Error Handling: Clear messages for compounds that cannot be found
Installation
Prerequisites
Python 3.7 or higher
pip package manager
Setup Instructions
Clone this repository:

git clone https://github.com/yourusername/chemical-formula-finder.git
cd chemical-formula-finder
Create and activate a virtual environment (optional but recommended):

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
Install the required dependencies:

pip install -r requirements.txt
Usage
Start the Streamlit application:

streamlit run app.py
Open your web browser and navigate to the URL displayed in the terminal (typically http://localhost:8501)

Enter a chemical name (e.g., "methane", "aspirin", "caffeine") in the search box and press Enter or click the Search button

View the chemical information and structure displayed on the page

How It Works
The application uses PubChemPy to access the PubChem database maintained by the National Center for Biotechnology Information (NCBI). When you enter a chemical name:

The app sends a request to the PubChem database via the PubChemPy API
PubChem returns detailed information about the compound
The app extracts relevant information and displays it in a user-friendly format
The molecular structure is retrieved from PubChem and displayed as an image
Dependencies
Streamlit: Web application framework
PubChemPy: Python interface to PubChem
See requirements.txt for a complete list of dependencies
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
PubChem for providing the chemical database
The PubChemPy developers for creating the Python interface
Streamlit team for the intuitive web app framework

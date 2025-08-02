# Resume Parser NER
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Spacy](https://img.shields.io/badge/Spacy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)](https://spacy.io/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![FitZ](https://img.shields.io/badge/FitZ-008000?style=for-the-badge&logo=fitz&logoColor=white)](https://pymupdf.readthedocs.io/en/latest/index.html)

## Overview
The Resume Parser NER is a project designed to parse resumes and extract relevant information using Natural Language Processing (NLP) techniques. The project utilizes the Spacy library for entity recognition and the FitZ library for reading PDF files.

## Key Features
* 📄 **Resume Parsing**: Extract text from PDF resumes
* 📊 **Entity Recognition**: Identify and extract entities such as names, locations, and organizations
* 💼 **Skill Matching**: Match skills extracted from resumes with predefined skill sets

## Technology Stack
* Backend: Python
* ML: Spacy
* Libs: FitZ, Streamlit
* Database: None

## Getting Started
To get started with the project, follow these steps:
1. Clone the repository using `git clone https://github.com/JananiSoundararajan/resume-parser-ner.git`
2. Install the required libraries using `pip install -r requirements.txt`
3. Run the application using `python app.py` or `streamlit run app.py`

## Usage
To use the project, simply upload a PDF resume to the application, and it will extract the relevant information and display it in a user-friendly format.

## Configuration
No specific configuration is required for this project. However, you may need to install additional libraries or dependencies depending on your system requirements.

## Contributing
Contributions are welcome! If you'd like to contribute to the project, please fork the repository and submit a pull request with your changes.

## License
No license information is provided.

## Project Structure
The project structure is as follows:
* `app.py`: The main application file
* `main.py`: The main entry point for the project
* `parser/`: A directory containing the parsing logic
	+ `ner.py`: Entity recognition logic
	+ `pdfreader.py`: PDF reading logic
	+ `skill_matcher.py`: Skill matching logic
	+ `utils.py`: Utility functions
* `outputs/`: A directory containing the output files
* `sample_resumes/`: A directory containing sample resumes

## Credit
Built with ❤️ by Janani Soundararajan

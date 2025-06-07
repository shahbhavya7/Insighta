import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') # Setting up logging configuration 


project_name = "Insighta" # Replace with your project name

list_of_files = [ # List of files to be created 
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]


for filepath in list_of_files: # Iterate through the list of files and create them
    # Create directories and files if they do not exist
    filepath = Path(filepath) # Convert to Path to windows compatible path
    filedir, filename = os.path.split(filepath) # Split the path into directory and filename

    if filedir != "": # If the directory part is not empty, create the directory
        # Create the directory if it does not exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}") # Log the creation of the directory

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # if the file does not exist or is empty then create it
        # Create an empty file
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")

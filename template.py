import os 
from pathlib import Path 
import logging 

#logging string

logging.basicConfig(level = logging.INFO, format='[%(asctime)s]:%(message)s:')  #asctime -> timestamp and message fetches logging.info from below

project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",           # no use of git keep just to have some file 
    f"src/{project_name}/__init__.py",      # src -> source folder contains maximum compnents internally 
    f"src/{project_name}/components/__init__.py", #src/components will have data ingestion, model training and many more
    f"src/{project_name}/utils/__init__.py",    #src/utils will contain utility files
    f"src/{project_name}/config/__init__.py",    
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",  
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)   # makes the filepath into os specfic path 
    filedir, filename = os.path.split(filepath)    # implicit splitting


    if filedir !="":            #making directory 
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #making file
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")
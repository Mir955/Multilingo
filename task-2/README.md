
# Welcome to Duolingo API!  
  
This module is written to create a Python API using Flask. It can be used to fetch 10 number of sentence pairs from the database of 100 sentence pairs stored in an Excel.  
  
### Quick start

##### For local deployment   
  
 - create a anaconda virtual environment `conda create -n multilingo python=3.9`  
 - activate the virtual environment `conda activate multilingo`  
 - install the dependencies `pip install -r requirements.txt`  
- execute  `python main.py`  

#####  For Docker 

 - build docker image `docker build -t translation_app .`
 - run container  `docker run -d -p 8000:8000 translation_app`

  
  
### Folder structure  
1. `app/` - folder containing routes, sentence fetching logic, excel master data, logs   
2. `main.py` - entrypoint to routes  
3. `requirements.txt` - python dependencies  
4. `Dockerfile ` - Docker description
  
### Files  
  
Excel file provided by Carol (ceo from Multilingo) is cleaned as a part of task 1 and the cleaned file is used in this module as a master database.  
  
### Endpoints  
1. GET /api/v1/status  
  
   - returns appropriate status code of API  
  
2. GET /api/v1/sentences  
  
   - returns 10 sentences pairs in a list  
  
   - returns appropriate status code  
   - response = `jsonify({"data": data, "message": message}), status`  
  
### Author  
  
 - Mihir Shah   
 - [mihirshah1328@gmail.com](mailto:mihirshah1328@gmail.com)
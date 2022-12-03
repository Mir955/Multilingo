# Multilingo

*Carol is the CEO of Multilingo, a language learning platform. She takes digital lectures on the app. 
She wants to integrate a feature on the app in which students can practice translation skills by 
studying 10 translations a day. She has 100 sets of parallel sentences for this task which is scrapped 
from a website.*


# Task 1

Being the data scientist of Multilingo, analyze the scraped dataset using your Python skills. The goal 
is to make the data suitable for reading by the students. Use your imagination to apply different 
processing steps to make the data clean (syntactically and semantically).

*Since you have prepared the data which can be used by students to study translation, now is the time 
for integrating this feature in the app. The frontend engineer needs 10 translation sentence pair from 
a data upon a request sent to backend.*

## Task 2

Being a data scientist of a startup and a small team, you take care of API's related to machine learning 
models. Please help the team by writing a Flask-based API which returns 10 translation pairs from the 
dataset.

*Carol is happy with the new feature of Multilingo. Now she wants to help the visually challenged students 
on the app with the help of optical character recognition (OCR) technology.*

## Task 3

Being the data scientist of Multilingo, you should help Carol with information about state-of-the-art OCR 
technology. She is looking for the internal mechanism, any already done implementation, how to train 
(if applicable), how to serve and evaluate such technology. Therefore, please conduct initial research on 
the former mentioned topic and bits and prepare a short report(doc/ppt) for your pitch to Carol.


## Recommendation 

1.  Use Jupyter notebook for Task 1 i.e., data processing task to make it interactive for us to understand 
your thoughts.
    

2.  Use suitable headings and proper comments when required.
    

3.  Use Python 3.9 or above.
    

4.  Write python code with PEP8 compliance.
    

5.  Store the provided parallel sentence data file as you like. Using excel/csv with pandas is fine.
    

6.  Pack the work of Task 2 into docker container and use CI (continuous integration) for Task 2 in any cloud 
git repository. GitHub action is preferable.
    

7.  Document the repository with proper **README.md** file.
    

8.  Do not complex any step. Try to keep everything simple.
    

9.  Task 3 documentation should not be more than 5 slides or 3 pages in doc.
    

10.  Approach as much as you can and let us know the status of your solution correctly.

## Endpoints to implement

    1. GET /api/v1/status
    
	    - returns appropriate status code of API

    2. GET /api/v1/sentences
    
	    - returns 10 sentences in a list
    
	    - returns appropriate status code

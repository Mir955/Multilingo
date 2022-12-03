from flask import Flask
import logging
from app.get_translations import sentence_route
import os

# for logging errors and info
if not os.path.isdir("app/logs"):
    os.makedirs("app/logs")
logging.basicConfig(filename='app/logs/record.log', format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)

app = Flask(__name__)
sentence_route(app)

if __name__ == '__main__':
    # run api in debug mode
    app.run(debug=True, host='0.0.0.0', port=8000)

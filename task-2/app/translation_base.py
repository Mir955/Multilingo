import pandas as pd
from http import HTTPStatus


def get_ten_translation():
    """
    fetch 10 sentence pair randomly from the Excel files
    :return:http_status_code, message, data(sentence-pair)
    """
    try:
        df = pd.read_excel("app/data/translation-data.xlsx")
        parallel_sentence = df.sample(10).to_dict('records')
        return HTTPStatus.OK, "Data read successfully!", parallel_sentence
    except (FileNotFoundError, IOError):
        return 204, "File not exist!", None
    # if error happens in sampling
    except ValueError:
        return 500, "Not sufficient sentences found!", None

from flask import jsonify, make_response
from http import HTTPStatus
from app.translation_base import get_ten_translation
from CONFIG import API_VERSION


def sentence_route(app):
    # handle 404 error
    @app.errorhandler(404)
    def handle_404_error(_error):
        return make_response(jsonify({"message": "Page not found!"}), HTTPStatus.NOT_FOUND)

    # handle 500 error
    @app.errorhandler(500)
    def handle_500_error(_error):
        return make_response(jsonify({"message": "Internal server error!"}), HTTPStatus.INTERNAL_SERVER_ERROR)

    # route for health check
    @app.route(f"{API_VERSION}/status", methods=['GET'])
    def health_check():
        return "Success", HTTPStatus.OK

    # route for fetching 10 sentence
    @app.route(f"{API_VERSION}/sentence", methods=['GET'])
    def get_sentence():
        status: HTTPStatus
        status, message, data = get_ten_translation()
        if status == HTTPStatus.OK:
            app.logger.info(message)
        else:
            app.logger.error(message)
        return make_response(jsonify({"data": data, "message": message}), status)

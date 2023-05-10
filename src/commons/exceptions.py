from flask import jsonify


def error_template(data, status_code=400):
    return {
        'status_code': status_code,
        'message': data['message'],
        'error': data['error'],
        'payload': data['payload'],
    }


class ApiException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None, error=None):
        Exception.__init__(self)
        if status_code is not None:
            self.status_code = status_code
        self.response = error_template({
            message,
            payload,
            error
        }, self.status_code)

    def to_json(self):
        rv = self.response
        return jsonify(rv)

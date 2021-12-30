import json

class HttpResponseUtils:
    @staticmethod
    def get_response(http, status, message, data=[]):
        http.send_response(status)
        http.send_header('Content-type', 'application/json')
        http.end_headers()

        response = {
            'status': status,
            'data': data,
            'message': message
        }

        http.wfile.write(json.dumps(response, ensure_ascii=False).encode(encoding='utf_8'))

    @staticmethod
    def get_success_response(http, message, data=[]):
        HttpResponseUtils.get_response(http, 200, message, data)

    @staticmethod
    def get_bad_request_response(http, message):
        HttpResponseUtils.get_response(http, 400, message)

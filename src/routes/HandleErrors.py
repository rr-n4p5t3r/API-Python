from flask import jsonify
def page_not_found(error):
    return jsonify({
            "error_code": 404,
            "message": "Página no encontrada"
        }), 404
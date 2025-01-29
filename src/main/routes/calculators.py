from flask import Blueprint, jsonify, request
from ..factories.calculator4_factory import calculator4_factory
from ...errors.error_controller import handle_errors

calc_rout_bp = Blueprint("calc_routes", __name__)


@calc_rout_bp.route("/calculator/4", methods=["POST"])
def calculator_1():
    try:
        calc = calculator4_factory()
        response = calc.calculate(request)

        return jsonify(response)
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]

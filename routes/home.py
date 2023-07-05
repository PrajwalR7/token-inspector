from flask import Blueprint, request
import json
from utils.get_num_token import get_num_token

home_bp = Blueprint('home_blueprint', __name__)

@home_bp.route('/', methods=["POST"])
def index():
    body = json.loads(request.data)
    num_token = get_num_token(body)
    return {
        'num_token': num_token
    }

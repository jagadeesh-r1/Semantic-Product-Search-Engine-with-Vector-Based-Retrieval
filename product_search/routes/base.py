from flask import Blueprint,request
from flask_cors import cross_origin
from product_search.services import search_db

base = Blueprint('base',__name__)

@base.route('/search',methods=['POST'])
@cross_origin(supports_credentials=True)
def index():
    query = request.json["query"]
    response = search_db.search_products(query)
    response = {"products":response}
    
    return response

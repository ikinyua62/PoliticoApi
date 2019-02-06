from flask import jsonify, make_response
from flask import jsonify, make_response, request
from app.models import PartyModel
from app.party import party

@party.route('/parties', methods=['GET'])
def get_parties():
    if len(PartyModel.parties_db) <= 0:
        return make_response(jsonify({
            'status': 'Not Found',
            'message': 'No parties to show'
        }), 404)
    else:
        return make_response(jsonify({
            'status':'OK',
            'parties': parties_db
        }), 200) 
        
                    'parties': PartyModel.parties_db
        }), 200)

@party.route('/addparty', methods=['POST'])
def add_party():
    data = request.get_json()
    name = data['name']
    hqAddress = data['hqAddress']
    logoUrl = data['logoUrl']
    id = len(PartyModel.parties_db) + 1

    new_party = {
        'id' : id,
        'name' : name,
        'hqAddress' : hqAddress,
        'logoUrl' : logoUrl 
    }

    PartyModel.parties_db.append(new_party)

    return make_response(jsonify({
        'Status' : 'OK',
        'Message' : 'New Party added',
        'Party' : new_party['name']
    }), 201)
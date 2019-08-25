from Model.soccer_team import SoccerTeam
from Model.player import Player
from Model.manager import Manager
import json
from flask import Flask, request

app = Flask(__name__)

# soccer_team = SoccerTeam('../team.json')
MEMBERS_DB = 'members.sqlite'

member_mgr = SoccerTeam(MEMBERS_DB)

@app.route('/soccer_team/member', methods=['POST'])
def add_member():
    """ Adds a member to a team """
    content = request.json
    try:
        if content['type'] == 'manager':
            member1 = Manager(content['f_name'], content['l_name'], content['address'], content['phone'],
                             content['position'], content['salary'], content['type'])
            num = member_mgr.add_member(member1)
            response = app.response_class(
                response="New member ID: %s" % (str(num)),
                status=200
            )
        elif content['type'] == 'player':
            member1 = Player(content['f_name'], content['l_name'], content['address'], content['phone'],
                             content['position'],
                             content['jersey_number'], content['wage'], content["type"])
            num = member_mgr.add_member(member1)
            response = app.response_class(
                response="New member ID: %s" % (str(num)),
                status=200
            )
        else:
            raise ValueError('JSON object invalid')

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )
    return response


@app.route('/soccer_team/member/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    """ Updates a member on a team """
    content = request.json

    try:
        if content["type"] == "manager":
            member1 = Manager(content['f_name'], content['l_name'], content['address'],
                              content['phone'],
                              content['position'], content['salary'], content["type"])
            member1.member_id = member_id
            member_mgr.update(member1)
            response = app.response_class(
                response="ok",
                status=200
            )
            return response
        elif content["type"] == "player":
            member1 = Player(content['f_name'], content['l_name'], content['address'],
                             content['phone'], content['position'], content['jersey_number'], content['wage'], content["type"])
            member1.member_id = member_id
            member_mgr.update(member1)
            response = app.response_class(
                response="ok",
                status=200
            )
            return response
    except KeyError:
        print("Wrong JSON format")

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )
        return response


@app.route('/soccer_team/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    """ Delete a member from team """
    try:
        member_mgr.delete(member_id)
        response = app.response_class(
            response="OK",
            status=200
        )

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
    return response


@app.route('/soccer_team/member/<int:id>', methods=['GET'])
def get_member(id):
    """ returns a member on a team """

    try:
        member = member_mgr.get_member(int(id))
        if member != None:
            response = app.response_class(
                status=200,
                response=json.dumps(member.to_dict()),
                mimetype='application/json'
            )
        else:
            response = app.response_class(
                status=404,
                response="No member with that ID found"
            )
        return response
    except ValueError as e:
        response = app.response_class(
            status=400,
            response=e
        )
    return response


@app.route('/soccer_team/member/all', methods=['GET'])
def get_all():
    """ returns all members on a team """

    members = member_mgr.get_team_members()
    member_list = []
    for member in members:
        member_list.append(member.to_dict())

    response = app.response_class(
        status=200,
        response=json.dumps(member_list),
        mimetype='application/json'
    )
    return response


@app.route('/soccer_team/member/all/<type>', methods=['GET'])
def get_type(type):
    """ returns all members of a type on a team """

    if type != "player" and type != "manager":
        response = app.response_class(
            status=400,
            response="Invalid member type"
        )
        return response

    try:
        members = member_mgr.get_member_by_type(type)
        member_list = []
        for member in members:
            member_list.append(member.to_dict())

        response = app.response_class(
            status=200,
            response=json.dumps(member_list),
            mimetype='application/json'
        )
    except ValueError as e:
        response = app.response_class(
            status=404,
            response=e
        )

    return response


if __name__ == "__main__":
    app.run()
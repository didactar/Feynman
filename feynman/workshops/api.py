from flask import request
from flask import jsonify
from .models import Workshop
from . import workshops



@workshops.route('/workshops', methods=['GET', 'POST'])
def workshop_list():

    if request.method == 'GET':
        workshops = Workshop.get_all()
        response = Workshop.serialize_list(workshops)
        return jsonify(response)

    if request.method == 'POST':
        data = request.get_json()
        workshop = Workshop(data)
        workshop.save()
        response = workshop.serialize()
        return jsonify(response), 201



@workshops.route('/workshops/<workshop_slug>', methods=['GET', 'DELETE'])
def workshop_detail(workshop_slug):

    if request.method == 'GET':
        workshop = Workshop.get_by_slug(workshop_slug)
        if workshop:
            response = workshop.serialize()
            return jsonify(response) 
        return '', 404

    if request.method == 'DELETE':
        workshop = Workshop.get_by_slug(workshop_slug)
        if workshop:
            workshop.delete()
            return '', 204
        return '', 404

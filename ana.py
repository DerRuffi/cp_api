"""
This is the people module and supports all the ReST actions for the
PEOPLE collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort



# Data to serve with our API
PEOPLE = {

}


def create(body):
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    pilotpoint = body.get("ppname", None)
    file_id = body.get("file_id", None)
    print('lol',pilotpoint, file_id)

    # Does the person exist already?
    if pilotpoint not in PEOPLE and pilotpoint is not None:
        PEOPLE[pilotpoint] = {
            "pilotpoint": pilotpoint,
            "file_id": file_id,
        }
        return PEOPLE[pilotpoint], 201

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Person with last name {pilotpoint} already exists".format(pilotpoint=pilotpoint),
        )

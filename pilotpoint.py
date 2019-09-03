"""
This is the people module and supports all the ReST actions for the
pp_dict collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort

# Data to serve with our API
pp_dict = {}
anastep_dict = {}
group_dict = {}


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        json string of list of people
    """
    return [pp_dict[key] for key in sorted(pp_dict.keys())]


def read_one(ppname):
    """
    This function responds to a request for /api/people/{pilotpoint}
    with one matching person from people

    :param pilotpoint:   last name of person to find
    :return:        person matching last name
    """
    if ppname in pp_dict:
        pilotpoint = pp_dict.get(ppname)
    else:
        abort(
            404, "Person with last name {ppname} not found".format(ppname=ppname)
        )
    return pilotpoint


def createpp(body):
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
    if pilotpoint not in pp_dict and pilotpoint is not None:
        pp_dict[pilotpoint] = {
            "pilotpoint": pilotpoint,
            "file_id": file_id,
        }
        return pp_dict[pilotpoint], 201

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Person with last name {pilotpoint} already exists".format(pilotpoint=pilotpoint),
        )

def createanastep(body):
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    pilotpoint = body.get("ppname", None)
    steps = body.get("steps", None)
    print('lol',pilotpoint, steps)

    # Does the person exist already?
    if pilotpoint not in anastep_dict and pilotpoint is not None:
        anastep_dict[pilotpoint] = {
            "pilotpoint": pilotpoint,
            "steps": steps,
        }
        return anastep_dict[pilotpoint], 201

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Person with last name {pilotpoint} already exists".format(pilotpoint=pilotpoint),
        )

def creategroup(body):
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    group = body.get("groupname", None)
    pps = body.get("pilotpoints", None)
    print('lol',group, pps)
    print(type(pps))

    # Does the person exist already?
    if group not in group_dict and group is not None:
        group_dict[group] = {
            "groupname": group,
            "pilotpoints": pps,
        }
        return group_dict[group], 201

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Person with last name {group} already exists".format(group=group),
        )

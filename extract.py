"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    #    self.designation = info.get('pdes','')
    #     self.name = info.get('name',None)
    #     self.diameter = float(info.get('diameter','nan'))
    #     self.hazardous = bool(info.get('pha',False))
    neo = []
    with open(neo_csv_path, "r") as nf:
        reader = csv.DictReader(nf)
        for line in reader:
            neo_instance = NearEarthObject(info=line)
            neo.append(neo_instance)
    return neo


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = []
    with open(cad_json_path, "r") as cf:
        cad_data = json.load(cf)
        keys = cad_data["fields"]
        data = cad_data["data"]
        _dict = {}
        for line in data:
            for i, val in enumerate(line):
                _dict[keys[i]] = val
            cad = CloseApproach(info=_dict)
            approaches.append(cad)
    return approaches

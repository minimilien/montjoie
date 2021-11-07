# -*- coding: utf-8 -*-
import json
from typing import Any


def read_file(path:str) -> str:
    """Returns a file's content."""
    with open(path,"r",encoding="utf-8") as file:
        data = file.read()
    return data


def write_file(path:str,data:Any) -> None:
    """Writes data in a file."""
    with open(path,"w",encoding="utf-8") as file:
        file.write(f"{data}")


def read_json(path:str) -> dict:
    """Loads a dict from a json file."""
    json_string = read_file(path)
    return json.loads(json_string)


def write_json(path:str,data:dict) -> None:
    """Writes a dictionnary in a json file."""
    write_file(path,json.dumps(data))
# coding: utf-8

"""
    RSC API Docs

    RSC API Documentation

    The version of the OpenAPI document: v1
    Contact: contact@snippets.local
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictInt, conlist, constr

class TeamGameListResultsField(BaseModel):
    """
    TeamGameListResultsField
    """
    team: constr(strict=True, min_length=1) = Field(...)
    goals: StrictInt = Field(...)
    shots: StrictInt = Field(...)
    players: conlist(constr(strict=True, min_length=1), max_items=10, min_items=0) = Field(...)
    __properties = ["team", "goals", "shots", "players"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TeamGameListResultsField:
        """Create an instance of TeamGameListResultsField from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamGameListResultsField:
        """Create an instance of TeamGameListResultsField from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamGameListResultsField.parse_obj(obj)

        _obj = TeamGameListResultsField.parse_obj({
            "team": obj.get("team"),
            "goals": obj.get("goals"),
            "shots": obj.get("shots"),
            "players": obj.get("players")
        })
        return _obj



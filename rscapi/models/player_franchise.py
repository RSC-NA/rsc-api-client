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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, constr
from rscapi.models.franchise_gm import FranchiseGM

class PlayerFranchise(BaseModel):
    """
    PlayerFranchise
    """
    name: Optional[constr(strict=True, min_length=1)] = None
    id: Optional[StrictInt] = None
    gm: FranchiseGM = Field(...)
    __properties = ["name", "id", "gm"]

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
    def from_json(cls, json_str: str) -> PlayerFranchise:
        """Create an instance of PlayerFranchise from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "name",
                            "id",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of gm
        if self.gm:
            _dict['gm'] = self.gm.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayerFranchise:
        """Create an instance of PlayerFranchise from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayerFranchise.parse_obj(obj)

        _obj = PlayerFranchise.parse_obj({
            "name": obj.get("name"),
            "id": obj.get("id"),
            "gm": FranchiseGM.from_dict(obj.get("gm")) if obj.get("gm") is not None else None
        })
        return _obj


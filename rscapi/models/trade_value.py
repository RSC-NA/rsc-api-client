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
from pydantic import BaseModel, Field, StrictInt
from rscapi.models.draft_pick import DraftPick

class TradeValue(BaseModel):
    """
    The specific item being traded (player or pick)  # noqa: E501
    """
    player: Optional[StrictInt] = Field(None, description="Discord ID of Player being traded.")
    pick: Optional[DraftPick] = None
    __properties = ["player", "pick"]

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
    def from_json(cls, json_str: str) -> TradeValue:
        """Create an instance of TradeValue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pick
        if self.pick:
            _dict['pick'] = self.pick.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TradeValue:
        """Create an instance of TradeValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TradeValue.parse_obj(obj)

        _obj = TradeValue.parse_obj({
            "player": obj.get("player"),
            "pick": DraftPick.from_dict(obj.get("pick")) if obj.get("pick") is not None else None
        })
        return _obj


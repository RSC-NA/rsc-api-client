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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, conlist, constr
from rscapi.models.tracker_link import TrackerLink

class MemberTracker(BaseModel):
    """
    MemberTracker
    """
    player: constr(strict=True, min_length=1) = Field(...)
    rscid: constr(strict=True, min_length=1) = Field(...)
    discord_id: Optional[StrictInt] = None
    accounts: conlist(TrackerLink) = Field(...)
    __properties = ["player", "rscid", "discord_id", "accounts"]

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
    def from_json(cls, json_str: str) -> MemberTracker:
        """Create an instance of MemberTracker from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "discord_id",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in accounts (list)
        _items = []
        if self.accounts:
            for _item in self.accounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accounts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MemberTracker:
        """Create an instance of MemberTracker from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MemberTracker.parse_obj(obj)

        _obj = MemberTracker.parse_obj({
            "player": obj.get("player"),
            "rscid": obj.get("rscid"),
            "discord_id": obj.get("discord_id"),
            "accounts": [TrackerLink.from_dict(_item) for _item in obj.get("accounts")] if obj.get("accounts") is not None else None
        })
        return _obj


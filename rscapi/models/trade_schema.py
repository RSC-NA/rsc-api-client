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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from rscapi.models.trade_item import TradeItem

class TradeSchema(BaseModel):
    """
    Schema for Pick/Player trades  # noqa: E501
    """
    trades: Optional[conlist(TradeItem)] = Field(None, description="List of trades to execute")
    league: Optional[StrictInt] = Field(None, description="ID of the league transaction is for.")
    executor: Optional[StrictInt] = Field(None, description="Discord ID of specific member who ran the transaction.")
    admin_override: Optional[StrictBool] = Field(None, description="Boolean indicating whether or not an admin is overriding this command.")
    notes: Optional[StrictStr] = Field(None, description="Notes for the transaction from the TM running it.")
    __properties = ["trades", "league", "executor", "admin_override", "notes"]

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
    def from_json(cls, json_str: str) -> TradeSchema:
        """Create an instance of TradeSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in trades (list)
        _items = []
        if self.trades:
            for _item in self.trades:
                if _item:
                    _items.append(_item.to_dict())
            _dict['trades'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TradeSchema:
        """Create an instance of TradeSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TradeSchema.parse_obj(obj)

        _obj = TradeSchema.parse_obj({
            "trades": [TradeItem.from_dict(_item) for _item in obj.get("trades")] if obj.get("trades") is not None else None,
            "league": obj.get("league"),
            "executor": obj.get("executor"),
            "admin_override": obj.get("admin_override"),
            "notes": obj.get("notes")
        })
        return _obj


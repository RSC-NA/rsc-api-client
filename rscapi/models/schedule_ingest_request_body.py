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



from pydantic import BaseModel, Field, StrictStr

class ScheduleIngestRequestBody(BaseModel):
    """
    Values required for schedule submitting for a given season.  # noqa: E501
    """
    sheet_link: StrictStr = Field(..., description="The link to the google sheet containing scheduling information.")
    __properties = ["sheet_link"]

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
    def from_json(cls, json_str: str) -> ScheduleIngestRequestBody:
        """Create an instance of ScheduleIngestRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ScheduleIngestRequestBody:
        """Create an instance of ScheduleIngestRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ScheduleIngestRequestBody.parse_obj(obj)

        _obj = ScheduleIngestRequestBody.parse_obj({
            "sheet_link": obj.get("sheet_link")
        })
        return _obj


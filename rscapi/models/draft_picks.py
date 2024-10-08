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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from rscapi.models.draft_pick_season_tier import DraftPickSeasonTier
from typing import Optional, Set
from typing_extensions import Self

class DraftPicks(BaseModel):
    """
    DraftPicks
    """ # noqa: E501
    number: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(default=None, description="Pick in the specific tier.")
    round: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(default=None, description="Specific round in the tier.")
    gm: StrictInt
    season_tier: DraftPickSeasonTier
    __properties: ClassVar[List[str]] = ["number", "round", "gm", "season_tier"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DraftPicks from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of season_tier
        if self.season_tier:
            _dict['season_tier'] = self.season_tier.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DraftPicks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "number": obj.get("number"),
            "round": obj.get("round"),
            "gm": obj.get("gm"),
            "season_tier": DraftPickSeasonTier.from_dict(obj["season_tier"]) if obj.get("season_tier") is not None else None
        })
        return _obj



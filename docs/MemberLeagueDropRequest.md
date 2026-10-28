# MemberLeagueDropRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** | League ID to drop the member from. | 

## Example

```python
from rscapi.models.member_league_drop_request import MemberLeagueDropRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemberLeagueDropRequest from a JSON string
member_league_drop_request_instance = MemberLeagueDropRequest.from_json(json)
# print the JSON string representation of the object
print(MemberLeagueDropRequest.to_json())

# convert the object into a dict
member_league_drop_request_dict = member_league_drop_request_instance.to_dict()
# create an instance of MemberLeagueDropRequest from a dict
member_league_drop_request_from_dict = MemberLeagueDropRequest.from_dict(member_league_drop_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



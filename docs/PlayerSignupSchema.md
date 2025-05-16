# PlayerSignupSchema

Request body object containing league player signup data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** | League of team player will be captain in | 
**tracker_links** | **List[str]** | List of players tracker links | 
**rsc_name** | **str** | Discord display name of player | 
**accepted_rules** | **bool** | Acknowledgement of player accepting rules | 
**accepted_match_nights** | **bool** | Acknowledgement of player accepting rules | 
**platform** | **str** | Platform the user plays on. | 
**referrer** | **str** | Who referred the player | 
**new_or_returning** | **str** | Is the player new or returning? | 
**region_preference** | **str** | Players specific region preference | 
**admin_override** | **bool** | Admin overriding signup | [optional] 
**executor** | **int** | Admin override executor | [optional] 

## Example

```python
from rscapi.models.player_signup_schema import PlayerSignupSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSignupSchema from a JSON string
player_signup_schema_instance = PlayerSignupSchema.from_json(json)
# print the JSON string representation of the object
print(PlayerSignupSchema.to_json())

# convert the object into a dict
player_signup_schema_dict = player_signup_schema_instance.to_dict()
# create an instance of PlayerSignupSchema from a dict
player_signup_schema_from_dict = PlayerSignupSchema.from_dict(player_signup_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



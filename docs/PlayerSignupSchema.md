# PlayerSignupSchema

Request body object containing league player signup data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** | League of team player will be captain in | 
**tracker_links** | **List[str]** | List of players tracker links | 
**rsc_name** | **str** | Discord display name of player | 

## Example

```python
from openapi_client.models.player_signup_schema import PlayerSignupSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSignupSchema from a JSON string
player_signup_schema_instance = PlayerSignupSchema.from_json(json)
# print the JSON string representation of the object
print PlayerSignupSchema.to_json()

# convert the object into a dict
player_signup_schema_dict = player_signup_schema_instance.to_dict()
# create an instance of PlayerSignupSchema from a dict
player_signup_schema_form_dict = player_signup_schema.from_dict(player_signup_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



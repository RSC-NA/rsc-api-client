# PlayerActivityCheckSchema

Request body for player activity check

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** | League that action is being performed on. | 
**admin_override** | **bool** | Admin overriding signup | [optional] 
**executor** | **int** | Admin override executor | [optional] 
**returning_status** | **bool** | If the player is staying in this season or dropping the league | 

## Example

```python
from rscapi.models.player_activity_check_schema import PlayerActivityCheckSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerActivityCheckSchema from a JSON string
player_activity_check_schema_instance = PlayerActivityCheckSchema.from_json(json)
# print the JSON string representation of the object
print(PlayerActivityCheckSchema.to_json())

# convert the object into a dict
player_activity_check_schema_dict = player_activity_check_schema_instance.to_dict()
# create an instance of PlayerActivityCheckSchema from a dict
player_activity_check_schema_from_dict = PlayerActivityCheckSchema.from_dict(player_activity_check_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



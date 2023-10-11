# PreviousTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional] [readonly] 
**sign_date** | **datetime** |  | [optional] [readonly] 
**release_date** | **datetime** |  | [optional] [readonly] 
**player** | **str** |  | 

## Example

```python
from openapi_client.models.previous_team import PreviousTeam

# TODO update the JSON string below
json = "{}"
# create an instance of PreviousTeam from a JSON string
previous_team_instance = PreviousTeam.from_json(json)
# print the JSON string representation of the object
print PreviousTeam.to_json()

# convert the object into a dict
previous_team_dict = previous_team_instance.to_dict()
# create an instance of PreviousTeam from a dict
previous_team_form_dict = previous_team.from_dict(previous_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



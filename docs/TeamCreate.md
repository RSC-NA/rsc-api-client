# TeamCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**franchise** | [**TeamFranchise**](TeamFranchise.md) |  | 
**tier** | [**Tier**](Tier.md) |  | 
**league** | **int** |  | [optional] 

## Example

```python
from rscapi.models.team_create import TeamCreate

# TODO update the JSON string below
json = "{}"
# create an instance of TeamCreate from a JSON string
team_create_instance = TeamCreate.from_json(json)
# print the JSON string representation of the object
print(TeamCreate.to_json())

# convert the object into a dict
team_create_dict = team_create_instance.to_dict()
# create an instance of TeamCreate from a dict
team_create_form_dict = team_create.from_dict(team_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



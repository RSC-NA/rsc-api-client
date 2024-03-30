# TeamFranchise


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**gm** | [**FranchiseGM**](FranchiseGM.md) |  | 
**name** | **str** |  | 

## Example

```python
from rscapi.models.team_franchise import TeamFranchise

# TODO update the JSON string below
json = "{}"
# create an instance of TeamFranchise from a JSON string
team_franchise_instance = TeamFranchise.from_json(json)
# print the JSON string representation of the object
print(TeamFranchise.to_json())

# convert the object into a dict
team_franchise_dict = team_franchise_instance.to_dict()
# create an instance of TeamFranchise from a dict
team_franchise_form_dict = team_franchise.from_dict(team_franchise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FranchiseTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.franchise_team import FranchiseTeam

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseTeam from a JSON string
franchise_team_instance = FranchiseTeam.from_json(json)
# print the JSON string representation of the object
print(FranchiseTeam.to_json())

# convert the object into a dict
franchise_team_dict = franchise_team_instance.to_dict()
# create an instance of FranchiseTeam from a dict
franchise_team_from_dict = FranchiseTeam.from_dict(franchise_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



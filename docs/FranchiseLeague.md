# FranchiseLeague


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | [optional] [readonly] 
**guild_id** | **int** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.franchise_league import FranchiseLeague

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseLeague from a JSON string
franchise_league_instance = FranchiseLeague.from_json(json)
# print the JSON string representation of the object
print FranchiseLeague.to_json()

# convert the object into a dict
franchise_league_dict = franchise_league_instance.to_dict()
# create an instance of FranchiseLeague from a dict
franchise_league_form_dict = franchise_league.from_dict(franchise_league_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



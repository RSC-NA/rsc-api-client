# FranchiseStandings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**franchise** | **str** |  | 
**gm** | **str** |  | 
**wins** | **int** |  | [optional] 
**losses** | **int** |  | [optional] 
**win_percentage** | **float** |  | [optional] 
**franchise_standings_rank** | **int** |  | 

## Example

```python
from rscapi.models.franchise_standings import FranchiseStandings

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseStandings from a JSON string
franchise_standings_instance = FranchiseStandings.from_json(json)
# print the JSON string representation of the object
print(FranchiseStandings.to_json())

# convert the object into a dict
franchise_standings_dict = franchise_standings_instance.to_dict()
# create an instance of FranchiseStandings from a dict
franchise_standings_form_dict = franchise_standings.from_dict(franchise_standings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



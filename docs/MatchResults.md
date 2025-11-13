# MatchResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_wins** | **int** |  | [optional] 
**away_wins** | **int** |  | [optional] 
**manual** | **bool** |  | [optional] 
**ballchasing_group** | **str** |  | [optional] 

## Example

```python
from rscapi.models.match_results import MatchResults

# TODO update the JSON string below
json = "{}"
# create an instance of MatchResults from a JSON string
match_results_instance = MatchResults.from_json(json)
# print the JSON string representation of the object
print(MatchResults.to_json())

# convert the object into a dict
match_results_dict = match_results_instance.to_dict()
# create an instance of MatchResults from a dict
match_results_from_dict = MatchResults.from_dict(match_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



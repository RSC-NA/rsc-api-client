# ListMatchResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_wins** | **int** |  | [optional] [readonly] 
**away_wins** | **int** |  | [optional] [readonly] 
**games** | [**List[ListGames]**](ListGames.md) |  | 

## Example

```python
from rscapi.models.list_match_results import ListMatchResults

# TODO update the JSON string below
json = "{}"
# create an instance of ListMatchResults from a JSON string
list_match_results_instance = ListMatchResults.from_json(json)
# print the JSON string representation of the object
print ListMatchResults.to_json()

# convert the object into a dict
list_match_results_dict = list_match_results_instance.to_dict()
# create an instance of ListMatchResults from a dict
list_match_results_form_dict = list_match_results.from_dict(list_match_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



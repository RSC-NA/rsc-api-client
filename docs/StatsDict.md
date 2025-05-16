# StatsDict


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blue** | [**TeamGameListResults**](TeamGameListResults.md) |  | 
**orange** | [**TeamGameListResults**](TeamGameListResults.md) |  | 

## Example

```python
from rscapi.models.stats_dict import StatsDict

# TODO update the JSON string below
json = "{}"
# create an instance of StatsDict from a JSON string
stats_dict_instance = StatsDict.from_json(json)
# print the JSON string representation of the object
print(StatsDict.to_json())

# convert the object into a dict
stats_dict_dict = stats_dict_instance.to_dict()
# create an instance of StatsDict from a dict
stats_dict_from_dict = StatsDict.from_dict(stats_dict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



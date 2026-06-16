# PlayoffGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**conference** | **str** |  | 
**accent** | **str** |  | 
**cutoff** | **int** |  | 
**teams** | [**List[PlayoffTeam]**](PlayoffTeam.md) |  | 

## Example

```python
from rscapi.models.playoff_group import PlayoffGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PlayoffGroup from a JSON string
playoff_group_instance = PlayoffGroup.from_json(json)
# print the JSON string representation of the object
print(PlayoffGroup.to_json())

# convert the object into a dict
playoff_group_dict = playoff_group_instance.to_dict()
# create an instance of PlayoffGroup from a dict
playoff_group_from_dict = PlayoffGroup.from_dict(playoff_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



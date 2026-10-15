# PlayoffDivision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**division** | **str** |  | 
**label** | **str** |  | 

## Example

```python
from rscapi.models.playoff_division import PlayoffDivision

# TODO update the JSON string below
json = "{}"
# create an instance of PlayoffDivision from a JSON string
playoff_division_instance = PlayoffDivision.from_json(json)
# print the JSON string representation of the object
print(PlayoffDivision.to_json())

# convert the object into a dict
playoff_division_dict = playoff_division_instance.to_dict()
# create an instance of PlayoffDivision from a dict
playoff_division_from_dict = PlayoffDivision.from_dict(playoff_division_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



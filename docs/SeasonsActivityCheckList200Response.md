# SeasonsActivityCheckList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ActivityCheck]**](ActivityCheck.md) |  | 

## Example

```python
from rscapi.models.seasons_activity_check_list200_response import SeasonsActivityCheckList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonsActivityCheckList200Response from a JSON string
seasons_activity_check_list200_response_instance = SeasonsActivityCheckList200Response.from_json(json)
# print the JSON string representation of the object
print(SeasonsActivityCheckList200Response.to_json())

# convert the object into a dict
seasons_activity_check_list200_response_dict = seasons_activity_check_list200_response_instance.to_dict()
# create an instance of SeasonsActivityCheckList200Response from a dict
seasons_activity_check_list200_response_from_dict = SeasonsActivityCheckList200Response.from_dict(seasons_activity_check_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



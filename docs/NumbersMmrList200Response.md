# NumbersMmrList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PlayerMMR]**](PlayerMMR.md) |  | 

## Example

```python
from rscapi.models.numbers_mmr_list200_response import NumbersMmrList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of NumbersMmrList200Response from a JSON string
numbers_mmr_list200_response_instance = NumbersMmrList200Response.from_json(json)
# print the JSON string representation of the object
print(NumbersMmrList200Response.to_json())

# convert the object into a dict
numbers_mmr_list200_response_dict = numbers_mmr_list200_response_instance.to_dict()
# create an instance of NumbersMmrList200Response from a dict
numbers_mmr_list200_response_from_dict = NumbersMmrList200Response.from_dict(numbers_mmr_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



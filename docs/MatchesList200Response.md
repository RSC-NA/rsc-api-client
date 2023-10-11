# MatchesList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[MatchList]**](MatchList.md) |  | 

## Example

```python
from openapi_client.models.matches_list200_response import MatchesList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MatchesList200Response from a JSON string
matches_list200_response_instance = MatchesList200Response.from_json(json)
# print the JSON string representation of the object
print MatchesList200Response.to_json()

# convert the object into a dict
matches_list200_response_dict = matches_list200_response_instance.to_dict()
# create an instance of MatchesList200Response from a dict
matches_list200_response_form_dict = matches_list200_response.from_dict(matches_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



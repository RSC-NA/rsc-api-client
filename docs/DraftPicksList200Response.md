# DraftPicksList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DraftPicks]**](DraftPicks.md) |  | 

## Example

```python
from rscapi.models.draft_picks_list200_response import DraftPicksList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPicksList200Response from a JSON string
draft_picks_list200_response_instance = DraftPicksList200Response.from_json(json)
# print the JSON string representation of the object
print(DraftPicksList200Response.to_json())

# convert the object into a dict
draft_picks_list200_response_dict = draft_picks_list200_response_instance.to_dict()
# create an instance of DraftPicksList200Response from a dict
draft_picks_list200_response_form_dict = draft_picks_list200_response.from_dict(draft_picks_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



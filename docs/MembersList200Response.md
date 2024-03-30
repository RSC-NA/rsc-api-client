# MembersList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Member]**](Member.md) |  | 

## Example

```python
from rscapi.models.members_list200_response import MembersList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MembersList200Response from a JSON string
members_list200_response_instance = MembersList200Response.from_json(json)
# print the JSON string representation of the object
print(MembersList200Response.to_json())

# convert the object into a dict
members_list200_response_dict = members_list200_response_instance.to_dict()
# create an instance of MembersList200Response from a dict
members_list200_response_form_dict = members_list200_response.from_dict(members_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



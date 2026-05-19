# PatchedMemberNameChangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**admin_override** | **bool** |  | [optional] [default to False]

## Example

```python
from rscapi.models.patched_member_name_change_request import PatchedMemberNameChangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMemberNameChangeRequest from a JSON string
patched_member_name_change_request_instance = PatchedMemberNameChangeRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedMemberNameChangeRequest.to_json())

# convert the object into a dict
patched_member_name_change_request_dict = patched_member_name_change_request_instance.to_dict()
# create an instance of PatchedMemberNameChangeRequest from a dict
patched_member_name_change_request_from_dict = PatchedMemberNameChangeRequest.from_dict(patched_member_name_change_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



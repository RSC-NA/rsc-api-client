# PatchedMemberUpdate

PUT/PATCH on a member. Only the username: the RSC name and Discord ID have their own routes (name_change keeps the name history, update_discord_id checks uniqueness), and editing them here skipped both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 

## Example

```python
from rscapi.models.patched_member_update import PatchedMemberUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMemberUpdate from a JSON string
patched_member_update_instance = PatchedMemberUpdate.from_json(json)
# print the JSON string representation of the object
print(PatchedMemberUpdate.to_json())

# convert the object into a dict
patched_member_update_dict = patched_member_update_instance.to_dict()
# create an instance of PatchedMemberUpdate from a dict
patched_member_update_from_dict = PatchedMemberUpdate.from_dict(patched_member_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



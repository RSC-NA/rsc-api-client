# MemberUpdate

PUT/PATCH on a member. Only the username: the RSC name and Discord ID have their own routes (name_change keeps the name history, update_discord_id checks uniqueness), and editing them here skipped both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 

## Example

```python
from rscapi.models.member_update import MemberUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MemberUpdate from a JSON string
member_update_instance = MemberUpdate.from_json(json)
# print the JSON string representation of the object
print(MemberUpdate.to_json())

# convert the object into a dict
member_update_dict = member_update_instance.to_dict()
# create an instance of MemberUpdate from a dict
member_update_from_dict = MemberUpdate.from_dict(member_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MemberTransferSchema

Object used to transfer a member to a new discord ID/RSC ID. Used when the player signs up with a new discord ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_account** | **int** | Discord ID of the new member account. This will be the one they have used to sign up with | 

## Example

```python
from rscapi.models.member_transfer_schema import MemberTransferSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MemberTransferSchema from a JSON string
member_transfer_schema_instance = MemberTransferSchema.from_json(json)
# print the JSON string representation of the object
print(MemberTransferSchema.to_json())

# convert the object into a dict
member_transfer_schema_dict = member_transfer_schema_instance.to_dict()
# create an instance of MemberTransferSchema from a dict
member_transfer_schema_from_dict = MemberTransferSchema.from_dict(member_transfer_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MemberTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_account** | **int** | Discord ID for the member account to transfer to or set as the member&#39;s new Discord ID. | 

## Example

```python
from rscapi.models.member_transfer_request import MemberTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemberTransferRequest from a JSON string
member_transfer_request_instance = MemberTransferRequest.from_json(json)
# print the JSON string representation of the object
print(MemberTransferRequest.to_json())

# convert the object into a dict
member_transfer_request_dict = member_transfer_request_instance.to_dict()
# create an instance of MemberTransferRequest from a dict
member_transfer_request_from_dict = MemberTransferRequest.from_dict(member_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



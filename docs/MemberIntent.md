# MemberIntent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**MemberIntentData**](MemberIntentData.md) |  | 
**team** | **str** |  | [optional] [default to '']
**franchise** | **str** |  | [optional] [default to '']

## Example

```python
from rscapi.models.member_intent import MemberIntent

# TODO update the JSON string below
json = "{}"
# create an instance of MemberIntent from a JSON string
member_intent_instance = MemberIntent.from_json(json)
# print the JSON string representation of the object
print(MemberIntent.to_json())

# convert the object into a dict
member_intent_dict = member_intent_instance.to_dict()
# create an instance of MemberIntent from a dict
member_intent_form_dict = member_intent.from_dict(member_intent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



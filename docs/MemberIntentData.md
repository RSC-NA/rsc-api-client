# MemberIntentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rsc_name** | **str** |  | 
**discord_id** | **int** |  | 

## Example

```python
from rscapi.models.member_intent_data import MemberIntentData

# TODO update the JSON string below
json = "{}"
# create an instance of MemberIntentData from a JSON string
member_intent_data_instance = MemberIntentData.from_json(json)
# print the JSON string representation of the object
print(MemberIntentData.to_json())

# convert the object into a dict
member_intent_data_dict = member_intent_data_instance.to_dict()
# create an instance of MemberIntentData from a dict
member_intent_data_from_dict = MemberIntentData.from_dict(member_intent_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



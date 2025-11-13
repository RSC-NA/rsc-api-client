# CreateMemberInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**rsc_name** | **str** |  | 
**discord_id** | **int** |  | 

## Example

```python
from rscapi.models.create_member_input import CreateMemberInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMemberInput from a JSON string
create_member_input_instance = CreateMemberInput.from_json(json)
# print the JSON string representation of the object
print(CreateMemberInput.to_json())

# convert the object into a dict
create_member_input_dict = create_member_input_instance.to_dict()
# create an instance of CreateMemberInput from a dict
create_member_input_from_dict = CreateMemberInput.from_dict(create_member_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



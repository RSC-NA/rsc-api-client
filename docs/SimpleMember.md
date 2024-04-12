# SimpleMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rsc_name** | **str** |  | [optional] 
**rsc_id** | **str** |  | [optional] [readonly] 
**discord_id** | **int** |  | [optional] 

## Example

```python
from rscapi.models.simple_member import SimpleMember

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleMember from a JSON string
simple_member_instance = SimpleMember.from_json(json)
# print the JSON string representation of the object
print(SimpleMember.to_json())

# convert the object into a dict
simple_member_dict = simple_member_instance.to_dict()
# create an instance of SimpleMember from a dict
simple_member_form_dict = simple_member.from_dict(simple_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



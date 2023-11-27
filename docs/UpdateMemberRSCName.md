# UpdateMemberRSCName

Update a players RSC name with a new name.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Players new RSC Name | 

## Example

```python
from rscapi.models.update_member_rsc_name import UpdateMemberRSCName

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMemberRSCName from a JSON string
update_member_rsc_name_instance = UpdateMemberRSCName.from_json(json)
# print the JSON string representation of the object
print UpdateMemberRSCName.to_json()

# convert the object into a dict
update_member_rsc_name_dict = update_member_rsc_name_instance.to_dict()
# create an instance of UpdateMemberRSCName from a dict
update_member_rsc_name_form_dict = update_member_rsc_name.from_dict(update_member_rsc_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



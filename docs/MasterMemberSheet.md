# MasterMemberSheet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rsc_id** | **str** |  | [optional] [readonly] 
**rsc_name** | **str** |  | [optional] [readonly] 
**discord_id** | **int** |  | [optional] [readonly] 
**threes_active** | **bool** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.master_member_sheet import MasterMemberSheet

# TODO update the JSON string below
json = "{}"
# create an instance of MasterMemberSheet from a JSON string
master_member_sheet_instance = MasterMemberSheet.from_json(json)
# print the JSON string representation of the object
print(MasterMemberSheet.to_json())

# convert the object into a dict
master_member_sheet_dict = master_member_sheet_instance.to_dict()
# create an instance of MasterMemberSheet from a dict
master_member_sheet_from_dict = MasterMemberSheet.from_dict(master_member_sheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TwosMasterMemberSheet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rsc_id** | **str** |  | [optional] [readonly] 
**rsc_name** | **str** |  | [optional] [readonly] 
**discord_id** | **int** |  | [optional] [readonly] 
**twos_active** | **bool** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.twos_master_member_sheet import TwosMasterMemberSheet

# TODO update the JSON string below
json = "{}"
# create an instance of TwosMasterMemberSheet from a JSON string
twos_master_member_sheet_instance = TwosMasterMemberSheet.from_json(json)
# print the JSON string representation of the object
print(TwosMasterMemberSheet.to_json())

# convert the object into a dict
twos_master_member_sheet_dict = twos_master_member_sheet_instance.to_dict()
# create an instance of TwosMasterMemberSheet from a dict
twos_master_member_sheet_from_dict = TwosMasterMemberSheet.from_dict(twos_master_member_sheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



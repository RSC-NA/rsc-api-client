# WaiverOrderEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** |  | 
**franchise_id** | **int** |  | 
**franchise_name** | **str** |  | 
**franchise_prefix** | **str** |  | 
**team_id** | **int** |  | 
**team_name** | **str** |  | 
**wins** | **int** |  | 
**losses** | **int** |  | 
**claim_count** | **int** |  | 

## Example

```python
from rscapi.models.waiver_order_entry import WaiverOrderEntry

# TODO update the JSON string below
json = "{}"
# create an instance of WaiverOrderEntry from a JSON string
waiver_order_entry_instance = WaiverOrderEntry.from_json(json)
# print the JSON string representation of the object
print(WaiverOrderEntry.to_json())

# convert the object into a dict
waiver_order_entry_dict = waiver_order_entry_instance.to_dict()
# create an instance of WaiverOrderEntry from a dict
waiver_order_entry_from_dict = WaiverOrderEntry.from_dict(waiver_order_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



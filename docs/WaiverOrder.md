# WaiverOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier_id** | **int** |  | 
**tier_name** | **str** |  | 
**basis** | **str** |  | 
**completed_match_day** | **int** |  | 
**order** | [**List[WaiverOrderEntry]**](WaiverOrderEntry.md) |  | 

## Example

```python
from rscapi.models.waiver_order import WaiverOrder

# TODO update the JSON string below
json = "{}"
# create an instance of WaiverOrder from a JSON string
waiver_order_instance = WaiverOrder.from_json(json)
# print the JSON string representation of the object
print(WaiverOrder.to_json())

# convert the object into a dict
waiver_order_dict = waiver_order_instance.to_dict()
# create an instance of WaiverOrder from a dict
waiver_order_from_dict = WaiverOrder.from_dict(waiver_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



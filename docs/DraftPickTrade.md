# DraftPickTrade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **str** |  | 
**round** | **int** |  | 
**number** | **int** |  | 
**future** | **bool** |  | 
**original_pick** | **str** |  | [optional] 
**future_season** | **int** |  | [optional] 

## Example

```python
from rscapi.models.draft_pick_trade import DraftPickTrade

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPickTrade from a JSON string
draft_pick_trade_instance = DraftPickTrade.from_json(json)
# print the JSON string representation of the object
print(DraftPickTrade.to_json())

# convert the object into a dict
draft_pick_trade_dict = draft_pick_trade_instance.to_dict()
# create an instance of DraftPickTrade from a dict
draft_pick_trade_from_dict = DraftPickTrade.from_dict(draft_pick_trade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



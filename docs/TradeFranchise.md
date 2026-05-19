# TradeFranchise


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**gm** | **int** |  | [optional] 

## Example

```python
from rscapi.models.trade_franchise import TradeFranchise

# TODO update the JSON string below
json = "{}"
# create an instance of TradeFranchise from a JSON string
trade_franchise_instance = TradeFranchise.from_json(json)
# print the JSON string representation of the object
print(TradeFranchise.to_json())

# convert the object into a dict
trade_franchise_dict = trade_franchise_instance.to_dict()
# create an instance of TradeFranchise from a dict
trade_franchise_from_dict = TradeFranchise.from_dict(trade_franchise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



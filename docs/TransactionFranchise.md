# TransactionFranchise


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gm** | [**FranchiseGM**](FranchiseGM.md) |  | 
**name** | **str** |  | 
**id** | **int** |  | [optional] [readonly] 
**prefix** | **str** |  | 

## Example

```python
from rscapi.models.transaction_franchise import TransactionFranchise

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionFranchise from a JSON string
transaction_franchise_instance = TransactionFranchise.from_json(json)
# print the JSON string representation of the object
print(TransactionFranchise.to_json())

# convert the object into a dict
transaction_franchise_dict = transaction_franchise_instance.to_dict()
# create an instance of TransactionFranchise from a dict
transaction_franchise_from_dict = TransactionFranchise.from_dict(transaction_franchise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TransactionTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.transaction_team import TransactionTeam

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTeam from a JSON string
transaction_team_instance = TransactionTeam.from_json(json)
# print the JSON string representation of the object
print TransactionTeam.to_json()

# convert the object into a dict
transaction_team_dict = transaction_team_instance.to_dict()
# create an instance of TransactionTeam from a dict
transaction_team_form_dict = transaction_team.from_dict(transaction_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



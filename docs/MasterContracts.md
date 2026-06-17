# MasterContracts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | 
**rsc_id** | **str** |  | 
**name** | **str** |  | 
**franchise** | **str** |  | [optional] [readonly] 
**contract_length** | **int** |  | 
**current_mmr** | **int** |  | [optional] 
**status** | **str** |  | [optional] [readonly] 
**base_mmr** | **int** |  | [optional] 
**team_name** | **str** |  | [optional] [readonly] 
**waiver_period_end_date** | **datetime** |  | [optional] 

## Example

```python
from rscapi.models.master_contracts import MasterContracts

# TODO update the JSON string below
json = "{}"
# create an instance of MasterContracts from a JSON string
master_contracts_instance = MasterContracts.from_json(json)
# print the JSON string representation of the object
print(MasterContracts.to_json())

# convert the object into a dict
master_contracts_dict = master_contracts_instance.to_dict()
# create an instance of MasterContracts from a dict
master_contracts_from_dict = MasterContracts.from_dict(master_contracts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



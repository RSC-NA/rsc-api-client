# FranchiseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**prefix** | **str** |  | [optional] [readonly] 
**gm** | [**FranchiseGM**](FranchiseGM.md) |  | [optional] 
**league** | **int** |  | [optional] [readonly] 
**tiers** | [**List[FranchiseTier]**](FranchiseTier.md) |  | [optional] [readonly] 
**active** | **bool** |  | [optional] [readonly] 
**teams** | [**List[FranchiseTeam]**](FranchiseTeam.md) |  | [optional] [readonly] 
**logo** | **str** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.franchise_list import FranchiseList

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseList from a JSON string
franchise_list_instance = FranchiseList.from_json(json)
# print the JSON string representation of the object
print FranchiseList.to_json()

# convert the object into a dict
franchise_list_dict = franchise_list_instance.to_dict()
# create an instance of FranchiseList from a dict
franchise_list_form_dict = franchise_list.from_dict(franchise_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



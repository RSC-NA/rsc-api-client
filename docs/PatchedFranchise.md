# PatchedFranchise


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**id** | **int** |  | [optional] [readonly] 
**league** | [**FranchiseLeague**](FranchiseLeague.md) |  | [optional] 
**tiers** | [**List[FranchiseTier]**](FranchiseTier.md) |  | [optional] [readonly] 
**active** | **bool** |  | [optional] [readonly] 
**teams** | [**List[Team]**](Team.md) |  | [optional] [readonly] 
**logo** | **str** |  | [optional] [readonly] 
**gm** | [**FranchiseGM**](FranchiseGM.md) |  | [optional] 
**agms** | [**List[FranchiseGM]**](FranchiseGM.md) |  | [optional] [readonly] 

## Example

```python
from rscapi.models.patched_franchise import PatchedFranchise

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedFranchise from a JSON string
patched_franchise_instance = PatchedFranchise.from_json(json)
# print the JSON string representation of the object
print(PatchedFranchise.to_json())

# convert the object into a dict
patched_franchise_dict = patched_franchise_instance.to_dict()
# create an instance of PatchedFranchise from a dict
patched_franchise_from_dict = PatchedFranchise.from_dict(patched_franchise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



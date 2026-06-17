# Franchise


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**prefix** | **str** |  | 
**id** | **int** |  | [optional] [readonly] 
**league** | [**FranchiseLeague**](FranchiseLeague.md) |  | 
**tiers** | [**List[FranchiseTier]**](FranchiseTier.md) |  | [optional] [readonly] 
**active** | **bool** |  | [optional] [readonly] 
**teams** | [**List[Team]**](Team.md) |  | [optional] [readonly] 
**logo** | **str** |  | [optional] [readonly] 
**gm** | [**FranchiseGM**](FranchiseGM.md) |  | 
**agms** | [**List[FranchiseGM]**](FranchiseGM.md) |  | [optional] [readonly] 

## Example

```python
from rscapi.models.franchise import Franchise

# TODO update the JSON string below
json = "{}"
# create an instance of Franchise from a JSON string
franchise_instance = Franchise.from_json(json)
# print the JSON string representation of the object
print(Franchise.to_json())

# convert the object into a dict
franchise_dict = franchise_instance.to_dict()
# create an instance of Franchise from a dict
franchise_from_dict = Franchise.from_dict(franchise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Franchise


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**prefix** | **str** |  | 
**gm** | [**FranchiseGM**](FranchiseGM.md) |  | [optional] 
**league** | [**League**](League.md) |  | 
**tiers** | **object** |  | [optional] [readonly] 
**active** | **bool** |  | [optional] [readonly] 
**teams** | **object** |  | [optional] [readonly] 
**logo** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.franchise import Franchise

# TODO update the JSON string below
json = "{}"
# create an instance of Franchise from a JSON string
franchise_instance = Franchise.from_json(json)
# print the JSON string representation of the object
print Franchise.to_json()

# convert the object into a dict
franchise_dict = franchise_instance.to_dict()
# create an instance of Franchise from a dict
franchise_form_dict = franchise.from_dict(franchise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



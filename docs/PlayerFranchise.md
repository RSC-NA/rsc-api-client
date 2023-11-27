# PlayerFranchise


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 
**gm** | [**FranchiseGM**](FranchiseGM.md) |  | 

## Example

```python
from rscapi.models.player_franchise import PlayerFranchise

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerFranchise from a JSON string
player_franchise_instance = PlayerFranchise.from_json(json)
# print the JSON string representation of the object
print PlayerFranchise.to_json()

# convert the object into a dict
player_franchise_dict = player_franchise_instance.to_dict()
# create an instance of PlayerFranchise from a dict
player_franchise_form_dict = player_franchise.from_dict(player_franchise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



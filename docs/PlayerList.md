# PlayerList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 

## Example

```python
from rscapi.models.player_list import PlayerList

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerList from a JSON string
player_list_instance = PlayerList.from_json(json)
# print the JSON string representation of the object
print PlayerList.to_json()

# convert the object into a dict
player_list_dict = player_list_instance.to_dict()
# create an instance of PlayerList from a dict
player_list_form_dict = player_list.from_dict(player_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



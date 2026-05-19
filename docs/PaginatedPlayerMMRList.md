# PaginatedPlayerMMRList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PlayerMMR]**](PlayerMMR.md) |  | 

## Example

```python
from rscapi.models.paginated_player_mmr_list import PaginatedPlayerMMRList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPlayerMMRList from a JSON string
paginated_player_mmr_list_instance = PaginatedPlayerMMRList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPlayerMMRList.to_json())

# convert the object into a dict
paginated_player_mmr_list_dict = paginated_player_mmr_list_instance.to_dict()
# create an instance of PaginatedPlayerMMRList from a dict
paginated_player_mmr_list_from_dict = PaginatedPlayerMMRList.from_dict(paginated_player_mmr_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



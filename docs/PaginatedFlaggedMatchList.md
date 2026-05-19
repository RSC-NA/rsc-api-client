# PaginatedFlaggedMatchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FlaggedMatch]**](FlaggedMatch.md) |  | 

## Example

```python
from rscapi.models.paginated_flagged_match_list import PaginatedFlaggedMatchList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFlaggedMatchList from a JSON string
paginated_flagged_match_list_instance = PaginatedFlaggedMatchList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFlaggedMatchList.to_json())

# convert the object into a dict
paginated_flagged_match_list_dict = paginated_flagged_match_list_instance.to_dict()
# create an instance of PaginatedFlaggedMatchList from a dict
paginated_flagged_match_list_from_dict = PaginatedFlaggedMatchList.from_dict(paginated_flagged_match_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



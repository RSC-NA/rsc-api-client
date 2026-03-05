# PaginatedMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | 
**previous** | **str** |  | 
**results** | [**List[Match]**](Match.md) |  | 

## Example

```python
from rscapi.models.paginated_match import PaginatedMatch

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMatch from a JSON string
paginated_match_instance = PaginatedMatch.from_json(json)
# print the JSON string representation of the object
print(PaginatedMatch.to_json())

# convert the object into a dict
paginated_match_dict = paginated_match_instance.to_dict()
# create an instance of PaginatedMatch from a dict
paginated_match_from_dict = PaginatedMatch.from_dict(paginated_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



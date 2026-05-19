# PaginatedTrackerLinkList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[TrackerLink]**](TrackerLink.md) |  | 

## Example

```python
from rscapi.models.paginated_tracker_link_list import PaginatedTrackerLinkList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTrackerLinkList from a JSON string
paginated_tracker_link_list_instance = PaginatedTrackerLinkList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTrackerLinkList.to_json())

# convert the object into a dict
paginated_tracker_link_list_dict = paginated_tracker_link_list_instance.to_dict()
# create an instance of PaginatedTrackerLinkList from a dict
paginated_tracker_link_list_from_dict = PaginatedTrackerLinkList.from_dict(paginated_tracker_link_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



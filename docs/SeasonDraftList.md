# SeasonDraftList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**number** | **int** |  | 

## Example

```python
from rscapi.models.season_draft_list import SeasonDraftList

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonDraftList from a JSON string
season_draft_list_instance = SeasonDraftList.from_json(json)
# print the JSON string representation of the object
print(SeasonDraftList.to_json())

# convert the object into a dict
season_draft_list_dict = season_draft_list_instance.to_dict()
# create an instance of SeasonDraftList from a dict
season_draft_list_from_dict = SeasonDraftList.from_dict(season_draft_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



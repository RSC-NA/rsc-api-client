# SeasonDraftPickList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | [**DraftTierList**](DraftTierList.md) |  | 
**season** | [**SeasonDraftList**](SeasonDraftList.md) |  | 

## Example

```python
from rscapi.models.season_draft_pick_list import SeasonDraftPickList

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonDraftPickList from a JSON string
season_draft_pick_list_instance = SeasonDraftPickList.from_json(json)
# print the JSON string representation of the object
print(SeasonDraftPickList.to_json())

# convert the object into a dict
season_draft_pick_list_dict = season_draft_pick_list_instance.to_dict()
# create an instance of SeasonDraftPickList from a dict
season_draft_pick_list_from_dict = SeasonDraftPickList.from_dict(season_draft_pick_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



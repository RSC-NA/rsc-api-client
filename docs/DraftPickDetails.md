# DraftPickDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**round** | **int** | Specific round in the tier. | [optional] 
**number** | **int** | Pick in the specific tier. | [optional] 
**tier** | [**SeasonDraftPickList**](SeasonDraftPickList.md) |  | 
**franchise** | [**DraftPickFranchise**](DraftPickFranchise.md) |  | 
**future_pick** | **bool** |  | [optional] 
**deleted** | **bool** | Is this pick removed because someone lost a tier. | [optional] 
**pick_from** | **object** |  | [optional] [readonly] 
**original_pick** | **object** |  | [optional] [readonly] 
**future_season** | **int** |  | [optional] 
**players** | [**List[DraftPickLeaguePlayer]**](DraftPickLeaguePlayer.md) |  | 

## Example

```python
from rscapi.models.draft_pick_details import DraftPickDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPickDetails from a JSON string
draft_pick_details_instance = DraftPickDetails.from_json(json)
# print the JSON string representation of the object
print(DraftPickDetails.to_json())

# convert the object into a dict
draft_pick_details_dict = draft_pick_details_instance.to_dict()
# create an instance of DraftPickDetails from a dict
draft_pick_details_from_dict = DraftPickDetails.from_dict(draft_pick_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



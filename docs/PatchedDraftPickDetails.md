# PatchedDraftPickDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**round** | **int** | Specific round in the tier. | [optional] 
**number** | **int** | Pick in the specific tier. | [optional] 
**tier** | [**SeasonDraftPickList**](SeasonDraftPickList.md) |  | [optional] 
**franchise** | [**DraftPickFranchise**](DraftPickFranchise.md) |  | [optional] 
**future_pick** | **bool** |  | [optional] 
**deleted** | **bool** | Is this pick removed because someone lost a tier. | [optional] 
**pick_from** | **Dict[str, object]** |  | [optional] [readonly] 
**original_pick** | **Dict[str, object]** |  | [optional] [readonly] 
**future_season** | **int** |  | [optional] 
**players** | [**List[DraftPickLeaguePlayer]**](DraftPickLeaguePlayer.md) |  | [optional] 

## Example

```python
from rscapi.models.patched_draft_pick_details import PatchedDraftPickDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDraftPickDetails from a JSON string
patched_draft_pick_details_instance = PatchedDraftPickDetails.from_json(json)
# print the JSON string representation of the object
print(PatchedDraftPickDetails.to_json())

# convert the object into a dict
patched_draft_pick_details_dict = patched_draft_pick_details_instance.to_dict()
# create an instance of PatchedDraftPickDetails from a dict
patched_draft_pick_details_from_dict = PatchedDraftPickDetails.from_dict(patched_draft_pick_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



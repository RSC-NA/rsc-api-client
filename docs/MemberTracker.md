# MemberTracker


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | **str** |  | 
**rscid** | **str** |  | 
**discord_id** | **int** |  | [optional] [readonly] 
**accounts** | [**List[TrackerLink]**](TrackerLink.md) |  | 

## Example

```python
from rscapi.models.member_tracker import MemberTracker

# TODO update the JSON string below
json = "{}"
# create an instance of MemberTracker from a JSON string
member_tracker_instance = MemberTracker.from_json(json)
# print the JSON string representation of the object
print MemberTracker.to_json()

# convert the object into a dict
member_tracker_dict = member_tracker_instance.to_dict()
# create an instance of MemberTracker from a dict
member_tracker_form_dict = member_tracker.from_dict(member_tracker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



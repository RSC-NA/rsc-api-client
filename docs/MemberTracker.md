# MemberTracker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | **str** |  | [optional] [readonly] 
**rsc_name** | **str** |  | 
**rscid** | **str** |  | [optional] [readonly] 
**discord_id** | **int** |  | [optional] [readonly] 
**accounts** | [**List[TrackerLink]**](TrackerLink.md) |  | [optional] [readonly] 

## Example

```python
from rscapi.models.member_tracker import MemberTracker

# TODO update the JSON string below
json = "{}"
# create an instance of MemberTracker from a JSON string
member_tracker_instance = MemberTracker.from_json(json)
# print the JSON string representation of the object
print(MemberTracker.to_json())

# convert the object into a dict
member_tracker_dict = member_tracker_instance.to_dict()
# create an instance of MemberTracker from a dict
member_tracker_from_dict = MemberTracker.from_dict(member_tracker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



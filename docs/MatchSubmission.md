# MatchSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_team** | **int** |  | 
**away_team** | **int** |  | 
**day** | **int** |  | [optional] 
**match_format** | **str** |  | 
**match_type** | **str** |  | 

## Example

```python
from rscapi.models.match_submission import MatchSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of MatchSubmission from a JSON string
match_submission_instance = MatchSubmission.from_json(json)
# print the JSON string representation of the object
print(MatchSubmission.to_json())

# convert the object into a dict
match_submission_dict = match_submission_instance.to_dict()
# create an instance of MatchSubmission from a dict
match_submission_from_dict = MatchSubmission.from_dict(match_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



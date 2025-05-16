# MatchScoreReport

Data to score report a match.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_score** | **int** | Number of games Home won. | [optional] 
**away_score** | **int** | Number of games Away won. | [optional] 
**executor** | **int** | Person executing the score report | [optional] 
**override** | **bool** | Is an admin overriding the score report. | [optional] 
**ballchasing_group** | **str** | ID of the ballchasing group of match results. | [optional] 

## Example

```python
from rscapi.models.match_score_report import MatchScoreReport

# TODO update the JSON string below
json = "{}"
# create an instance of MatchScoreReport from a JSON string
match_score_report_instance = MatchScoreReport.from_json(json)
# print the JSON string representation of the object
print(MatchScoreReport.to_json())

# convert the object into a dict
match_score_report_dict = match_score_report_instance.to_dict()
# create an instance of MatchScoreReport from a dict
match_score_report_from_dict = MatchScoreReport.from_dict(match_score_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MatchScoreReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_score** | **int** | Number of games Home won. | 
**away_score** | **int** | Number of games Away won. | 
**executor** | **int** | Person executing the score report | 
**ballchasing_group** | **str** | ID of the ballchasing group of match results. | 
**override** | **bool** | Is an admin overriding the score report. | [optional] [default to False]

## Example

```python
from rscapi.models.match_score_report_request import MatchScoreReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchScoreReportRequest from a JSON string
match_score_report_request_instance = MatchScoreReportRequest.from_json(json)
# print the JSON string representation of the object
print(MatchScoreReportRequest.to_json())

# convert the object into a dict
match_score_report_request_dict = match_score_report_request_instance.to_dict()
# create an instance of MatchScoreReportRequest from a dict
match_score_report_request_from_dict = MatchScoreReportRequest.from_dict(match_score_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



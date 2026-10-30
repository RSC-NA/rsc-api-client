# PendingSeries

A team's next playoff series before it has a match: its opponent is the winner of a feeder series not yet reported. No lobby yet; the match, with one, exists once it is.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **str** |  | 
**round** | **int** | Playoff round: 1 Wild Card, 2 Quarterfinals, 3 Semifinals, 4 Finals | 
**round_label** | **str** |  | 
**match_format** | [**MatchFormatEnum**](MatchFormatEnum.md) |  | 
**num_games** | **int** |  | 
**var_date** | **datetime** |  | 
**home** | **bool** | True or False when the team is home or away whoever wins the feeder; null when that depends. | 
**team** | [**BaseTeam**](BaseTeam.md) |  | 
**possible_opponents** | [**List[BaseTeam]**](BaseTeam.md) |  | 
**feeder_match** | [**PendingSeriesFeeder**](PendingSeriesFeeder.md) |  | 

## Example

```python
from rscapi.models.pending_series import PendingSeries

# TODO update the JSON string below
json = "{}"
# create an instance of PendingSeries from a JSON string
pending_series_instance = PendingSeries.from_json(json)
# print the JSON string representation of the object
print(PendingSeries.to_json())

# convert the object into a dict
pending_series_dict = pending_series_instance.to_dict()
# create an instance of PendingSeries from a dict
pending_series_from_dict = PendingSeries.from_dict(pending_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



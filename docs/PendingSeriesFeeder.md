# PendingSeriesFeeder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**day** | **int** |  | [optional] [readonly] 
**var_date** | **datetime** |  | [optional] [readonly] 
**match_format** | [**MatchFormatEnum**](MatchFormatEnum.md) |  | [optional] [readonly] 
**home_team** | [**BaseTeam**](BaseTeam.md) |  | 
**away_team** | [**BaseTeam**](BaseTeam.md) |  | 

## Example

```python
from rscapi.models.pending_series_feeder import PendingSeriesFeeder

# TODO update the JSON string below
json = "{}"
# create an instance of PendingSeriesFeeder from a JSON string
pending_series_feeder_instance = PendingSeriesFeeder.from_json(json)
# print the JSON string representation of the object
print(PendingSeriesFeeder.to_json())

# convert the object into a dict
pending_series_feeder_dict = pending_series_feeder_instance.to_dict()
# create an instance of PendingSeriesFeeder from a dict
pending_series_feeder_from_dict = PendingSeriesFeeder.from_dict(pending_series_feeder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# LeagueFutureSeasonCreate

Request body for creating a future season.  Dates are real ``DateTimeField``s rather than the strings ``LeagueSeasonStartSerializer`` parses by hand, so an unparsable date is a field error instead of a 500.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Must be in the future. | 
**end_date** | **datetime** | Must be later than the current season&#39;s end_date. | 
**draft_date** | **datetime** | Must be in the future. | 
**preseason_start_date** | **datetime** |  | [optional] 
**regular_season_start** | **datetime** |  | [optional] 
**regular_season_end** | **datetime** |  | [optional] 
**signup_close** | **datetime** |  | [optional] 
**signups_open** | **datetime** |  | [optional] 
**season_number** | **int** | Defaults to the current season&#39;s number + 1. | [optional] 
**num_rounds** | **int** | Draft rounds per tier. | [optional] [default to 6]
**tier_overrides** | [**List[FutureSeasonTierOverride]**](FutureSeasonTierOverride.md) |  | [optional] 
**allow_promotion** | **bool** | Proceed even when the current season has already ended and this season would be promoted to current immediately. | [optional] [default to False]
**dry_run** | **bool** | Report what would be created without writing anything. | [optional] [default to False]

## Example

```python
from rscapi.models.league_future_season_create import LeagueFutureSeasonCreate

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueFutureSeasonCreate from a JSON string
league_future_season_create_instance = LeagueFutureSeasonCreate.from_json(json)
# print the JSON string representation of the object
print(LeagueFutureSeasonCreate.to_json())

# convert the object into a dict
league_future_season_create_dict = league_future_season_create_instance.to_dict()
# create an instance of LeagueFutureSeasonCreate from a dict
league_future_season_create_from_dict = LeagueFutureSeasonCreate.from_dict(league_future_season_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



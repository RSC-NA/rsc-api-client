# PlayerSeasonStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**player** | **str** |  | 
**season** | **int** |  | 
**type** | **str** |  | 
**shooting_percentage** | **float** |  | 
**bpm** | **float** |  | 
**bcpm** | **float** |  | 
**avg_amount** | **float** |  | 
**percent_zero_boost** | **float** |  | 
**percent_full_boost** | **float** |  | 
**percent_boost_0_25** | **float** |  | 
**percent_boost_25_50** | **float** |  | 
**percent_boost_50_75** | **float** |  | 
**percent_boost_75_100** | **float** |  | 
**avg_speed** | **int** |  | 
**avg_powerslide_duration** | **float** |  | 
**avg_speed_percentage** | **float** |  | 
**percent_slow_speed** | **float** |  | 
**percent_boost_speed** | **float** |  | 
**percent_supersonic_speed** | **float** |  | 
**percent_ground** | **float** |  | 
**percent_low_air** | **float** |  | 
**percent_high_air** | **float** |  | 
**avg_distance_to_ball** | **int** |  | 
**avg_distance_to_ball_possession** | **int** |  | 
**avg_distance_to_ball_no_possession** | **int** |  | 
**avg_distance_to_mates** | **int** |  | 
**percent_defensive_third** | **float** |  | 
**percent_offensive_third** | **float** |  | 
**percent_neutral_third** | **float** |  | 
**percent_defensive_half** | **float** |  | 
**percent_offensive_half** | **float** |  | 
**percent_behind_ball** | **float** |  | 
**percent_infront_ball** | **float** |  | 
**percent_most_back** | **float** |  | 
**percent_most_forward** | **float** |  | 
**percent_closest_to_ball** | **float** |  | 
**percent_farthest_from_ball** | **float** |  | 
**stats_type** | **str** |  | [optional] 
**total_shots** | **int** |  | [optional] 
**games_played** | **int** |  | [optional] 
**games_won** | **int** |  | [optional] 
**games_lost** | **int** |  | [optional] 
**mvps** | **int** |  | [optional] 
**shots** | **int** |  | [optional] 
**shots_against** | **int** |  | [optional] 
**goals** | **int** |  | [optional] 
**goals_against** | **int** |  | [optional] 
**saves** | **int** |  | [optional] 
**assists** | **int** |  | [optional] 
**points** | **int** |  | [optional] 
**hat_tricks** | **int** |  | [optional] 
**playmakers** | **int** |  | [optional] 
**saviors** | **int** |  | [optional] 
**goals_against_while_last_defender** | **int** |  | [optional] 
**time_powerslide** | **float** |  | [optional] 
**count_powerslide** | **int** |  | [optional] 
**amount_collected** | **int** |  | [optional] 
**amount_stolen** | **int** |  | [optional] 
**amount_collected_big** | **int** |  | [optional] 
**amount_stolen_big** | **int** |  | [optional] 
**amount_collected_small** | **int** |  | [optional] 
**amount_stolen_small** | **int** |  | [optional] 
**count_collected_big** | **int** |  | [optional] 
**count_stolen_big** | **int** |  | [optional] 
**count_collected_small** | **int** |  | [optional] 
**count_stolen_small** | **int** |  | [optional] 
**amount_overfill** | **int** |  | [optional] 
**amount_overfill_stolen** | **int** |  | [optional] 
**amount_used_while_supersonic** | **int** |  | [optional] 
**time_zero_boost** | **float** |  | [optional] 
**time_full_boost** | **float** |  | [optional] 
**time_boost_0_25** | **float** |  | [optional] 
**time_boost_25_50** | **float** |  | [optional] 
**time_boost_50_75** | **float** |  | [optional] 
**time_boost_75_100** | **float** |  | [optional] 
**total_distance** | **int** |  | [optional] 
**time_supersonic_speed** | **float** |  | [optional] 
**time_boost_speed** | **float** |  | [optional] 
**time_slow_speed** | **float** |  | [optional] 
**time_ground** | **float** |  | [optional] 
**time_low_air** | **float** |  | [optional] 
**time_high_air** | **float** |  | [optional] 
**time_defensive_third** | **float** |  | [optional] 
**time_neutral_third** | **float** |  | [optional] 
**time_offensive_third** | **float** |  | [optional] 
**time_defensive_half** | **float** |  | [optional] 
**time_offensive_half** | **float** |  | [optional] 
**time_behind_ball** | **float** |  | [optional] 
**time_infront_ball** | **float** |  | [optional] 
**time_most_back** | **float** |  | [optional] 
**time_most_forward** | **float** |  | [optional] 
**time_closest_to_ball** | **float** |  | [optional] 
**time_farthest_from_ball** | **float** |  | [optional] 
**demos_inflicted** | **int** |  | [optional] 
**demos_taken** | **int** |  | [optional] 
**raw_boost_time** | **float** |  | [optional] 
**raw_bpm** | **float** |  | [optional] 
**raw_bcpm** | **float** |  | [optional] 
**raw_avg_amount** | **float** |  | [optional] 
**raw_movement_time** | **float** |  | [optional] 
**raw_avg_speed** | **int** |  | [optional] 
**raw_avg_speed_percentage** | **float** |  | [optional] 
**raw_positioning_time** | **float** |  | [optional] 
**raw_avg_distance_to_ball** | **int** |  | [optional] 
**raw_avg_distance_to_ball_possession** | **int** |  | [optional] 
**raw_avg_distance_to_ball_no_possession** | **int** |  | [optional] 
**raw_avg_distance_to_mates** | **int** |  | [optional] 
**tier** | **int** |  | 

## Example

```python
from rscapi.models.player_season_stats import PlayerSeasonStats

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSeasonStats from a JSON string
player_season_stats_instance = PlayerSeasonStats.from_json(json)
# print the JSON string representation of the object
print(PlayerSeasonStats.to_json())

# convert the object into a dict
player_season_stats_dict = player_season_stats_instance.to_dict()
# create an instance of PlayerSeasonStats from a dict
player_season_stats_from_dict = PlayerSeasonStats.from_dict(player_season_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



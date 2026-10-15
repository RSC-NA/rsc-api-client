# PlayoffTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** |  | 
**team_name** | **str** |  | 
**franchise_id** | **int** |  | 
**franchise_name** | **str** |  | 
**franchise_prefix** | **str** |  | 
**franchise_logo_url** | **str** |  | 
**conference** | **str** |  | 
**conference_label** | **str** |  | 
**division** | **str** |  | 
**division_label** | **str** |  | 
**overall_rank** | **int** |  | 
**overall_games_back** | **float** |  | 
**playoff_rank** | **int** | Position in the playoff group&#39;s standings. | 
**playoff_seed** | **int** | Seed among the group&#39;s qualifiers by record (rule 2.5.5); null when outside. | 
**playoff_group_label** | **str** |  | 
**playoff_cutoff** | **int** |  | 
**playoff_qualified** | **bool** |  | 
**playoff_qualifier_reason** | [**PlayoffQualifierReasonEnum**](PlayoffQualifierReasonEnum.md) | How the team qualifies: top of the group, its division, or a wildcard; null when outside.  * &#x60;cut&#x60; - cut * &#x60;division&#x60; - division * &#x60;wildcard&#x60; - wildcard | 
**tiebreak_draw** | [**TiebreakDrawEnum**](TiebreakDrawEnum.md) | Set when the random draw (rule 2.4.2.9) decided this team&#39;s spot or seed; otherwise null.  * &#x60;provisional&#x60; - provisional * &#x60;drawn&#x60; - drawn | 
**playoff_status_label** | **str** |  | 
**playoff_delta_label** | **str** |  | 
**playoff_magic_number** | **int** |  | 
**playoff_magic_number_label** | **str** |  | 
**remaining_games** | **int** |  | 
**max_possible_games_won** | **int** |  | 
**group_games_back** | **float** |  | 
**group_games_won** | **int** |  | 
**group_games_lost** | **int** |  | 
**group_win_pct** | **float** |  | 
**games_played** | **int** |  | 
**games_won** | **int** |  | 
**games_lost** | **int** |  | 
**win_pct** | **float** |  | 
**goals** | **int** |  | 
**opponent_goals** | **int** |  | 
**goal_differential** | **int** |  | 
**shots** | **int** |  | 
**shot_pct** | **float** |  | 

## Example

```python
from rscapi.models.playoff_team import PlayoffTeam

# TODO update the JSON string below
json = "{}"
# create an instance of PlayoffTeam from a JSON string
playoff_team_instance = PlayoffTeam.from_json(json)
# print the JSON string representation of the object
print(PlayoffTeam.to_json())

# convert the object into a dict
playoff_team_dict = playoff_team_instance.to_dict()
# create an instance of PlayoffTeam from a dict
playoff_team_from_dict = PlayoffTeam.from_dict(playoff_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



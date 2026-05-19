# TierLeagueAdd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **int** |  | 
**role_id** | **int** |  | [optional] 

## Example

```python
from rscapi.models.tier_league_add import TierLeagueAdd

# TODO update the JSON string below
json = "{}"
# create an instance of TierLeagueAdd from a JSON string
tier_league_add_instance = TierLeagueAdd.from_json(json)
# print the JSON string representation of the object
print(TierLeagueAdd.to_json())

# convert the object into a dict
tier_league_add_dict = tier_league_add_instance.to_dict()
# create an instance of TierLeagueAdd from a dict
tier_league_add_from_dict = TierLeagueAdd.from_dict(tier_league_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



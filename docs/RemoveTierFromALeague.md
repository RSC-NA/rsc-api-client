# RemoveTierFromALeague

Remove an existing tier from a league

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **int** | Tier to add to the league | 

## Example

```python
from rscapi.models.remove_tier_from_a_league import RemoveTierFromALeague

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveTierFromALeague from a JSON string
remove_tier_from_a_league_instance = RemoveTierFromALeague.from_json(json)
# print the JSON string representation of the object
print RemoveTierFromALeague.to_json()

# convert the object into a dict
remove_tier_from_a_league_dict = remove_tier_from_a_league_instance.to_dict()
# create an instance of RemoveTierFromALeague from a dict
remove_tier_from_a_league_form_dict = remove_tier_from_a_league.from_dict(remove_tier_from_a_league_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AddTierToLeague

Add an existing tier to a league

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **int** | Tier to add to the league | 
**role_id** | **int** | ID of the role in the server. | [optional] 

## Example

```python
from rscapi.models.add_tier_to_league import AddTierToLeague

# TODO update the JSON string below
json = "{}"
# create an instance of AddTierToLeague from a JSON string
add_tier_to_league_instance = AddTierToLeague.from_json(json)
# print the JSON string representation of the object
print AddTierToLeague.to_json()

# convert the object into a dict
add_tier_to_league_dict = add_tier_to_league_instance.to_dict()
# create an instance of AddTierToLeague from a dict
add_tier_to_league_form_dict = add_tier_to_league.from_dict(add_tier_to_league_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



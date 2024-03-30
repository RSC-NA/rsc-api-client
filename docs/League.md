# League


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**guild_id** | **int** |  | 
**league_data** | [**LeagueData**](LeagueData.md) |  | 
**tiers** | [**List[Tier]**](Tier.md) |  | 

## Example

```python
from rscapi.models.league import League

# TODO update the JSON string below
json = "{}"
# create an instance of League from a JSON string
league_instance = League.from_json(json)
# print the JSON string representation of the object
print(League.to_json())

# convert the object into a dict
league_dict = league_instance.to_dict()
# create an instance of League from a dict
league_form_dict = league.from_dict(league_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



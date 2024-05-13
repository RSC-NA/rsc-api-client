# MatchGM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rsc_name** | **str** |  | [optional] 
**discord_id** | **int** |  | [optional] 

## Example

```python
from rscapi.models.match_gm import MatchGM

# TODO update the JSON string below
json = "{}"
# create an instance of MatchGM from a JSON string
match_gm_instance = MatchGM.from_json(json)
# print the JSON string representation of the object
print(MatchGM.to_json())

# convert the object into a dict
match_gm_dict = match_gm_instance.to_dict()
# create an instance of MatchGM from a dict
match_gm_form_dict = match_gm.from_dict(match_gm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



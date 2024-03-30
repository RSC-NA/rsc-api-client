# BaseTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 

## Example

```python
from rscapi.models.base_team import BaseTeam

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTeam from a JSON string
base_team_instance = BaseTeam.from_json(json)
# print the JSON string representation of the object
print(BaseTeam.to_json())

# convert the object into a dict
base_team_dict = base_team_instance.to_dict()
# create an instance of BaseTeam from a dict
base_team_form_dict = base_team.from_dict(base_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



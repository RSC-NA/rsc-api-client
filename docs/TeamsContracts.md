# TeamsContracts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**franchise** | **str** |  | 
**tier** | **str** |  | 

## Example

```python
from rscapi.models.teams_contracts import TeamsContracts

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsContracts from a JSON string
teams_contracts_instance = TeamsContracts.from_json(json)
# print the JSON string representation of the object
print(TeamsContracts.to_json())

# convert the object into a dict
teams_contracts_dict = teams_contracts_instance.to_dict()
# create an instance of TeamsContracts from a dict
teams_contracts_from_dict = TeamsContracts.from_dict(teams_contracts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



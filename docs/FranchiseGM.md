# FranchiseGM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rsc_name** | **str** |  | [optional] [readonly] 
**discord_id** | **int** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.franchise_gm import FranchiseGM

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseGM from a JSON string
franchise_gm_instance = FranchiseGM.from_json(json)
# print the JSON string representation of the object
print(FranchiseGM.to_json())

# convert the object into a dict
franchise_gm_dict = franchise_gm_instance.to_dict()
# create an instance of FranchiseGM from a dict
franchise_gm_form_dict = franchise_gm.from_dict(franchise_gm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



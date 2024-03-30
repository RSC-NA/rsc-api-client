# RebrandAFranchise

Rebrand a franchise to new details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name you would like to give the rebranded franchise. | 
**prefix** | **str** | New prefix of the franchise | 
**teams** | [**List[TeamDetails]**](TeamDetails.md) | List of team names and their tier. | 
**admin_override** | **bool** | Override any checks and approve the rebrand. | [optional] 

## Example

```python
from rscapi.models.rebrand_a_franchise import RebrandAFranchise

# TODO update the JSON string below
json = "{}"
# create an instance of RebrandAFranchise from a JSON string
rebrand_a_franchise_instance = RebrandAFranchise.from_json(json)
# print the JSON string representation of the object
print(RebrandAFranchise.to_json())

# convert the object into a dict
rebrand_a_franchise_dict = rebrand_a_franchise_instance.to_dict()
# create an instance of RebrandAFranchise from a dict
rebrand_a_franchise_form_dict = rebrand_a_franchise.from_dict(rebrand_a_franchise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



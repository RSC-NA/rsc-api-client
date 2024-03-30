# FranchiseIdentifier

Identifier for the franchise in question. (Provide at least 1)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gm** | **int** | Discord ID of current GM of the franchise | [optional] 
**name** | **str** | Name of the franchise (exact name required). | [optional] 
**id** | **int** | ID of the franchise. | [optional] 

## Example

```python
from rscapi.models.franchise_identifier import FranchiseIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseIdentifier from a JSON string
franchise_identifier_instance = FranchiseIdentifier.from_json(json)
# print the JSON string representation of the object
print(FranchiseIdentifier.to_json())

# convert the object into a dict
franchise_identifier_dict = franchise_identifier_instance.to_dict()
# create an instance of FranchiseIdentifier from a dict
franchise_identifier_form_dict = franchise_identifier.from_dict(franchise_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



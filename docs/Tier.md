# Tier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **int** |  | [optional] [readonly] 
**color** | **int** |  | [optional] [readonly] 
**position** | **int** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.tier import Tier

# TODO update the JSON string below
json = "{}"
# create an instance of Tier from a JSON string
tier_instance = Tier.from_json(json)
# print the JSON string representation of the object
print(Tier.to_json())

# convert the object into a dict
tier_dict = tier_instance.to_dict()
# create an instance of Tier from a dict
tier_from_dict = Tier.from_dict(tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



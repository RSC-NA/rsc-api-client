# Tier

Read and write serializer for :class:`Tier`.  ``position`` and ``color`` used to be in ``read_only_fields``, which made the endpoint impossible to use: ``Tier.position`` is NOT NULL with no model default, so DRF stripped it from ``validated_data`` and every create died with an IntegrityError 500 rather than a 400. Both are writable now.  The validators below stand in for database constraints the table does not have. ``Tier`` rows are global -- they are shared between leagues through ``LeagueTiers`` -- so ``name`` and ``position`` have to be unique across the whole table, not per league.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**color** | **int** |  | [optional] 
**position** | **int** |  | 
**league** | **int** |  | [optional] 
**role_id** | **int** |  | [optional] 

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



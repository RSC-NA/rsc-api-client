# PatchedTier

Read and write serializer for :class:`Tier`.  ``position`` and ``color`` used to be in ``read_only_fields``, which made the endpoint impossible to use: ``Tier.position`` is NOT NULL with no model default, so DRF stripped it from ``validated_data`` and every create died with an IntegrityError 500 rather than a 400. Both are writable now.  The validators below stand in for database constraints the table does not have. ``Tier`` rows are global -- they are shared between leagues through ``LeagueTiers`` -- so ``name`` and ``position`` have to be unique across the whole table, not per league.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**color** | **int** |  | [optional] 
**position** | **int** |  | [optional] 
**league** | **int** |  | [optional] 
**role_id** | **int** |  | [optional] 

## Example

```python
from rscapi.models.patched_tier import PatchedTier

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTier from a JSON string
patched_tier_instance = PatchedTier.from_json(json)
# print the JSON string representation of the object
print(PatchedTier.to_json())

# convert the object into a dict
patched_tier_dict = patched_tier_instance.to_dict()
# create an instance of PatchedTier from a dict
patched_tier_from_dict = PatchedTier.from_dict(patched_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



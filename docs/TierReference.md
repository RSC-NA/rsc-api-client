# TierReference

A tier identified by name, for endpoints that look one up rather than define one.  ``TeamCreateSerializer`` nests this to say which tier a new team belongs to. It used to nest ``TierSerializer``, which was harmless only because every field but ``name`` was read-only there. Now that ``TierSerializer`` validates a tier definition -- ``position`` required, name and position rejected if already taken -- reusing it would demand a position for a lookup and reject every tier that actually exists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from rscapi.models.tier_reference import TierReference

# TODO update the JSON string below
json = "{}"
# create an instance of TierReference from a JSON string
tier_reference_instance = TierReference.from_json(json)
# print the JSON string representation of the object
print(TierReference.to_json())

# convert the object into a dict
tier_reference_dict = tier_reference_instance.to_dict()
# create an instance of TierReference from a dict
tier_reference_from_dict = TierReference.from_dict(tier_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



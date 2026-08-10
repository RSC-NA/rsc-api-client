# ElevatedRoleUpdate

Write body for PUT/PATCH on /members/{member_id}/elevated_roles/{id}/.  Deliberately not a subclass of ElevatedRoleInputSerializer: `league` is immutable on an existing grant. Moving a grant between leagues is a different grant, and since the executor check is scoped to a league, a mutable `league` would let an admin of league A push a row into league B while only ever being checked against A.  Every mutable field carries an explicit `default`. `Field.validate_empty_values` falls back to `get_default()` for an absent value, and `get_default()` raises SkipField when the default is `empty` -- so `required=False` alone would silently persist the stored value on a PUT, giving a full-replace that only half replaces. Under `partial=True` the default is never consulted, so PATCH is unaffected.  Must be constructed with the instance: `validate()` runs against the merged row, not the payload, so its rules hold under PATCH too.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | [**PositionEnum**](PositionEnum.md) |  | [optional] 
**executor** | **int** |  | 

## Example

```python
from rscapi.models.elevated_role_update import ElevatedRoleUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ElevatedRoleUpdate from a JSON string
elevated_role_update_instance = ElevatedRoleUpdate.from_json(json)
# print the JSON string representation of the object
print(ElevatedRoleUpdate.to_json())

# convert the object into a dict
elevated_role_update_dict = elevated_role_update_instance.to_dict()
# create an instance of ElevatedRoleUpdate from a dict
elevated_role_update_from_dict = ElevatedRoleUpdate.from_dict(elevated_role_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



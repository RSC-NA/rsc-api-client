# InactiveReserve

Place a player on IR

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | **int** | Specific player to perform transaction on. | 
**league** | **int** | ID of the league transaction is for. | 
**executor** | **int** | Discord ID of specific member who ran the transaction. | 
**notes** | **str** | Notes for the transaction from the TM running it. | [optional] 
**admin_override** | **bool** | Boolean indicating whether or not an admin is overriding this command. | [optional] 
**remove_from_ir** | **bool** | Boolean indicating whether or not the player is returning from IR. | [optional] 

## Example

```python
from rscapi.models.inactive_reserve import InactiveReserve

# TODO update the JSON string below
json = "{}"
# create an instance of InactiveReserve from a JSON string
inactive_reserve_instance = InactiveReserve.from_json(json)
# print the JSON string representation of the object
print InactiveReserve.to_json()

# convert the object into a dict
inactive_reserve_dict = inactive_reserve_instance.to_dict()
# create an instance of InactiveReserve from a dict
inactive_reserve_form_dict = inactive_reserve.from_dict(inactive_reserve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



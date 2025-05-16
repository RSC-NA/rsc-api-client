# TemporaryFASub

Temporarily sub a free agent to a team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player_in** | **int** | Specific player to perform transaction on. | 
**player_out** | **int** | Specific player to perform transaction on. | 
**league** | **int** | ID of the league transaction is for. | 
**executor** | **int** | Discord ID of specific member who ran the transaction. | 
**notes** | **str** | Notes for the transaction from the TM running it. | [optional] 
**admin_override** | **bool** | Boolean indicating whether or not an admin is overriding this command. | [optional] 

## Example

```python
from rscapi.models.temporary_fa_sub import TemporaryFASub

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryFASub from a JSON string
temporary_fa_sub_instance = TemporaryFASub.from_json(json)
# print the JSON string representation of the object
print(TemporaryFASub.to_json())

# convert the object into a dict
temporary_fa_sub_dict = temporary_fa_sub_instance.to_dict()
# create an instance of TemporaryFASub from a dict
temporary_fa_sub_from_dict = TemporaryFASub.from_dict(temporary_fa_sub_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CutAPlayerAndSignAnother

Cuts a player from a team and signs another.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cut_player** | **int** | Specific player to perform transaction on. | 
**sign_player** | **int** | Specific player to perform transaction on. | 
**league** | **int** | ID of the league transaction is for. | 
**executor** | **int** | Discord ID of specific member who ran the transaction. | 
**admin_override** | **bool** | Boolean indicating whether or not an admin is overriding this command. | [optional] 
**notes** | **str** | Notes for the transaction from the TM running it. | [optional] 

## Example

```python
from rscapi.models.cut_a_player_and_sign_another import CutAPlayerAndSignAnother

# TODO update the JSON string below
json = "{}"
# create an instance of CutAPlayerAndSignAnother from a JSON string
cut_a_player_and_sign_another_instance = CutAPlayerAndSignAnother.from_json(json)
# print the JSON string representation of the object
print CutAPlayerAndSignAnother.to_json()

# convert the object into a dict
cut_a_player_and_sign_another_dict = cut_a_player_and_sign_another_instance.to_dict()
# create an instance of CutAPlayerAndSignAnother from a dict
cut_a_player_and_sign_another_form_dict = cut_a_player_and_sign_another.from_dict(cut_a_player_and_sign_another_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



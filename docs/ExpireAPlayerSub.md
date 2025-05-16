# ExpireAPlayerSub

Expire a sub for a player who's subbing in on a team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** | ID of the league transaction is for. | [optional] 
**player** | **int** | Specific player to perform transaction on. | [optional] 
**executor** | **int** | Discord ID of specific member who ran the transaction. | [optional] 

## Example

```python
from rscapi.models.expire_a_player_sub import ExpireAPlayerSub

# TODO update the JSON string below
json = "{}"
# create an instance of ExpireAPlayerSub from a JSON string
expire_a_player_sub_instance = ExpireAPlayerSub.from_json(json)
# print the JSON string representation of the object
print(ExpireAPlayerSub.to_json())

# convert the object into a dict
expire_a_player_sub_dict = expire_a_player_sub_instance.to_dict()
# create an instance of ExpireAPlayerSub from a dict
expire_a_player_sub_from_dict = ExpireAPlayerSub.from_dict(expire_a_player_sub_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



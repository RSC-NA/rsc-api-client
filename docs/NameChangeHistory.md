# NameChangeHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_name** | **str** |  | 
**date_changed** | **datetime** |  | [optional] 

## Example

```python
from rscapi.models.name_change_history import NameChangeHistory

# TODO update the JSON string below
json = "{}"
# create an instance of NameChangeHistory from a JSON string
name_change_history_instance = NameChangeHistory.from_json(json)
# print the JSON string representation of the object
print(NameChangeHistory.to_json())

# convert the object into a dict
name_change_history_dict = name_change_history_instance.to_dict()
# create an instance of NameChangeHistory from a dict
name_change_history_from_dict = NameChangeHistory.from_dict(name_change_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



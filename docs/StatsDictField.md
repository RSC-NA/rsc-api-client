# StatsDictField


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blue** | [**TeamGameListResultsField**](TeamGameListResultsField.md) |  | 
**orange** | [**TeamGameListResultsField**](TeamGameListResultsField.md) |  | 

## Example

```python
from rscapi.models.stats_dict_field import StatsDictField

# TODO update the JSON string below
json = "{}"
# create an instance of StatsDictField from a JSON string
stats_dict_field_instance = StatsDictField.from_json(json)
# print the JSON string representation of the object
print StatsDictField.to_json()

# convert the object into a dict
stats_dict_field_dict = stats_dict_field_instance.to_dict()
# create an instance of StatsDictField from a dict
stats_dict_field_form_dict = stats_dict_field.from_dict(stats_dict_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ActivityCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**missing** | **bool** |  | [optional] 
**completed** | **bool** |  | [optional] 
**season** | **int** |  | 
**member** | **str** |  | 
**rsc_id** | **str** |  | 
**discord_id** | **int** |  | 
**returning_status** | **bool** |  | [optional] 

## Example

```python
from rscapi.models.activity_check import ActivityCheck

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCheck from a JSON string
activity_check_instance = ActivityCheck.from_json(json)
# print the JSON string representation of the object
print(ActivityCheck.to_json())

# convert the object into a dict
activity_check_dict = activity_check_instance.to_dict()
# create an instance of ActivityCheck from a dict
activity_check_from_dict = ActivityCheck.from_dict(activity_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



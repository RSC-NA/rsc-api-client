# ActivityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_override** | **bool** |  | 
**executor** | **int** |  | 
**league** | **int** |  | 
**returning_status** | **bool** |  | 

## Example

```python
from rscapi.models.activity_request import ActivityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityRequest from a JSON string
activity_request_instance = ActivityRequest.from_json(json)
# print the JSON string representation of the object
print(ActivityRequest.to_json())

# convert the object into a dict
activity_request_dict = activity_request_instance.to_dict()
# create an instance of ActivityRequest from a dict
activity_request_from_dict = ActivityRequest.from_dict(activity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



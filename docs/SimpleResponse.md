# SimpleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 

## Example

```python
from rscapi.models.simple_response import SimpleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleResponse from a JSON string
simple_response_instance = SimpleResponse.from_json(json)
# print the JSON string representation of the object
print(SimpleResponse.to_json())

# convert the object into a dict
simple_response_dict = simple_response_instance.to_dict()
# create an instance of SimpleResponse from a dict
simple_response_from_dict = SimpleResponse.from_dict(simple_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TrackerCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discord_id** | **int** | The Discord ID of the member to link the tracker to. | 
**link** | **str** | Rocket Tracker Link | 

## Example

```python
from rscapi.models.tracker_create_input import TrackerCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerCreateInput from a JSON string
tracker_create_input_instance = TrackerCreateInput.from_json(json)
# print the JSON string representation of the object
print(TrackerCreateInput.to_json())

# convert the object into a dict
tracker_create_input_dict = tracker_create_input_instance.to_dict()
# create an instance of TrackerCreateInput from a dict
tracker_create_input_from_dict = TrackerCreateInput.from_dict(tracker_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



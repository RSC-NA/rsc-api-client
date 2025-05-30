# TrackerIDInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracker_id** | **int** | The ID of the tracker link to be processed. | 

## Example

```python
from rscapi.models.tracker_id_input import TrackerIDInput

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerIDInput from a JSON string
tracker_id_input_instance = TrackerIDInput.from_json(json)
# print the JSON string representation of the object
print(TrackerIDInput.to_json())

# convert the object into a dict
tracker_id_input_dict = tracker_id_input_instance.to_dict()
# create an instance of TrackerIDInput from a dict
tracker_id_input_from_dict = TrackerIDInput.from_dict(tracker_id_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



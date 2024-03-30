# ScheduleIngestRequestBody

Values required for schedule submitting for a given season.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sheet_link** | **str** | The link to the google sheet containing scheduling information. | 

## Example

```python
from rscapi.models.schedule_ingest_request_body import ScheduleIngestRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleIngestRequestBody from a JSON string
schedule_ingest_request_body_instance = ScheduleIngestRequestBody.from_json(json)
# print the JSON string representation of the object
print(ScheduleIngestRequestBody.to_json())

# convert the object into a dict
schedule_ingest_request_body_dict = schedule_ingest_request_body_instance.to_dict()
# create an instance of ScheduleIngestRequestBody from a dict
schedule_ingest_request_body_form_dict = schedule_ingest_request_body.from_dict(schedule_ingest_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BulkMMRSchemaSubmission

A list of MMR objects to submit for processing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mmrs** | **List[object]** | The list of MMR objects | 

## Example

```python
from rscapi.models.bulk_mmr_schema_submission import BulkMMRSchemaSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of BulkMMRSchemaSubmission from a JSON string
bulk_mmr_schema_submission_instance = BulkMMRSchemaSubmission.from_json(json)
# print the JSON string representation of the object
print(BulkMMRSchemaSubmission.to_json())

# convert the object into a dict
bulk_mmr_schema_submission_dict = bulk_mmr_schema_submission_instance.to_dict()
# create an instance of BulkMMRSchemaSubmission from a dict
bulk_mmr_schema_submission_form_dict = bulk_mmr_schema_submission.from_dict(bulk_mmr_schema_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



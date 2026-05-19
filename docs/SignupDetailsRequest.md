# SignupDetailsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rsc_name** | **str** |  | [optional] 
**league** | **int** |  | 
**platform** | [**PlatformEnum**](PlatformEnum.md) |  | 
**referrer** | [**ReferrerEnum**](ReferrerEnum.md) |  | 
**region_preference** | [**RegionPreferenceEnum**](RegionPreferenceEnum.md) |  | 
**new_or_returning** | [**NewOrReturningEnum**](NewOrReturningEnum.md) |  | 
**accepted_rules** | **bool** |  | 
**accepted_match_nights** | **bool** |  | 
**tracker_links** | **List[str]** |  | 
**admin_override** | **bool** |  | [optional] 
**executor** | **int** |  | [optional] 

## Example

```python
from rscapi.models.signup_details_request import SignupDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SignupDetailsRequest from a JSON string
signup_details_request_instance = SignupDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(SignupDetailsRequest.to_json())

# convert the object into a dict
signup_details_request_dict = signup_details_request_instance.to_dict()
# create an instance of SignupDetailsRequest from a dict
signup_details_request_from_dict = SignupDetailsRequest.from_dict(signup_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



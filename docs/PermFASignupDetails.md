# PermFASignupDetails


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
from rscapi.models.perm_fa_signup_details import PermFASignupDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PermFASignupDetails from a JSON string
perm_fa_signup_details_instance = PermFASignupDetails.from_json(json)
# print the JSON string representation of the object
print(PermFASignupDetails.to_json())

# convert the object into a dict
perm_fa_signup_details_dict = perm_fa_signup_details_instance.to_dict()
# create an instance of PermFASignupDetails from a dict
perm_fa_signup_details_from_dict = PermFASignupDetails.from_dict(perm_fa_signup_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



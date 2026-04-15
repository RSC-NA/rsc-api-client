# rscapi.ElevatedRolesApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**elevated_roles_list**](ElevatedRolesApi.md#elevated_roles_list) | **GET** /elevated-roles/ | 


# **elevated_roles_list**
> ElevatedRolesList200Response elevated_roles_list(position=position, league=league, gm=gm, agm=agm, limit=limit, offset=offset)

List all elevated roles with optional filters.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.elevated_roles_list200_response import ElevatedRolesList200Response
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://staging-api.rscna.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Api-Key
configuration.api_key['Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
async with rscapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rscapi.ElevatedRolesApi(api_client)
    position = 'position_example' # str | Staff position (optional)
    league = 56 # int | League ID (optional)
    gm = True # bool | General Manager (optional)
    agm = True # bool | Assistant GM (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.elevated_roles_list(position=position, league=league, gm=gm, agm=agm, limit=limit, offset=offset)
        print("The response of ElevatedRolesApi->elevated_roles_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ElevatedRolesApi->elevated_roles_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**| Staff position | [optional] 
 **league** | **int**| League ID | [optional] 
 **gm** | **bool**| General Manager | [optional] 
 **agm** | **bool**| Assistant GM | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**ElevatedRolesList200Response**](ElevatedRolesList200Response.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# openapi_client.NumbersApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**numbers_mmr_list**](NumbersApi.md#numbers_mmr_list) | **GET** /numbers/mmr/ | 
[**numbers_mmr_read**](NumbersApi.md#numbers_mmr_read) | **GET** /numbers/mmr/{id}/ | 


# **numbers_mmr_list**
> List[PlayerMMR] numbers_mmr_list(pulled=pulled, rscid=rscid)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.player_mmr import PlayerMMR
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging-api.rscna.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NumbersApi(api_client)
    pulled = 'pulled_example' # str | pulled (optional)
    rscid = 'rscid_example' # str | rscid (optional)

    try:
        api_response = await api_instance.numbers_mmr_list(pulled=pulled, rscid=rscid)
        print("The response of NumbersApi->numbers_mmr_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NumbersApi->numbers_mmr_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulled** | **str**| pulled | [optional] 
 **rscid** | **str**| rscid | [optional] 

### Return type

[**List[PlayerMMR]**](PlayerMMR.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numbers_mmr_read**
> PlayerMMR numbers_mmr_read(id)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.player_mmr import PlayerMMR
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging-api.rscna.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NumbersApi(api_client)
    id = 56 # int | A unique integer value identifying this player mmr pull.

    try:
        api_response = await api_instance.numbers_mmr_read(id)
        print("The response of NumbersApi->numbers_mmr_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NumbersApi->numbers_mmr_read: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this player mmr pull. | 

### Return type

[**PlayerMMR**](PlayerMMR.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


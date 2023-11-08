# rscapi.FranchisesApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**franchises_list**](FranchisesApi.md#franchises_list) | **GET** /franchises/ | 
[**franchises_read**](FranchisesApi.md#franchises_read) | **GET** /franchises/{id}/ | 


# **franchises_list**
> List[FranchiseList] franchises_list(prefix=prefix, league=league, gm_name=gm_name, name=name, tier=tier, tier_name=tier_name)



Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import rscapi
from rscapi.models.franchise_list import FranchiseList
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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with rscapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rscapi.FranchisesApi(api_client)
    prefix = 'prefix_example' # str | prefix (optional)
    league = 'league_example' # str | league (optional)
    gm_name = 'gm_name_example' # str | gm_name (optional)
    name = 'name_example' # str | name (optional)
    tier = 'tier_example' # str | tier (optional)
    tier_name = 'tier_name_example' # str | tier_name (optional)

    try:
        api_response = await api_instance.franchises_list(prefix=prefix, league=league, gm_name=gm_name, name=name, tier=tier, tier_name=tier_name)
        print("The response of FranchisesApi->franchises_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| prefix | [optional] 
 **league** | **str**| league | [optional] 
 **gm_name** | **str**| gm_name | [optional] 
 **name** | **str**| name | [optional] 
 **tier** | **str**| tier | [optional] 
 **tier_name** | **str**| tier_name | [optional] 

### Return type

[**List[FranchiseList]**](FranchiseList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **franchises_read**
> Franchise franchises_read(id)



Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import rscapi
from rscapi.models.franchise import Franchise
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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with rscapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rscapi.FranchisesApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.

    try:
        api_response = await api_instance.franchises_read(id)
        print("The response of FranchisesApi->franchises_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_read: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 

### Return type

[**Franchise**](Franchise.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


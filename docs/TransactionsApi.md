# rscapi.TransactionsApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactions_cut_create**](TransactionsApi.md#transactions_cut_create) | **POST** /transactions/cut/ | 
[**transactions_sign_create**](TransactionsApi.md#transactions_sign_create) | **POST** /transactions/sign/ | 


# **transactions_cut_create**
> CutAPlayerFromALeague transactions_cut_create(data)



Cut a player

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import rscapi
from rscapi.models.cut_a_player_from_a_league import CutAPlayerFromALeague
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
    api_instance = rscapi.TransactionsApi(api_client)
    data = rscapi.CutAPlayerFromALeague() # CutAPlayerFromALeague | 

    try:
        api_response = await api_instance.transactions_cut_create(data)
        print("The response of TransactionsApi->transactions_cut_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_cut_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CutAPlayerFromALeague**](CutAPlayerFromALeague.md)|  | 

### Return type

[**CutAPlayerFromALeague**](CutAPlayerFromALeague.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_sign_create**
> SignAPlayerToATeamInALeague transactions_sign_create(data)



Sign a player

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import rscapi
from rscapi.models.sign_a_player_to_a_team_in_a_league import SignAPlayerToATeamInALeague
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
    api_instance = rscapi.TransactionsApi(api_client)
    data = rscapi.SignAPlayerToATeamInALeague() # SignAPlayerToATeamInALeague | 

    try:
        api_response = await api_instance.transactions_sign_create(data)
        print("The response of TransactionsApi->transactions_sign_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_sign_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SignAPlayerToATeamInALeague**](SignAPlayerToATeamInALeague.md)|  | 

### Return type

[**SignAPlayerToATeamInALeague**](SignAPlayerToATeamInALeague.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


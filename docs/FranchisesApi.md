# rscapi.FranchisesApi

All URIs are relative to *https://api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**franchises_list**](FranchisesApi.md#franchises_list) | **GET** /franchises/ | 
[**franchises_logo**](FranchisesApi.md#franchises_logo) | **GET** /franchises/{id}/logo/ | 
[**franchises_read**](FranchisesApi.md#franchises_read) | **GET** /franchises/{id}/ | 


# **franchises_list**
> List[FranchiseList] franchises_list(prefix=prefix, league=league, gm_name=gm_name, gm_discord_id=gm_discord_id, name=name, tier=tier, tier_name=tier_name)

Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise_list import FranchiseList
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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
    api_instance = rscapi.FranchisesApi(api_client)
    prefix = 'prefix_example' # str | prefix (optional)
    league = 56 # int | League id (optional)
    gm_name = 'gm_name_example' # str | gm_name (optional)
    gm_discord_id = 56 # int | Discord id of GM (optional)
    name = 'name_example' # str | name (optional)
    tier = 56 # int | ID of Tier players are in. (optional)
    tier_name = 'tier_name_example' # str | tier_name (optional)

    try:
        api_response = await api_instance.franchises_list(prefix=prefix, league=league, gm_name=gm_name, gm_discord_id=gm_discord_id, name=name, tier=tier, tier_name=tier_name)
        print("The response of FranchisesApi->franchises_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| prefix | [optional] 
 **league** | **int**| League id | [optional] 
 **gm_name** | **str**| gm_name | [optional] 
 **gm_discord_id** | **int**| Discord id of GM | [optional] 
 **name** | **str**| name | [optional] 
 **tier** | **int**| ID of Tier players are in. | [optional] 
 **tier_name** | **str**| tier_name | [optional] 

### Return type

[**List[FranchiseList]**](FranchiseList.md)

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

# **franchises_logo**
> FranchiseLogo franchises_logo(id)

Get direct link for logo of a franchise

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise_logo import FranchiseLogo
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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
    api_instance = rscapi.FranchisesApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.

    try:
        api_response = await api_instance.franchises_logo(id)
        print("The response of FranchisesApi->franchises_logo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_logo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 

### Return type

[**FranchiseLogo**](FranchiseLogo.md)

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

# **franchises_read**
> Franchise franchises_read(id)

Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise import Franchise
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


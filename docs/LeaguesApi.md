# rscapi.LeaguesApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**leagues_current_season**](LeaguesApi.md#leagues_current_season) | **GET** /leagues/{id}/current_season/ | 
[**leagues_list**](LeaguesApi.md#leagues_list) | **GET** /leagues/ | 
[**leagues_read**](LeaguesApi.md#leagues_read) | **GET** /leagues/{id}/ | 
[**leagues_seasons**](LeaguesApi.md#leagues_seasons) | **GET** /leagues/{id}/seasons/ | 


# **leagues_current_season**
> Season leagues_current_season(id)



Get current season for a given league

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.season import Season
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
    api_instance = rscapi.LeaguesApi(api_client)
    id = 56 # int | A unique integer value identifying this league.

    try:
        api_response = await api_instance.leagues_current_season(id)
        print("The response of LeaguesApi->leagues_current_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_current_season: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league. | 

### Return type

[**Season**](Season.md)

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

# **leagues_list**
> List[League] leagues_list()



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league import League
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
    api_instance = rscapi.LeaguesApi(api_client)

    try:
        api_response = await api_instance.leagues_list()
        print("The response of LeaguesApi->leagues_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[League]**](League.md)

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

# **leagues_read**
> League leagues_read(id)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league import League
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
    api_instance = rscapi.LeaguesApi(api_client)
    id = 56 # int | A unique integer value identifying this league.

    try:
        api_response = await api_instance.leagues_read(id)
        print("The response of LeaguesApi->leagues_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league. | 

### Return type

[**League**](League.md)

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

# **leagues_seasons**
> List[Season] leagues_seasons(id)



Get all seasons for a given league.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.season import Season
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
    api_instance = rscapi.LeaguesApi(api_client)
    id = 56 # int | A unique integer value identifying this league.

    try:
        api_response = await api_instance.leagues_seasons(id)
        print("The response of LeaguesApi->leagues_seasons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_seasons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league. | 

### Return type

[**List[Season]**](Season.md)

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


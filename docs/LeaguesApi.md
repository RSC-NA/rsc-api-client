# rscapi.LeaguesApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**leagues_add_tier**](LeaguesApi.md#leagues_add_tier) | **PUT** /leagues/{id}/add_tier/ | 
[**leagues_current_season**](LeaguesApi.md#leagues_current_season) | **GET** /leagues/{id}/current_season/ | 
[**leagues_expire_subs**](LeaguesApi.md#leagues_expire_subs) | **POST** /leagues/{id}/expire_subs/ | 
[**leagues_list**](LeaguesApi.md#leagues_list) | **GET** /leagues/ | 
[**leagues_read**](LeaguesApi.md#leagues_read) | **GET** /leagues/{id}/ | 
[**leagues_remove_tier**](LeaguesApi.md#leagues_remove_tier) | **PUT** /leagues/{id}/remove_tier/ | 
[**leagues_seasons**](LeaguesApi.md#leagues_seasons) | **GET** /leagues/{id}/seasons/ | 
[**leagues_start_new_season**](LeaguesApi.md#leagues_start_new_season) | **POST** /leagues/{id}/start_new_season/ | 


# **leagues_add_tier**
> League leagues_add_tier(id, data)

Add a tier to a league

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.add_tier_to_league import AddTierToLeague
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
    data = rscapi.AddTierToLeague() # AddTierToLeague | 

    try:
        api_response = await api_instance.leagues_add_tier(id, data)
        print("The response of LeaguesApi->leagues_add_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_add_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league. | 
 **data** | [**AddTierToLeague**](AddTierToLeague.md)|  | 

### Return type

[**League**](League.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **leagues_expire_subs**
> League leagues_expire_subs(id, data)

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
    data = rscapi.League() # League | 

    try:
        api_response = await api_instance.leagues_expire_subs(id, data)
        print("The response of LeaguesApi->leagues_expire_subs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_expire_subs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league. | 
 **data** | [**League**](League.md)|  | 

### Return type

[**League**](League.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leagues_list**
> List[League] leagues_list(name=name, guild_id=guild_id)

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
    name = 'name_example' # str | name (optional)
    guild_id = 'guild_id_example' # str | guild_id (optional)

    try:
        api_response = await api_instance.leagues_list(name=name, guild_id=guild_id)
        print("The response of LeaguesApi->leagues_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | [optional] 
 **guild_id** | **str**| guild_id | [optional] 

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

# **leagues_remove_tier**
> Deleted leagues_remove_tier(id, data)

Remove a tier from a league

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.deleted import Deleted
from rscapi.models.remove_tier_from_a_league import RemoveTierFromALeague
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
    data = rscapi.RemoveTierFromALeague() # RemoveTierFromALeague | 

    try:
        api_response = await api_instance.leagues_remove_tier(id, data)
        print("The response of LeaguesApi->leagues_remove_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_remove_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league. | 
 **data** | [**RemoveTierFromALeague**](RemoveTierFromALeague.md)|  | 

### Return type

[**Deleted**](Deleted.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

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

# **leagues_start_new_season**
> Season leagues_start_new_season(id, data)

Start a new season for a given league

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.season import Season
from rscapi.models.start_new_season import StartNewSeason
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
    data = rscapi.StartNewSeason() # StartNewSeason | 

    try:
        api_response = await api_instance.leagues_start_new_season(id, data)
        print("The response of LeaguesApi->leagues_start_new_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_start_new_season: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league. | 
 **data** | [**StartNewSeason**](StartNewSeason.md)|  | 

### Return type

[**Season**](Season.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


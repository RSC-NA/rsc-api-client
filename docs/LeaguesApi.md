# rscapi.LeaguesApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**leagues_add_tier_update**](LeaguesApi.md#leagues_add_tier_update) | **PUT** /leagues/{id}/add_tier/ | 
[**leagues_create**](LeaguesApi.md#leagues_create) | **POST** /leagues/ | 
[**leagues_current_season_retrieve**](LeaguesApi.md#leagues_current_season_retrieve) | **GET** /leagues/{id}/current_season/ | 
[**leagues_destroy**](LeaguesApi.md#leagues_destroy) | **DELETE** /leagues/{id}/ | 
[**leagues_expire_subs_create**](LeaguesApi.md#leagues_expire_subs_create) | **POST** /leagues/{id}/expire_subs/ | 
[**leagues_list**](LeaguesApi.md#leagues_list) | **GET** /leagues/ | 
[**leagues_partial_update**](LeaguesApi.md#leagues_partial_update) | **PATCH** /leagues/{id}/ | 
[**leagues_remove_tier_update**](LeaguesApi.md#leagues_remove_tier_update) | **PUT** /leagues/{id}/remove_tier/ | 
[**leagues_retrieve**](LeaguesApi.md#leagues_retrieve) | **GET** /leagues/{id}/ | 
[**leagues_seasons_list**](LeaguesApi.md#leagues_seasons_list) | **GET** /leagues/{id}/seasons/ | 
[**leagues_start_new_season_create**](LeaguesApi.md#leagues_start_new_season_create) | **POST** /leagues/{id}/start_new_season/ | 
[**leagues_update**](LeaguesApi.md#leagues_update) | **PUT** /leagues/{id}/ | 


# **leagues_add_tier_update**
> League leagues_add_tier_update(id, tier_league_add)

Add a tier to a league

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league import League
from rscapi.models.tier_league_add import TierLeagueAdd
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "/api/v1"
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
    tier_league_add = rscapi.TierLeagueAdd() # TierLeagueAdd | 

    try:
        api_response = await api_instance.leagues_add_tier_update(id, tier_league_add)
        print("The response of LeaguesApi->leagues_add_tier_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_add_tier_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league. | 
 **tier_league_add** | [**TierLeagueAdd**](TierLeagueAdd.md)|  | 

### Return type

[**League**](League.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leagues_create**
> League leagues_create(league)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league import League
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "/api/v1"
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
    league = rscapi.League() # League | 

    try:
        api_response = await api_instance.leagues_create(league)
        print("The response of LeaguesApi->leagues_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league** | [**League**](League.md)|  | 

### Return type

[**League**](League.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leagues_current_season_retrieve**
> Season leagues_current_season_retrieve(id)

Get current season for a given league

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.season import Season
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "/api/v1"
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
        api_response = await api_instance.leagues_current_season_retrieve(id)
        print("The response of LeaguesApi->leagues_current_season_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_current_season_retrieve: %s\n" % e)
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

# **leagues_destroy**
> leagues_destroy(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "/api/v1"
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
        await api_instance.leagues_destroy(id)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league. | 

### Return type

void (empty response body)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leagues_expire_subs_create**
> League leagues_expire_subs_create(id, league)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league import League
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "/api/v1"
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
    league = rscapi.League() # League | 

    try:
        api_response = await api_instance.leagues_expire_subs_create(id, league)
        print("The response of LeaguesApi->leagues_expire_subs_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_expire_subs_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league. | 
 **league** | [**League**](League.md)|  | 

### Return type

[**League**](League.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leagues_list**
> List[League] leagues_list(guild_id=guild_id, name=name)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league import League
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "/api/v1"
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
    guild_id = 56 # int | Discord guild ID (optional)
    name = 'name_example' # str | League name (optional)

    try:
        api_response = await api_instance.leagues_list(guild_id=guild_id, name=name)
        print("The response of LeaguesApi->leagues_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **int**| Discord guild ID | [optional] 
 **name** | **str**| League name | [optional] 

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

# **leagues_partial_update**
> League leagues_partial_update(id, patched_league=patched_league)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league import League
from rscapi.models.patched_league import PatchedLeague
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "/api/v1"
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
    patched_league = rscapi.PatchedLeague() # PatchedLeague |  (optional)

    try:
        api_response = await api_instance.leagues_partial_update(id, patched_league=patched_league)
        print("The response of LeaguesApi->leagues_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league. | 
 **patched_league** | [**PatchedLeague**](PatchedLeague.md)|  | [optional] 

### Return type

[**League**](League.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leagues_remove_tier_update**
> Deleted leagues_remove_tier_update(id, tier_league_add)

Remove a tier from a league

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.deleted import Deleted
from rscapi.models.tier_league_add import TierLeagueAdd
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "/api/v1"
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
    tier_league_add = rscapi.TierLeagueAdd() # TierLeagueAdd | 

    try:
        api_response = await api_instance.leagues_remove_tier_update(id, tier_league_add)
        print("The response of LeaguesApi->leagues_remove_tier_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_remove_tier_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league. | 
 **tier_league_add** | [**TierLeagueAdd**](TierLeagueAdd.md)|  | 

### Return type

[**Deleted**](Deleted.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leagues_retrieve**
> League leagues_retrieve(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league import League
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "/api/v1"
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
        api_response = await api_instance.leagues_retrieve(id)
        print("The response of LeaguesApi->leagues_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_retrieve: %s\n" % e)
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

# **leagues_seasons_list**
> List[Season] leagues_seasons_list(id)

Get all seasons for a given league.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.season import Season
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "/api/v1"
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
        api_response = await api_instance.leagues_seasons_list(id)
        print("The response of LeaguesApi->leagues_seasons_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_seasons_list: %s\n" % e)
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

# **leagues_start_new_season_create**
> Season leagues_start_new_season_create(id, league_season_start)

Start a new season for a given league

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_season_start import LeagueSeasonStart
from rscapi.models.season import Season
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "/api/v1"
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
    league_season_start = rscapi.LeagueSeasonStart() # LeagueSeasonStart | 

    try:
        api_response = await api_instance.leagues_start_new_season_create(id, league_season_start)
        print("The response of LeaguesApi->leagues_start_new_season_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_start_new_season_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league. | 
 **league_season_start** | [**LeagueSeasonStart**](LeagueSeasonStart.md)|  | 

### Return type

[**Season**](Season.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leagues_update**
> League leagues_update(id, league)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league import League
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "/api/v1"
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
    league = rscapi.League() # League | 

    try:
        api_response = await api_instance.leagues_update(id, league)
        print("The response of LeaguesApi->leagues_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguesApi->leagues_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league. | 
 **league** | [**League**](League.md)|  | 

### Return type

[**League**](League.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# rscapi.SeasonsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**seasons_activity_check_list**](SeasonsApi.md#seasons_activity_check_list) | **GET** /seasons/activity_check/ | 
[**seasons_activity_check_retrieve**](SeasonsApi.md#seasons_activity_check_retrieve) | **GET** /seasons/activity_check/{id}/ | 
[**seasons_create**](SeasonsApi.md#seasons_create) | **POST** /seasons/ | 
[**seasons_destroy**](SeasonsApi.md#seasons_destroy) | **DELETE** /seasons/{id}/ | 
[**seasons_franchise_standings_list**](SeasonsApi.md#seasons_franchise_standings_list) | **GET** /seasons/{id}/franchise_standings/ | 
[**seasons_league_season_retrieve**](SeasonsApi.md#seasons_league_season_retrieve) | **GET** /seasons/league_season/ | 
[**seasons_list**](SeasonsApi.md#seasons_list) | **GET** /seasons/ | 
[**seasons_partial_update**](SeasonsApi.md#seasons_partial_update) | **PATCH** /seasons/{id}/ | 
[**seasons_player_intents_list**](SeasonsApi.md#seasons_player_intents_list) | **GET** /seasons/{id}/player_intents/ | 
[**seasons_retrieve**](SeasonsApi.md#seasons_retrieve) | **GET** /seasons/{id}/ | 
[**seasons_signup_season_retrieve**](SeasonsApi.md#seasons_signup_season_retrieve) | **GET** /seasons/signup_season/ | 
[**seasons_update**](SeasonsApi.md#seasons_update) | **PUT** /seasons/{id}/ | 


# **seasons_activity_check_list**
> PaginatedActivityCheckList seasons_activity_check_list(completed=completed, discord_id=discord_id, limit=limit, missing=missing, offset=offset, returning_status=returning_status, season=season, season_number=season_number)

List all activity checks for a given season.

Missing ActivityCheck records are automatically created for active
league players who have not yet submitted one.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.paginated_activity_check_list import PaginatedActivityCheckList
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
    api_instance = rscapi.SeasonsApi(api_client)
    completed = True # bool | Check has been completed or not. (optional)
    discord_id = 56 # int | Discord ID of player intent to search for. (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    missing = True # bool | If the player has responded or not. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    returning_status = True # bool | If the player is returning or not. (optional)
    season = 56 # int | Season ID (E.g: 8) (optional)
    season_number = 56 # int | Season number to search for. (E.g: 18) (optional)

    try:
        api_response = await api_instance.seasons_activity_check_list(completed=completed, discord_id=discord_id, limit=limit, missing=missing, offset=offset, returning_status=returning_status, season=season, season_number=season_number)
        print("The response of SeasonsApi->seasons_activity_check_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_activity_check_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **completed** | **bool**| Check has been completed or not. | [optional] 
 **discord_id** | **int**| Discord ID of player intent to search for. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **missing** | **bool**| If the player has responded or not. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **returning_status** | **bool**| If the player is returning or not. | [optional] 
 **season** | **int**| Season ID (E.g: 8) | [optional] 
 **season_number** | **int**| Season number to search for. (E.g: 18) | [optional] 

### Return type

[**PaginatedActivityCheckList**](PaginatedActivityCheckList.md)

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

# **seasons_activity_check_retrieve**
> ActivityCheck seasons_activity_check_retrieve(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.activity_check import ActivityCheck
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
    api_instance = rscapi.SeasonsApi(api_client)
    id = 56 # int | A unique integer value identifying this activity check.

    try:
        api_response = await api_instance.seasons_activity_check_retrieve(id)
        print("The response of SeasonsApi->seasons_activity_check_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_activity_check_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this activity check. | 

### Return type

[**ActivityCheck**](ActivityCheck.md)

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

# **seasons_create**
> Season seasons_create(season)

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
    api_instance = rscapi.SeasonsApi(api_client)
    season = rscapi.Season() # Season | 

    try:
        api_response = await api_instance.seasons_create(season)
        print("The response of SeasonsApi->seasons_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | [**Season**](Season.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seasons_destroy**
> seasons_destroy(id)

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
    api_instance = rscapi.SeasonsApi(api_client)
    id = 56 # int | A unique integer value identifying this season.

    try:
        await api_instance.seasons_destroy(id)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this season. | 

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

# **seasons_franchise_standings_list**
> List[FranchiseStandings] seasons_franchise_standings_list(id)

Get franchise standings for a given season

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise_standings import FranchiseStandings
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
    api_instance = rscapi.SeasonsApi(api_client)
    id = 56 # int | A unique integer value identifying this season.

    try:
        api_response = await api_instance.seasons_franchise_standings_list(id)
        print("The response of SeasonsApi->seasons_franchise_standings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_franchise_standings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this season. | 

### Return type

[**List[FranchiseStandings]**](FranchiseStandings.md)

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

# **seasons_league_season_retrieve**
> Season seasons_league_season_retrieve(league)

Get current season for a given league.

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
    api_instance = rscapi.SeasonsApi(api_client)
    league = 56 # int | League to get current season for.

    try:
        api_response = await api_instance.seasons_league_season_retrieve(league)
        print("The response of SeasonsApi->seasons_league_season_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_league_season_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league** | **int**| League to get current season for. | 

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
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seasons_list**
> List[Season] seasons_list(current=current, league=league, number=number)

Get list of seasons.

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
    api_instance = rscapi.SeasonsApi(api_client)
    current = True # bool | If true, only return the current season(s). (optional)
    league = 56 # int | ID of league to filter seasons by. (optional)
    number = 56 # int | Season number to filter seasons by. (optional)

    try:
        api_response = await api_instance.seasons_list(current=current, league=league, number=number)
        print("The response of SeasonsApi->seasons_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **current** | **bool**| If true, only return the current season(s). | [optional] 
 **league** | **int**| ID of league to filter seasons by. | [optional] 
 **number** | **int**| Season number to filter seasons by. | [optional] 

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

# **seasons_partial_update**
> Season seasons_partial_update(id, patched_season=patched_season)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.patched_season import PatchedSeason
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
    api_instance = rscapi.SeasonsApi(api_client)
    id = 56 # int | A unique integer value identifying this season.
    patched_season = rscapi.PatchedSeason() # PatchedSeason |  (optional)

    try:
        api_response = await api_instance.seasons_partial_update(id, patched_season=patched_season)
        print("The response of SeasonsApi->seasons_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this season. | 
 **patched_season** | [**PatchedSeason**](PatchedSeason.md)|  | [optional] 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seasons_player_intents_list**
> List[IntentToPlay] seasons_player_intents_list(id, discord_id=discord_id, missing=missing, returning=returning)

Get player intents for a specific season

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.intent_to_play import IntentToPlay
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
    api_instance = rscapi.SeasonsApi(api_client)
    id = 56 # int | A unique integer value identifying this season.
    discord_id = 56 # int |  (optional)
    missing = True # bool |  (optional)
    returning = True # bool |  (optional)

    try:
        api_response = await api_instance.seasons_player_intents_list(id, discord_id=discord_id, missing=missing, returning=returning)
        print("The response of SeasonsApi->seasons_player_intents_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_player_intents_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this season. | 
 **discord_id** | **int**|  | [optional] 
 **missing** | **bool**|  | [optional] 
 **returning** | **bool**|  | [optional] 

### Return type

[**List[IntentToPlay]**](IntentToPlay.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seasons_retrieve**
> Season seasons_retrieve(id)

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
    api_instance = rscapi.SeasonsApi(api_client)
    id = 56 # int | A unique integer value identifying this season.

    try:
        api_response = await api_instance.seasons_retrieve(id)
        print("The response of SeasonsApi->seasons_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this season. | 

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

# **seasons_signup_season_retrieve**
> Season seasons_signup_season_retrieve(league)

Get the season currently accepting signups.

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
    api_instance = rscapi.SeasonsApi(api_client)
    league = 56 # int | League to get current season for.

    try:
        api_response = await api_instance.seasons_signup_season_retrieve(league)
        print("The response of SeasonsApi->seasons_signup_season_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_signup_season_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league** | **int**| League to get current season for. | 

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
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seasons_update**
> Season seasons_update(id, season)

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
    api_instance = rscapi.SeasonsApi(api_client)
    id = 56 # int | A unique integer value identifying this season.
    season = rscapi.Season() # Season | 

    try:
        api_response = await api_instance.seasons_update(id, season)
        print("The response of SeasonsApi->seasons_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this season. | 
 **season** | [**Season**](Season.md)|  | 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


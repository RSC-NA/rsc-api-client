# rscapi.SeasonsApi

All URIs are relative to *http://127.0.0.1:8000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**seasons_activity_check_list**](SeasonsApi.md#seasons_activity_check_list) | **GET** /seasons/activity_check/ | 
[**seasons_activity_check_read**](SeasonsApi.md#seasons_activity_check_read) | **GET** /seasons/activity_check/{id}/ | 
[**seasons_franchise_standings**](SeasonsApi.md#seasons_franchise_standings) | **GET** /seasons/{id}/franchise_standings/ | 
[**seasons_league_season**](SeasonsApi.md#seasons_league_season) | **GET** /seasons/league_season/ | 
[**seasons_list**](SeasonsApi.md#seasons_list) | **GET** /seasons/ | 
[**seasons_player_intents**](SeasonsApi.md#seasons_player_intents) | **GET** /seasons/{id}/player_intents/ | 
[**seasons_read**](SeasonsApi.md#seasons_read) | **GET** /seasons/{id}/ | 


# **seasons_activity_check_list**
> SeasonsActivityCheckList200Response seasons_activity_check_list(discord_id=discord_id, completed=completed, returning_status=returning_status, missing=missing, season=season, season_number=season_number, limit=limit, offset=offset)

List all activity checks for a given season.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.seasons_activity_check_list200_response import SeasonsActivityCheckList200Response
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://127.0.0.1:8000/api/v1"
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
    discord_id = 56 # int | Discord ID of player intent to search for. (optional)
    completed = True # bool | Check has been completed or not. (optional)
    returning_status = True # bool | If the player is returning or not. (optional)
    missing = True # bool | If the player has responded or not. (optional)
    season = 56 # int | Season ID (E.g: 8) (optional)
    season_number = 56 # int | Season Number (E.g: 24) (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.seasons_activity_check_list(discord_id=discord_id, completed=completed, returning_status=returning_status, missing=missing, season=season, season_number=season_number, limit=limit, offset=offset)
        print("The response of SeasonsApi->seasons_activity_check_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_activity_check_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discord_id** | **int**| Discord ID of player intent to search for. | [optional] 
 **completed** | **bool**| Check has been completed or not. | [optional] 
 **returning_status** | **bool**| If the player is returning or not. | [optional] 
 **missing** | **bool**| If the player has responded or not. | [optional] 
 **season** | **int**| Season ID (E.g: 8) | [optional] 
 **season_number** | **int**| Season Number (E.g: 24) | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**SeasonsActivityCheckList200Response**](SeasonsActivityCheckList200Response.md)

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

# **seasons_activity_check_read**
> ActivityCheck seasons_activity_check_read(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.activity_check import ActivityCheck
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://127.0.0.1:8000/api/v1"
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
        api_response = await api_instance.seasons_activity_check_read(id)
        print("The response of SeasonsApi->seasons_activity_check_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_activity_check_read: %s\n" % e)
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

# **seasons_franchise_standings**
> List[FranchiseStandings] seasons_franchise_standings(id)

Get franchise standings for a given season

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise_standings import FranchiseStandings
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://127.0.0.1:8000/api/v1"
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
    id = 56 # int | A unique integer value identifying this seasons.

    try:
        api_response = await api_instance.seasons_franchise_standings(id)
        print("The response of SeasonsApi->seasons_franchise_standings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_franchise_standings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this seasons. | 

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

# **seasons_league_season**
> Season seasons_league_season(league)

Get current season for a given league.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.season import Season
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://127.0.0.1:8000/api/v1"
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
        api_response = await api_instance.seasons_league_season(league)
        print("The response of SeasonsApi->seasons_league_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_league_season: %s\n" % e)
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
> List[Season] seasons_list(league=league, number=number, current=current)

Get all seasons.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.season import Season
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://127.0.0.1:8000/api/v1"
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
    league = 'league_example' # str | league (optional)
    number = 'number_example' # str | number (optional)
    current = 'current_example' # str | current (optional)

    try:
        api_response = await api_instance.seasons_list(league=league, number=number, current=current)
        print("The response of SeasonsApi->seasons_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league** | **str**| league | [optional] 
 **number** | **str**| number | [optional] 
 **current** | **str**| current | [optional] 

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

# **seasons_player_intents**
> List[IntentToPlay] seasons_player_intents(id, discord_id=discord_id, returning=returning, missing=missing)

Get player intents for a specific season

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.intent_to_play import IntentToPlay
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://127.0.0.1:8000/api/v1"
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
    id = 56 # int | A unique integer value identifying this seasons.
    discord_id = 56 # int | Discord ID of player intent to search for. (optional)
    returning = True # bool | If the player is returning or not. (optional)
    missing = True # bool | If the player has responded or not. (optional)

    try:
        api_response = await api_instance.seasons_player_intents(id, discord_id=discord_id, returning=returning, missing=missing)
        print("The response of SeasonsApi->seasons_player_intents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_player_intents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this seasons. | 
 **discord_id** | **int**| Discord ID of player intent to search for. | [optional] 
 **returning** | **bool**| If the player is returning or not. | [optional] 
 **missing** | **bool**| If the player has responded or not. | [optional] 

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

# **seasons_read**
> Season seasons_read(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.season import Season
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://127.0.0.1:8000/api/v1"
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
    id = 56 # int | A unique integer value identifying this seasons.

    try:
        api_response = await api_instance.seasons_read(id)
        print("The response of SeasonsApi->seasons_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this seasons. | 

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


# rscapi.SeasonsApi

All URIs are relative to *https://api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**seasons_create**](SeasonsApi.md#seasons_create) | **POST** /seasons/ | 
[**seasons_delete**](SeasonsApi.md#seasons_delete) | **DELETE** /seasons/{id}/ | 
[**seasons_franchise_standings**](SeasonsApi.md#seasons_franchise_standings) | **GET** /seasons/{id}/franchise_standings/ | 
[**seasons_league_season**](SeasonsApi.md#seasons_league_season) | **GET** /seasons/league_season/ | 
[**seasons_list**](SeasonsApi.md#seasons_list) | **GET** /seasons/ | 
[**seasons_partial_update**](SeasonsApi.md#seasons_partial_update) | **PATCH** /seasons/{id}/ | 
[**seasons_player_intents**](SeasonsApi.md#seasons_player_intents) | **GET** /seasons/{id}/player_intents/ | 
[**seasons_read**](SeasonsApi.md#seasons_read) | **GET** /seasons/{id}/ | 
[**seasons_submit_schedule**](SeasonsApi.md#seasons_submit_schedule) | **POST** /seasons/{id}/submit_schedule/ | 
[**seasons_update**](SeasonsApi.md#seasons_update) | **PUT** /seasons/{id}/ | 


# **seasons_create**
> Season seasons_create(data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.season import Season
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
    api_instance = rscapi.SeasonsApi(api_client)
    data = rscapi.Season() # Season | 

    try:
        api_response = await api_instance.seasons_create(data)
        print("The response of SeasonsApi->seasons_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Season**](Season.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seasons_delete**
> seasons_delete(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
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
    api_instance = rscapi.SeasonsApi(api_client)
    id = 56 # int | A unique integer value identifying this seasons.

    try:
        await api_instance.seasons_delete(id)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this seasons. | 

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
**204** |  |  -  |

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
> List[Season] seasons_list()

Get all seasons.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.season import Season
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
    api_instance = rscapi.SeasonsApi(api_client)

    try:
        api_response = await api_instance.seasons_list()
        print("The response of SeasonsApi->seasons_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
> Season seasons_partial_update(id, data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.season import Season
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
    api_instance = rscapi.SeasonsApi(api_client)
    id = 56 # int | A unique integer value identifying this seasons.
    data = rscapi.Season() # Season | 

    try:
        api_response = await api_instance.seasons_partial_update(id, data)
        print("The response of SeasonsApi->seasons_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this seasons. | 
 **data** | [**Season**](Season.md)|  | 

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
    api_instance = rscapi.SeasonsApi(api_client)
    id = 56 # int | A unique integer value identifying this seasons.
    discord_id = 56 # int | Discord ID of player intent to search for. (optional)
    returning = True # bool | If the player is returning or not. (optional)
    missing = True # bool | If the player has filled out their intent form or not. (optional)

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
 **missing** | **bool**| If the player has filled out their intent form or not. | [optional] 

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

# **seasons_submit_schedule**
> SimpleResponse seasons_submit_schedule(id, data)

Endpoint to provide a schedule for a given season

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.schedule_ingest_request_body import ScheduleIngestRequestBody
from rscapi.models.simple_response import SimpleResponse
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
    api_instance = rscapi.SeasonsApi(api_client)
    id = 56 # int | A unique integer value identifying this seasons.
    data = rscapi.ScheduleIngestRequestBody() # ScheduleIngestRequestBody | 

    try:
        api_response = await api_instance.seasons_submit_schedule(id, data)
        print("The response of SeasonsApi->seasons_submit_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_submit_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this seasons. | 
 **data** | [**ScheduleIngestRequestBody**](ScheduleIngestRequestBody.md)|  | 

### Return type

[**SimpleResponse**](SimpleResponse.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seasons_update**
> Season seasons_update(id, data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.season import Season
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
    api_instance = rscapi.SeasonsApi(api_client)
    id = 56 # int | A unique integer value identifying this seasons.
    data = rscapi.Season() # Season | 

    try:
        api_response = await api_instance.seasons_update(id, data)
        print("The response of SeasonsApi->seasons_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this seasons. | 
 **data** | [**Season**](Season.md)|  | 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


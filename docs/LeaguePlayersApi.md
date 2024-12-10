# rscapi.LeaguePlayersApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**league_players_create**](LeaguePlayersApi.md#league_players_create) | **POST** /league-players/ | 
[**league_players_delete**](LeaguePlayersApi.md#league_players_delete) | **DELETE** /league-players/{id}/ | 
[**league_players_list**](LeaguePlayersApi.md#league_players_list) | **GET** /league-players/ | 
[**league_players_partial_update**](LeaguePlayersApi.md#league_players_partial_update) | **PATCH** /league-players/{id}/ | 
[**league_players_postseason_stats**](LeaguePlayersApi.md#league_players_postseason_stats) | **GET** /league-players/{id}/postseason_stats/ | 
[**league_players_read**](LeaguePlayersApi.md#league_players_read) | **GET** /league-players/{id}/ | 
[**league_players_set_captain**](LeaguePlayersApi.md#league_players_set_captain) | **POST** /league-players/{id}/set_captain/ | 
[**league_players_stats**](LeaguePlayersApi.md#league_players_stats) | **GET** /league-players/{id}/stats/ | 
[**league_players_update**](LeaguePlayersApi.md#league_players_update) | **PUT** /league-players/{id}/ | 


# **league_players_create**
> LeaguePlayer league_players_create(data)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    data = rscapi.LeaguePlayer() # LeaguePlayer | 

    try:
        api_response = await api_instance.league_players_create(data)
        print("The response of LeaguePlayersApi->league_players_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**LeaguePlayer**](LeaguePlayer.md)|  | 

### Return type

[**LeaguePlayer**](LeaguePlayer.md)

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

# **league_players_delete**
> league_players_delete(id)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.

    try:
        await api_instance.league_players_delete(id)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league player. | 

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

# **league_players_list**
> LeaguePlayersList200Response league_players_list(status=status, name=name, tier=tier, tier_name=tier_name, season=season, season_number=season_number, league=league, team_name=team_name, franchise=franchise, sub_status=sub_status, discord_id=discord_id, limit=limit, offset=offset)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_players_list200_response import LeaguePlayersList200Response
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    status = 'status_example' # str | Player Status (Rostered, IR, etc.) (optional)
    name = 'name_example' # str | name (optional)
    tier = 56 # int | ID of Tier players are in. (optional)
    tier_name = 'tier_name_example' # str | Name of tier players are in. (optional)
    season = 56 # int | ID of season players played in. (optional)
    season_number = 56 # int | Number of season players played in. (optional)
    league = 56 # int | ID of League player is in. (optional)
    team_name = 'team_name_example' # str | Name of team players are on. (optional)
    franchise = 'franchise_example' # str | Name of franchise players are in. (optional)
    sub_status = 56 # int | Player current substitution status. (optional)
    discord_id = 56 # int | Discord ID of League Player (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.league_players_list(status=status, name=name, tier=tier, tier_name=tier_name, season=season, season_number=season_number, league=league, team_name=team_name, franchise=franchise, sub_status=sub_status, discord_id=discord_id, limit=limit, offset=offset)
        print("The response of LeaguePlayersApi->league_players_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Player Status (Rostered, IR, etc.) | [optional] 
 **name** | **str**| name | [optional] 
 **tier** | **int**| ID of Tier players are in. | [optional] 
 **tier_name** | **str**| Name of tier players are in. | [optional] 
 **season** | **int**| ID of season players played in. | [optional] 
 **season_number** | **int**| Number of season players played in. | [optional] 
 **league** | **int**| ID of League player is in. | [optional] 
 **team_name** | **str**| Name of team players are on. | [optional] 
 **franchise** | **str**| Name of franchise players are in. | [optional] 
 **sub_status** | **int**| Player current substitution status. | [optional] 
 **discord_id** | **int**| Discord ID of League Player | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**LeaguePlayersList200Response**](LeaguePlayersList200Response.md)

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

# **league_players_partial_update**
> LeaguePlayer league_players_partial_update(id, data, league=league)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
from rscapi.models.league_player_patch import LeaguePlayerPatch
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.
    data = rscapi.LeaguePlayerPatch() # LeaguePlayerPatch | 
    league = 56 # int | ID of league to update player in (optional)

    try:
        api_response = await api_instance.league_players_partial_update(id, data, league=league)
        print("The response of LeaguePlayersApi->league_players_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league player. | 
 **data** | [**LeaguePlayerPatch**](LeaguePlayerPatch.md)|  | 
 **league** | **int**| ID of league to update player in | [optional] 

### Return type

[**LeaguePlayer**](LeaguePlayer.md)

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

# **league_players_postseason_stats**
> PlayerSeasonStats league_players_postseason_stats(id)



Get postseason stats for a specific league player.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_season_stats import PlayerSeasonStats
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.

    try:
        api_response = await api_instance.league_players_postseason_stats(id)
        print("The response of LeaguePlayersApi->league_players_postseason_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_postseason_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league player. | 

### Return type

[**PlayerSeasonStats**](PlayerSeasonStats.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **league_players_read**
> LeaguePlayer league_players_read(id)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.

    try:
        api_response = await api_instance.league_players_read(id)
        print("The response of LeaguePlayersApi->league_players_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league player. | 

### Return type

[**LeaguePlayer**](LeaguePlayer.md)

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

# **league_players_set_captain**
> LeaguePlayer league_players_set_captain(id)



Set (Or unset) a player to be captain of their team.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.

    try:
        api_response = await api_instance.league_players_set_captain(id)
        print("The response of LeaguePlayersApi->league_players_set_captain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_set_captain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league player. | 

### Return type

[**LeaguePlayer**](LeaguePlayer.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **league_players_stats**
> PlayerSeasonStats league_players_stats(id)



Get stats for a specific league player.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_season_stats import PlayerSeasonStats
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.

    try:
        api_response = await api_instance.league_players_stats(id)
        print("The response of LeaguePlayersApi->league_players_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league player. | 

### Return type

[**PlayerSeasonStats**](PlayerSeasonStats.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **league_players_update**
> LeaguePlayer league_players_update(id, data)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.
    data = rscapi.LeaguePlayer() # LeaguePlayer | 

    try:
        api_response = await api_instance.league_players_update(id, data)
        print("The response of LeaguePlayersApi->league_players_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league player. | 
 **data** | [**LeaguePlayer**](LeaguePlayer.md)|  | 

### Return type

[**LeaguePlayer**](LeaguePlayer.md)

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


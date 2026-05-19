# rscapi.LeaguePlayersApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**league_players_create**](LeaguePlayersApi.md#league_players_create) | **POST** /league-players/ | 
[**league_players_destroy**](LeaguePlayersApi.md#league_players_destroy) | **DELETE** /league-players/{id}/ | 
[**league_players_list**](LeaguePlayersApi.md#league_players_list) | **GET** /league-players/ | 
[**league_players_partial_update**](LeaguePlayersApi.md#league_players_partial_update) | **PATCH** /league-players/{id}/ | 
[**league_players_postseason_stats_retrieve**](LeaguePlayersApi.md#league_players_postseason_stats_retrieve) | **GET** /league-players/{id}/postseason_stats/ | 
[**league_players_retrieve**](LeaguePlayersApi.md#league_players_retrieve) | **GET** /league-players/{id}/ | 
[**league_players_set_captain_create**](LeaguePlayersApi.md#league_players_set_captain_create) | **POST** /league-players/{id}/set_captain/ | 
[**league_players_stats_retrieve**](LeaguePlayersApi.md#league_players_stats_retrieve) | **GET** /league-players/{id}/stats/ | 
[**league_players_update**](LeaguePlayersApi.md#league_players_update) | **PUT** /league-players/{id}/ | 


# **league_players_create**
> LeaguePlayer league_players_create(league_player)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    league_player = rscapi.LeaguePlayer() # LeaguePlayer | 

    try:
        api_response = await api_instance.league_players_create(league_player)
        print("The response of LeaguePlayersApi->league_players_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_player** | [**LeaguePlayer**](LeaguePlayer.md)|  | 

### Return type

[**LeaguePlayer**](LeaguePlayer.md)

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

# **league_players_destroy**
> league_players_destroy(id)

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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.

    try:
        await api_instance.league_players_destroy(id)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_destroy: %s\n" % e)
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
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **league_players_list**
> PaginatedLeaguePlayerList league_players_list(captain=captain, discord_id=discord_id, franchise=franchise, league=league, limit=limit, name=name, offset=offset, season=season, season_number=season_number, status=status, sub_status=sub_status, team_name=team_name, tier=tier, tier_name=tier_name)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.paginated_league_player_list import PaginatedLeaguePlayerList
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    captain = True # bool | Is team captain (optional)
    discord_id = 56 # int | Discord ID of League Player (optional)
    franchise = 'franchise_example' # str | Name of franchise players are in. (optional)
    league = 56 # int | ID of League player is in. (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    name = 'name_example' # str | Player RSC Name Contains (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    season = 56 # int | ID of season players played in. (optional)
    season_number = 56 # int | Number of season players played in. (optional)
    status = 'status_example' # str | Player Status (Rostered, IR, etc.) (optional)
    sub_status = 56 # int | Player current substitution status. (optional)
    team_name = 'team_name_example' # str | Name of team players are on. (optional)
    tier = 56 # int | ID of Tier players are in. (optional)
    tier_name = 'tier_name_example' # str | Name of tier players are in. (optional)

    try:
        api_response = await api_instance.league_players_list(captain=captain, discord_id=discord_id, franchise=franchise, league=league, limit=limit, name=name, offset=offset, season=season, season_number=season_number, status=status, sub_status=sub_status, team_name=team_name, tier=tier, tier_name=tier_name)
        print("The response of LeaguePlayersApi->league_players_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **captain** | **bool**| Is team captain | [optional] 
 **discord_id** | **int**| Discord ID of League Player | [optional] 
 **franchise** | **str**| Name of franchise players are in. | [optional] 
 **league** | **int**| ID of League player is in. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**| Player RSC Name Contains | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **season** | **int**| ID of season players played in. | [optional] 
 **season_number** | **int**| Number of season players played in. | [optional] 
 **status** | **str**| Player Status (Rostered, IR, etc.) | [optional] 
 **sub_status** | **int**| Player current substitution status. | [optional] 
 **team_name** | **str**| Name of team players are on. | [optional] 
 **tier** | **int**| ID of Tier players are in. | [optional] 
 **tier_name** | **str**| Name of tier players are in. | [optional] 

### Return type

[**PaginatedLeaguePlayerList**](PaginatedLeaguePlayerList.md)

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
> LeaguePlayer league_players_partial_update(id, league=league, patched_league_player_patch=patched_league_player_patch)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
from rscapi.models.patched_league_player_patch import PatchedLeaguePlayerPatch
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.
    league = 56 # int | ID of league to update player in (optional)
    patched_league_player_patch = rscapi.PatchedLeaguePlayerPatch() # PatchedLeaguePlayerPatch |  (optional)

    try:
        api_response = await api_instance.league_players_partial_update(id, league=league, patched_league_player_patch=patched_league_player_patch)
        print("The response of LeaguePlayersApi->league_players_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league player. | 
 **league** | **int**| ID of league to update player in | [optional] 
 **patched_league_player_patch** | [**PatchedLeaguePlayerPatch**](PatchedLeaguePlayerPatch.md)|  | [optional] 

### Return type

[**LeaguePlayer**](LeaguePlayer.md)

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

# **league_players_postseason_stats_retrieve**
> PlayerSeasonStats league_players_postseason_stats_retrieve(id)

Get postseason stats for a specific league player.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_season_stats import PlayerSeasonStats
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.

    try:
        api_response = await api_instance.league_players_postseason_stats_retrieve(id)
        print("The response of LeaguePlayersApi->league_players_postseason_stats_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_postseason_stats_retrieve: %s\n" % e)
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

# **league_players_retrieve**
> LeaguePlayer league_players_retrieve(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.

    try:
        api_response = await api_instance.league_players_retrieve(id)
        print("The response of LeaguePlayersApi->league_players_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_retrieve: %s\n" % e)
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

# **league_players_set_captain_create**
> LeaguePlayer league_players_set_captain_create(id)

Set (Or unset) a player to be captain of their team.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.

    try:
        api_response = await api_instance.league_players_set_captain_create(id)
        print("The response of LeaguePlayersApi->league_players_set_captain_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_set_captain_create: %s\n" % e)
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
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **league_players_stats_retrieve**
> PlayerSeasonStats league_players_stats_retrieve(id)

Get stats for a specific league player.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_season_stats import PlayerSeasonStats
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.

    try:
        api_response = await api_instance.league_players_stats_retrieve(id)
        print("The response of LeaguePlayersApi->league_players_stats_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_stats_retrieve: %s\n" % e)
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
> LeaguePlayer league_players_update(id, league_player)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
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
    api_instance = rscapi.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.
    league_player = rscapi.LeaguePlayer() # LeaguePlayer | 

    try:
        api_response = await api_instance.league_players_update(id, league_player)
        print("The response of LeaguePlayersApi->league_players_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league player. | 
 **league_player** | [**LeaguePlayer**](LeaguePlayer.md)|  | 

### Return type

[**LeaguePlayer**](LeaguePlayer.md)

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


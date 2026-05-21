# rscapi.TeamsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_create**](TeamsApi.md#teams_create) | **POST** /teams/ | 
[**teams_destroy**](TeamsApi.md#teams_destroy) | **DELETE** /teams/{id}/ | 
[**teams_list**](TeamsApi.md#teams_list) | **GET** /teams/ | 
[**teams_match_retrieve**](TeamsApi.md#teams_match_retrieve) | **GET** /teams/{id}/match/ | 
[**teams_next_match_retrieve**](TeamsApi.md#teams_next_match_retrieve) | **GET** /teams/{id}/next_match/ | 
[**teams_partial_update**](TeamsApi.md#teams_partial_update) | **PATCH** /teams/{id}/ | 
[**teams_player_stats_list**](TeamsApi.md#teams_player_stats_list) | **GET** /teams/{id}/player_stats/ | 
[**teams_players_list**](TeamsApi.md#teams_players_list) | **GET** /teams/{id}/players/ | 
[**teams_postseason_stats_retrieve**](TeamsApi.md#teams_postseason_stats_retrieve) | **GET** /teams/{id}/postseason_stats/ | 
[**teams_retrieve**](TeamsApi.md#teams_retrieve) | **GET** /teams/{id}/ | 
[**teams_season_matches_list**](TeamsApi.md#teams_season_matches_list) | **GET** /teams/{id}/season_matches/ | 
[**teams_stats_retrieve**](TeamsApi.md#teams_stats_retrieve) | **GET** /teams/{id}/stats/ | 
[**teams_update**](TeamsApi.md#teams_update) | **PUT** /teams/{id}/ | 


# **teams_create**
> TeamCreate teams_create(team_create)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.team_create import TeamCreate
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
    api_instance = rscapi.TeamsApi(api_client)
    team_create = rscapi.TeamCreate() # TeamCreate | 

    try:
        api_response = await api_instance.teams_create(team_create)
        print("The response of TeamsApi->teams_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_create** | [**TeamCreate**](TeamCreate.md)|  | 

### Return type

[**TeamCreate**](TeamCreate.md)

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

# **teams_destroy**
> teams_destroy(id)

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
    api_instance = rscapi.TeamsApi(api_client)
    id = 56 # int | A unique integer value identifying this team.

    try:
        await api_instance.teams_destroy(id)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this team. | 

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

# **teams_list**
> List[TeamList] teams_list(franchise=franchise, league=league, name=name, seasons=seasons, tier=tier)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.team_list import TeamList
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
    api_instance = rscapi.TeamsApi(api_client)
    franchise = 'franchise_example' # str | Franchise Name Contains (optional)
    league = 56 # int | League Database ID (optional)
    name = 'name_example' # str | Team Name Contains (optional)
    seasons = [56] # List[int] | Season Number contains (optional)
    tier = 'tier_example' # str | Tier Name Contains (optional)

    try:
        api_response = await api_instance.teams_list(franchise=franchise, league=league, name=name, seasons=seasons, tier=tier)
        print("The response of TeamsApi->teams_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **franchise** | **str**| Franchise Name Contains | [optional] 
 **league** | **int**| League Database ID | [optional] 
 **name** | **str**| Team Name Contains | [optional] 
 **seasons** | [**List[int]**](int.md)| Season Number contains | [optional] 
 **tier** | **str**| Tier Name Contains | [optional] 

### Return type

[**List[TeamList]**](TeamList.md)

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

# **teams_match_retrieve**
> Match teams_match_retrieve(day, id, preseason=preseason, season_number=season_number)

Get a match details for a specific day for the given team

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.match import Match
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
    api_instance = rscapi.TeamsApi(api_client)
    day = 56 # int | 
    id = 56 # int | A unique integer value identifying this team.
    preseason = False # bool |  (optional) (default to False)
    season_number = 56 # int |  (optional)

    try:
        api_response = await api_instance.teams_match_retrieve(day, id, preseason=preseason, season_number=season_number)
        print("The response of TeamsApi->teams_match_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_match_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **day** | **int**|  | 
 **id** | **int**| A unique integer value identifying this team. | 
 **preseason** | **bool**|  | [optional] [default to False]
 **season_number** | **int**|  | [optional] 

### Return type

[**Match**](Match.md)

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
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_next_match_retrieve**
> Match teams_next_match_retrieve(id)

Get the next match for a given team

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.match import Match
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
    api_instance = rscapi.TeamsApi(api_client)
    id = 56 # int | A unique integer value identifying this team.

    try:
        api_response = await api_instance.teams_next_match_retrieve(id)
        print("The response of TeamsApi->teams_next_match_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_next_match_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this team. | 

### Return type

[**Match**](Match.md)

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

# **teams_partial_update**
> TeamList teams_partial_update(id, patched_team_list=patched_team_list)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.patched_team_list import PatchedTeamList
from rscapi.models.team_list import TeamList
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
    api_instance = rscapi.TeamsApi(api_client)
    id = 56 # int | A unique integer value identifying this team.
    patched_team_list = rscapi.PatchedTeamList() # PatchedTeamList |  (optional)

    try:
        api_response = await api_instance.teams_partial_update(id, patched_team_list=patched_team_list)
        print("The response of TeamsApi->teams_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this team. | 
 **patched_team_list** | [**PatchedTeamList**](PatchedTeamList.md)|  | [optional] 

### Return type

[**TeamList**](TeamList.md)

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

# **teams_player_stats_list**
> List[PlayerSeasonStatsInDepth] teams_player_stats_list(id, franchise=franchise, league=league, name=name, season_id=season_id, season_number=season_number, seasons=seasons, tier=tier)

Get player stats for a given team. (Default: Current Season)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_season_stats_in_depth import PlayerSeasonStatsInDepth
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
    api_instance = rscapi.TeamsApi(api_client)
    id = 56 # int | A unique integer value identifying this team.
    franchise = 'franchise_example' # str | Franchise Name Contains (optional)
    league = 3.4 # float | League ID (optional)
    name = 'name_example' # str | Team Name Contains (optional)
    season_id = 56 # int | Season database ID to query for. (optional)
    season_number = 56 # int | Season number to query for. Defaults to the league current season when omitted. (optional)
    seasons = [56] # List[int] | Season Number contains (optional)
    tier = 'tier_example' # str | Tier Name Contains (optional)

    try:
        api_response = await api_instance.teams_player_stats_list(id, franchise=franchise, league=league, name=name, season_id=season_id, season_number=season_number, seasons=seasons, tier=tier)
        print("The response of TeamsApi->teams_player_stats_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_player_stats_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this team. | 
 **franchise** | **str**| Franchise Name Contains | [optional] 
 **league** | **float**| League ID | [optional] 
 **name** | **str**| Team Name Contains | [optional] 
 **season_id** | **int**| Season database ID to query for. | [optional] 
 **season_number** | **int**| Season number to query for. Defaults to the league current season when omitted. | [optional] 
 **seasons** | [**List[int]**](int.md)| Season Number contains | [optional] 
 **tier** | **str**| Tier Name Contains | [optional] 

### Return type

[**List[PlayerSeasonStatsInDepth]**](PlayerSeasonStatsInDepth.md)

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

# **teams_players_list**
> List[TeamPlayer] teams_players_list(id, franchise=franchise, league=league, name=name, seasons=seasons, tier=tier)

Get the players for a given team.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.team_player import TeamPlayer
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
    api_instance = rscapi.TeamsApi(api_client)
    id = 56 # int | A unique integer value identifying this team.
    franchise = 'franchise_example' # str | Franchise Name Contains (optional)
    league = 3.4 # float | League ID (optional)
    name = 'name_example' # str | Team Name Contains (optional)
    seasons = [56] # List[int] | Season Number contains (optional)
    tier = 'tier_example' # str | Tier Name Contains (optional)

    try:
        api_response = await api_instance.teams_players_list(id, franchise=franchise, league=league, name=name, seasons=seasons, tier=tier)
        print("The response of TeamsApi->teams_players_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_players_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this team. | 
 **franchise** | **str**| Franchise Name Contains | [optional] 
 **league** | **float**| League ID | [optional] 
 **name** | **str**| Team Name Contains | [optional] 
 **seasons** | [**List[int]**](int.md)| Season Number contains | [optional] 
 **tier** | **str**| Tier Name Contains | [optional] 

### Return type

[**List[TeamPlayer]**](TeamPlayer.md)

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

# **teams_postseason_stats_retrieve**
> TeamSeasonStats teams_postseason_stats_retrieve(id, season_id=season_id, season_number=season_number)

Get postseason stats for a given team. (Default: Current Season)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.team_season_stats import TeamSeasonStats
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
    api_instance = rscapi.TeamsApi(api_client)
    id = 56 # int | A unique integer value identifying this team.
    season_id = 56 # int | Season database ID to query for. (optional)
    season_number = 56 # int | Season number to query for. Defaults to the league current season when omitted. (optional)

    try:
        api_response = await api_instance.teams_postseason_stats_retrieve(id, season_id=season_id, season_number=season_number)
        print("The response of TeamsApi->teams_postseason_stats_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_postseason_stats_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this team. | 
 **season_id** | **int**| Season database ID to query for. | [optional] 
 **season_number** | **int**| Season number to query for. Defaults to the league current season when omitted. | [optional] 

### Return type

[**TeamSeasonStats**](TeamSeasonStats.md)

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

# **teams_retrieve**
> Team teams_retrieve(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.team import Team
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
    api_instance = rscapi.TeamsApi(api_client)
    id = 56 # int | A unique integer value identifying this team.

    try:
        api_response = await api_instance.teams_retrieve(id)
        print("The response of TeamsApi->teams_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this team. | 

### Return type

[**Team**](Team.md)

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

# **teams_season_matches_list**
> List[HighLevelMatch] teams_season_matches_list(id, franchise=franchise, league=league, name=name, preseason=preseason, season=season, seasons=seasons, tier=tier)

Get all matches for a given team.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.high_level_match import HighLevelMatch
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
    api_instance = rscapi.TeamsApi(api_client)
    id = 56 # int | A unique integer value identifying this team.
    franchise = 'franchise_example' # str | Franchise Name Contains (optional)
    league = 3.4 # float | League ID (optional)
    name = 'name_example' # str | Team Name Contains (optional)
    preseason = True # bool |  (optional)
    season = 56 # int |  (optional)
    seasons = [56] # List[int] | Season Number contains (optional)
    tier = 'tier_example' # str | Tier Name Contains (optional)

    try:
        api_response = await api_instance.teams_season_matches_list(id, franchise=franchise, league=league, name=name, preseason=preseason, season=season, seasons=seasons, tier=tier)
        print("The response of TeamsApi->teams_season_matches_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_season_matches_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this team. | 
 **franchise** | **str**| Franchise Name Contains | [optional] 
 **league** | **float**| League ID | [optional] 
 **name** | **str**| Team Name Contains | [optional] 
 **preseason** | **bool**|  | [optional] 
 **season** | **int**|  | [optional] 
 **seasons** | [**List[int]**](int.md)| Season Number contains | [optional] 
 **tier** | **str**| Tier Name Contains | [optional] 

### Return type

[**List[HighLevelMatch]**](HighLevelMatch.md)

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

# **teams_stats_retrieve**
> TeamSeasonStats teams_stats_retrieve(id, season_id=season_id, season_number=season_number)

Get regular season stats for a given team. (Default: Current Season)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.team_season_stats import TeamSeasonStats
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
    api_instance = rscapi.TeamsApi(api_client)
    id = 56 # int | A unique integer value identifying this team.
    season_id = 56 # int | Season database ID to query for. (optional)
    season_number = 56 # int | Season number to query for. Defaults to the league current season when omitted. (optional)

    try:
        api_response = await api_instance.teams_stats_retrieve(id, season_id=season_id, season_number=season_number)
        print("The response of TeamsApi->teams_stats_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_stats_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this team. | 
 **season_id** | **int**| Season database ID to query for. | [optional] 
 **season_number** | **int**| Season number to query for. Defaults to the league current season when omitted. | [optional] 

### Return type

[**TeamSeasonStats**](TeamSeasonStats.md)

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

# **teams_update**
> teams_update(id, team_patch)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.team_patch import TeamPatch
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
    api_instance = rscapi.TeamsApi(api_client)
    id = 56 # int | A unique integer value identifying this team.
    team_patch = rscapi.TeamPatch() # TeamPatch | 

    try:
        await api_instance.teams_update(id, team_patch)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this team. | 
 **team_patch** | [**TeamPatch**](TeamPatch.md)|  | 

### Return type

void (empty response body)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


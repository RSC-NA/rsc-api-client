# rscapi.TiersApi

All URIs are relative to *https://api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tiers_list**](TiersApi.md#tiers_list) | **GET** /tiers/ | 
[**tiers_player_stats**](TiersApi.md#tiers_player_stats) | **GET** /tiers/{id}/player_stats/ | 
[**tiers_players**](TiersApi.md#tiers_players) | **GET** /tiers/{id}/players/ | 
[**tiers_postseason_player_stats**](TiersApi.md#tiers_postseason_player_stats) | **GET** /tiers/{id}/postseason_player_stats/ | 
[**tiers_postseason_team_stats**](TiersApi.md#tiers_postseason_team_stats) | **GET** /tiers/{id}/postseason_team_stats/ | 
[**tiers_read**](TiersApi.md#tiers_read) | **GET** /tiers/{id}/ | 
[**tiers_team_stats**](TiersApi.md#tiers_team_stats) | **GET** /tiers/{id}/team_stats/ | 
[**tiers_teams**](TiersApi.md#tiers_teams) | **GET** /tiers/{id}/teams/ | 


# **tiers_list**
> List[Tier] tiers_list(name=name, league=league)

Viewset for the Tier model.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tier import Tier
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
    api_instance = rscapi.TiersApi(api_client)
    name = 'name_example' # str | name (optional)
    league = 56 # int | League Database ID (optional)

    try:
        api_response = await api_instance.tiers_list(name=name, league=league)
        print("The response of TiersApi->tiers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | [optional] 
 **league** | **int**| League Database ID | [optional] 

### Return type

[**List[Tier]**](Tier.md)

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

# **tiers_player_stats**
> List[PlayerSeasonStatsInDepth] tiers_player_stats(id, league, season=season)

Get player stats for a given tier and season in a league. (Default: Current Season)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_season_stats_in_depth import PlayerSeasonStatsInDepth
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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    league = 56 # int | League ID
    season = 56 # int | Season number (Default: Current season.) (optional)

    try:
        api_response = await api_instance.tiers_player_stats(id, league, season=season)
        print("The response of TiersApi->tiers_player_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_player_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **league** | **int**| League ID | 
 **season** | **int**| Season number (Default: Current season.) | [optional] 

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

# **tiers_players**
> List[LeaguePlayer] tiers_players(id, league, season=season)

Get all players for a specific tier in a league

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    league = 56 # int | League ID
    season = 56 # int | Season number (Default: Current season.) (optional)

    try:
        api_response = await api_instance.tiers_players(id, league, season=season)
        print("The response of TiersApi->tiers_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_players: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **league** | **int**| League ID | 
 **season** | **int**| Season number (Default: Current season.) | [optional] 

### Return type

[**List[LeaguePlayer]**](LeaguePlayer.md)

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

# **tiers_postseason_player_stats**
> List[PlayerSeasonStatsInDepth] tiers_postseason_player_stats(id, league, season=season)

Get player postseason stats for a given tier and season in a league

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_season_stats_in_depth import PlayerSeasonStatsInDepth
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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    league = 56 # int | League ID
    season = 56 # int | Season number (Default: Current season.) (optional)

    try:
        api_response = await api_instance.tiers_postseason_player_stats(id, league, season=season)
        print("The response of TiersApi->tiers_postseason_player_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_postseason_player_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **league** | **int**| League ID | 
 **season** | **int**| Season number (Default: Current season.) | [optional] 

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

# **tiers_postseason_team_stats**
> List[TeamSeasonStats] tiers_postseason_team_stats(id, league, season=season)

Get postseason team stats for a given tier and season in a league. (Default: Current)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.team_season_stats import TeamSeasonStats
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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    league = 56 # int | League ID
    season = 56 # int | Season number (Default: Current season.) (optional)

    try:
        api_response = await api_instance.tiers_postseason_team_stats(id, league, season=season)
        print("The response of TiersApi->tiers_postseason_team_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_postseason_team_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **league** | **int**| League ID | 
 **season** | **int**| Season number (Default: Current season.) | [optional] 

### Return type

[**List[TeamSeasonStats]**](TeamSeasonStats.md)

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

# **tiers_read**
> Tier tiers_read(id)

Viewset for the Tier model.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tier import Tier
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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.

    try:
        api_response = await api_instance.tiers_read(id)
        print("The response of TiersApi->tiers_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 

### Return type

[**Tier**](Tier.md)

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

# **tiers_team_stats**
> List[TeamSeasonStats] tiers_team_stats(id, league, season=season)

Get team based stats for a given tier and season in a league. (Default: Current)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.team_season_stats import TeamSeasonStats
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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    league = 56 # int | League ID
    season = 56 # int | Season number (Default: Current season.) (optional)

    try:
        api_response = await api_instance.tiers_team_stats(id, league, season=season)
        print("The response of TiersApi->tiers_team_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_team_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **league** | **int**| League ID | 
 **season** | **int**| Season number (Default: Current season.) | [optional] 

### Return type

[**List[TeamSeasonStats]**](TeamSeasonStats.md)

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

# **tiers_teams**
> List[Team] tiers_teams(id, league, season=season)

Get all teams for a specific tier in a league.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.team import Team
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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    league = 56 # int | League ID
    season = 56 # int | Season number (Default: Current season.) (optional)

    try:
        api_response = await api_instance.tiers_teams(id, league, season=season)
        print("The response of TiersApi->tiers_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **league** | **int**| League ID | 
 **season** | **int**| Season number (Default: Current season.) | [optional] 

### Return type

[**List[Team]**](Team.md)

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


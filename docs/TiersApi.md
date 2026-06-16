# rscapi.TiersApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tiers_create**](TiersApi.md#tiers_create) | **POST** /tiers/ | 
[**tiers_destroy**](TiersApi.md#tiers_destroy) | **DELETE** /tiers/{id}/ | 
[**tiers_list**](TiersApi.md#tiers_list) | **GET** /tiers/ | 
[**tiers_partial_update**](TiersApi.md#tiers_partial_update) | **PATCH** /tiers/{id}/ | 
[**tiers_player_stats_list**](TiersApi.md#tiers_player_stats_list) | **GET** /tiers/{id}/player_stats/ | 
[**tiers_players_list**](TiersApi.md#tiers_players_list) | **GET** /tiers/{id}/players/ | 
[**tiers_playoffs_retrieve**](TiersApi.md#tiers_playoffs_retrieve) | **GET** /tiers/{id}/playoffs/ | 
[**tiers_postseason_player_stats_list**](TiersApi.md#tiers_postseason_player_stats_list) | **GET** /tiers/{id}/postseason_player_stats/ | 
[**tiers_postseason_team_stats_list**](TiersApi.md#tiers_postseason_team_stats_list) | **GET** /tiers/{id}/postseason_team_stats/ | 
[**tiers_retrieve**](TiersApi.md#tiers_retrieve) | **GET** /tiers/{id}/ | 
[**tiers_standings_list**](TiersApi.md#tiers_standings_list) | **GET** /tiers/{id}/standings/ | 
[**tiers_team_stats_list**](TiersApi.md#tiers_team_stats_list) | **GET** /tiers/{id}/team_stats/ | 
[**tiers_teams_list**](TiersApi.md#tiers_teams_list) | **GET** /tiers/{id}/teams/ | 
[**tiers_update**](TiersApi.md#tiers_update) | **PUT** /tiers/{id}/ | 


# **tiers_create**
> Tier tiers_create(tier)

Viewset for the Tier model.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tier import Tier
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
    api_instance = rscapi.TiersApi(api_client)
    tier = rscapi.Tier() # Tier | 

    try:
        api_response = await api_instance.tiers_create(tier)
        print("The response of TiersApi->tiers_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tier** | [**Tier**](Tier.md)|  | 

### Return type

[**Tier**](Tier.md)

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

# **tiers_destroy**
> tiers_destroy(id)

Viewset for the Tier model.

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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.

    try:
        await api_instance.tiers_destroy(id)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 

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

# **tiers_list**
> List[Tier] tiers_list(league=league, name=name)

Viewset for the Tier model.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tier import Tier
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
    api_instance = rscapi.TiersApi(api_client)
    league = 56 # int | League Database ID (optional)
    name = 'name_example' # str | Tier Name Contains (optional)

    try:
        api_response = await api_instance.tiers_list(league=league, name=name)
        print("The response of TiersApi->tiers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league** | **int**| League Database ID | [optional] 
 **name** | **str**| Tier Name Contains | [optional] 

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

# **tiers_partial_update**
> Tier tiers_partial_update(id, patched_tier=patched_tier)

Viewset for the Tier model.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.patched_tier import PatchedTier
from rscapi.models.tier import Tier
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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    patched_tier = rscapi.PatchedTier() # PatchedTier |  (optional)

    try:
        api_response = await api_instance.tiers_partial_update(id, patched_tier=patched_tier)
        print("The response of TiersApi->tiers_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **patched_tier** | [**PatchedTier**](PatchedTier.md)|  | [optional] 

### Return type

[**Tier**](Tier.md)

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

# **tiers_player_stats_list**
> List[PlayerSeasonStatsInDepth] tiers_player_stats_list(id, league, name=name, season=season)

Get player stats for a given tier and season in a league. (Default: Current Season)

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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    league = 56 # int | League ID
    name = 'name_example' # str | Tier Name Contains (optional)
    season = 56 # int | Season number (Default: Current season.) (optional)

    try:
        api_response = await api_instance.tiers_player_stats_list(id, league, name=name, season=season)
        print("The response of TiersApi->tiers_player_stats_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_player_stats_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **league** | **int**| League ID | 
 **name** | **str**| Tier Name Contains | [optional] 
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

# **tiers_players_list**
> List[LeaguePlayer] tiers_players_list(id, league, name=name, season=season)

Get all players for a specific tier in a league

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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    league = 56 # int | League ID
    name = 'name_example' # str | Tier Name Contains (optional)
    season = 56 # int | Season number (Default: Current season.) (optional)

    try:
        api_response = await api_instance.tiers_players_list(id, league, name=name, season=season)
        print("The response of TiersApi->tiers_players_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_players_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **league** | **int**| League ID | 
 **name** | **str**| Tier Name Contains | [optional] 
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

# **tiers_playoffs_retrieve**
> TierPlayoffHunt tiers_playoffs_retrieve(id, league, season=season)

Get the current playoff hunt for a specific tier in a league and season.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tier_playoff_hunt import TierPlayoffHunt
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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    league = 56 # int | League ID
    season = 56 # int | Season number (Default: Current season.) (optional)

    try:
        api_response = await api_instance.tiers_playoffs_retrieve(id, league, season=season)
        print("The response of TiersApi->tiers_playoffs_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_playoffs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **league** | **int**| League ID | 
 **season** | **int**| Season number (Default: Current season.) | [optional] 

### Return type

[**TierPlayoffHunt**](TierPlayoffHunt.md)

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

# **tiers_postseason_player_stats_list**
> List[PlayerSeasonStatsInDepth] tiers_postseason_player_stats_list(id, league, name=name, season=season)

Get player postseason stats for a given tier and season in a league

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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    league = 56 # int | League ID
    name = 'name_example' # str | Tier Name Contains (optional)
    season = 56 # int | Season number (Default: Current season.) (optional)

    try:
        api_response = await api_instance.tiers_postseason_player_stats_list(id, league, name=name, season=season)
        print("The response of TiersApi->tiers_postseason_player_stats_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_postseason_player_stats_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **league** | **int**| League ID | 
 **name** | **str**| Tier Name Contains | [optional] 
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

# **tiers_postseason_team_stats_list**
> List[TeamSeasonStats] tiers_postseason_team_stats_list(id, league, name=name, season=season)

Get postseason team stats for a given tier and season in a league. (Default: Current)

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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    league = 56 # int | League ID
    name = 'name_example' # str | Tier Name Contains (optional)
    season = 56 # int | Season number (Default: Current season.) (optional)

    try:
        api_response = await api_instance.tiers_postseason_team_stats_list(id, league, name=name, season=season)
        print("The response of TiersApi->tiers_postseason_team_stats_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_postseason_team_stats_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **league** | **int**| League ID | 
 **name** | **str**| Tier Name Contains | [optional] 
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

# **tiers_retrieve**
> Tier tiers_retrieve(id)

Viewset for the Tier model.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tier import Tier
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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.

    try:
        api_response = await api_instance.tiers_retrieve(id)
        print("The response of TiersApi->tiers_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_retrieve: %s\n" % e)
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

# **tiers_standings_list**
> List[TeamStandings] tiers_standings_list(id, season, league=league, name=name)

Get standings for a specific tier in a league and season.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.team_standings import TeamStandings
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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    season = 56 # int | Season number to query for.
    league = 56 # int | Tiers in League with ID (optional)
    name = 'name_example' # str | Tier Name Contains (optional)

    try:
        api_response = await api_instance.tiers_standings_list(id, season, league=league, name=name)
        print("The response of TiersApi->tiers_standings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_standings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **season** | **int**| Season number to query for. | 
 **league** | **int**| Tiers in League with ID | [optional] 
 **name** | **str**| Tier Name Contains | [optional] 

### Return type

[**List[TeamStandings]**](TeamStandings.md)

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

# **tiers_team_stats_list**
> List[TeamSeasonStats] tiers_team_stats_list(id, league, name=name, season=season)

Get team based stats for a given tier and season in a league. (Default: Current)

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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    league = 56 # int | League ID
    name = 'name_example' # str | Tier Name Contains (optional)
    season = 56 # int | Season number (Default: Current season.) (optional)

    try:
        api_response = await api_instance.tiers_team_stats_list(id, league, name=name, season=season)
        print("The response of TiersApi->tiers_team_stats_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_team_stats_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **league** | **int**| League ID | 
 **name** | **str**| Tier Name Contains | [optional] 
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

# **tiers_teams_list**
> List[Team] tiers_teams_list(id, league, name=name, season=season)

Get all teams for a specific tier in a league.

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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    league = 56 # int | League ID
    name = 'name_example' # str | Tier Name Contains (optional)
    season = 56 # int | Season number (Default: Current season.) (optional)

    try:
        api_response = await api_instance.tiers_teams_list(id, league, name=name, season=season)
        print("The response of TiersApi->tiers_teams_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_teams_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **league** | **int**| League ID | 
 **name** | **str**| Tier Name Contains | [optional] 
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

# **tiers_update**
> Tier tiers_update(id, tier)

Viewset for the Tier model.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tier import Tier
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
    api_instance = rscapi.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    tier = rscapi.Tier() # Tier | 

    try:
        api_response = await api_instance.tiers_update(id, tier)
        print("The response of TiersApi->tiers_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **tier** | [**Tier**](Tier.md)|  | 

### Return type

[**Tier**](Tier.md)

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


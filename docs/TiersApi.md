# openapi_client.TiersApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tiers_create**](TiersApi.md#tiers_create) | **POST** /tiers/ | 
[**tiers_delete**](TiersApi.md#tiers_delete) | **DELETE** /tiers/{id}/ | 
[**tiers_list**](TiersApi.md#tiers_list) | **GET** /tiers/ | 
[**tiers_partial_update**](TiersApi.md#tiers_partial_update) | **PATCH** /tiers/{id}/ | 
[**tiers_player_stats**](TiersApi.md#tiers_player_stats) | **GET** /tiers/{id}/player_stats/ | 
[**tiers_players**](TiersApi.md#tiers_players) | **GET** /tiers/{id}/players/ | 
[**tiers_postseason_player_stats**](TiersApi.md#tiers_postseason_player_stats) | **GET** /tiers/{id}/postseason_player_stats/ | 
[**tiers_postseason_team_stats**](TiersApi.md#tiers_postseason_team_stats) | **GET** /tiers/{id}/postseason_team_stats/ | 
[**tiers_read**](TiersApi.md#tiers_read) | **GET** /tiers/{id}/ | 
[**tiers_team_stats**](TiersApi.md#tiers_team_stats) | **GET** /tiers/{id}/team_stats/ | 
[**tiers_teams**](TiersApi.md#tiers_teams) | **GET** /tiers/{id}/teams/ | 
[**tiers_update**](TiersApi.md#tiers_update) | **PUT** /tiers/{id}/ | 


# **tiers_create**
> Tier tiers_create(data)



Viewset for the Tier model.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.tier import Tier
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging-api.rscna.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TiersApi(api_client)
    data = openapi_client.Tier() # Tier | 

    try:
        api_response = await api_instance.tiers_create(data)
        print("The response of TiersApi->tiers_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Tier**](Tier.md)|  | 

### Return type

[**Tier**](Tier.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tiers_delete**
> tiers_delete(id)



Viewset for the Tier model.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging-api.rscna.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.

    try:
        await api_instance.tiers_delete(id)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tiers_list**
> List[Tier] tiers_list(name=name, league=league)



Viewset for the Tier model.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.tier import Tier
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging-api.rscna.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TiersApi(api_client)
    name = 'name_example' # str | name (optional)
    league = 'league_example' # str | league (optional)

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
 **league** | **str**| league | [optional] 

### Return type

[**List[Tier]**](Tier.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tiers_partial_update**
> Tier tiers_partial_update(id, data)



Viewset for the Tier model.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.tier import Tier
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging-api.rscna.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    data = openapi_client.Tier() # Tier | 

    try:
        api_response = await api_instance.tiers_partial_update(id, data)
        print("The response of TiersApi->tiers_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **data** | [**Tier**](Tier.md)|  | 

### Return type

[**Tier**](Tier.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
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

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.player_season_stats_in_depth import PlayerSeasonStatsInDepth
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging-api.rscna.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TiersApi(api_client)
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tiers_players**
> List[LeaguePlayer] tiers_players(id, league, season=season)



Get all players for a specific tier in a league

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.league_player import LeaguePlayer
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging-api.rscna.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TiersApi(api_client)
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tiers_postseason_player_stats**
> List[PlayerSeasonStatsInDepth] tiers_postseason_player_stats(id, league, season=season)



Get player postseason stats for a given tier and season in a league. (Default: Current Season)

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.player_season_stats_in_depth import PlayerSeasonStatsInDepth
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging-api.rscna.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TiersApi(api_client)
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tiers_postseason_team_stats**
> List[TeamSeasonStats] tiers_postseason_team_stats(id, league, season=season)



Get postseason team stats for a given tier and season in a league. (Default: Current Season)

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.team_season_stats import TeamSeasonStats
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging-api.rscna.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TiersApi(api_client)
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tiers_read**
> Tier tiers_read(id)



Viewset for the Tier model.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.tier import Tier
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging-api.rscna.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TiersApi(api_client)
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

[api_key](../README.md#api_key)

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



Get team based stats for a given tier and season in a league. (Default: Current Season)

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.team_season_stats import TeamSeasonStats
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging-api.rscna.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TiersApi(api_client)
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tiers_teams**
> List[Team] tiers_teams(id, league, season=season)



Get all teams for a specific tier in a league.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.team import Team
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging-api.rscna.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TiersApi(api_client)
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tiers_update**
> Tier tiers_update(id, data)



Viewset for the Tier model.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.tier import Tier
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging-api.rscna.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TiersApi(api_client)
    id = 56 # int | A unique integer value identifying this tier.
    data = openapi_client.Tier() # Tier | 

    try:
        api_response = await api_instance.tiers_update(id, data)
        print("The response of TiersApi->tiers_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiersApi->tiers_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tier. | 
 **data** | [**Tier**](Tier.md)|  | 

### Return type

[**Tier**](Tier.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


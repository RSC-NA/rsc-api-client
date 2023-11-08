# rscapi.TeamsApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_list**](TeamsApi.md#teams_list) | **GET** /teams/ | 
[**teams_match**](TeamsApi.md#teams_match) | **GET** /teams/{id}/match/ | 
[**teams_next_match**](TeamsApi.md#teams_next_match) | **GET** /teams/{id}/next_match/ | 
[**teams_players**](TeamsApi.md#teams_players) | **GET** /teams/{id}/players/ | 
[**teams_postseason_stats**](TeamsApi.md#teams_postseason_stats) | **GET** /teams/{id}/postseason_stats/ | 
[**teams_read**](TeamsApi.md#teams_read) | **GET** /teams/{id}/ | 
[**teams_season_matches**](TeamsApi.md#teams_season_matches) | **GET** /teams/{id}/season_matches/ | 
[**teams_stats**](TeamsApi.md#teams_stats) | **GET** /teams/{id}/stats/ | 


# **teams_list**
> List[TeamList] teams_list(seasons=seasons, franchise=franchise, name=name, tier=tier, league=league)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import rscapi
from rscapi.models.team_list import TeamList
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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with rscapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rscapi.TeamsApi(api_client)
    seasons = 'seasons_example' # str | seasons (optional)
    franchise = 'franchise_example' # str | franchise (optional)
    name = 'name_example' # str | name (optional)
    tier = 'tier_example' # str | tier (optional)
    league = 'league_example' # str | league (optional)

    try:
        api_response = await api_instance.teams_list(seasons=seasons, franchise=franchise, name=name, tier=tier, league=league)
        print("The response of TeamsApi->teams_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seasons** | **str**| seasons | [optional] 
 **franchise** | **str**| franchise | [optional] 
 **name** | **str**| name | [optional] 
 **tier** | **str**| tier | [optional] 
 **league** | **str**| league | [optional] 

### Return type

[**List[TeamList]**](TeamList.md)

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

# **teams_match**
> Match teams_match(id, day, preseason=preseason)



Get a match details for a specific day for the given team

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import rscapi
from rscapi.models.match import Match
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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with rscapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rscapi.TeamsApi(api_client)
    id = 'id_example' # str | 
    day = 56 # int | Match day to find
    preseason = 56 # int | 1 if this is a preseason match. (optional)

    try:
        api_response = await api_instance.teams_match(id, day, preseason=preseason)
        print("The response of TeamsApi->teams_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_match: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **day** | **int**| Match day to find | 
 **preseason** | **int**| 1 if this is a preseason match. | [optional] 

### Return type

[**Match**](Match.md)

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

# **teams_next_match**
> Match teams_next_match(id)



Get the next match for a given team

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import rscapi
from rscapi.models.match import Match
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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with rscapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rscapi.TeamsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.teams_next_match(id)
        print("The response of TeamsApi->teams_next_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_next_match: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Match**](Match.md)

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

# **teams_players**
> List[Player] teams_players(id)



Get the players for a given team.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import rscapi
from rscapi.models.player import Player
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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with rscapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rscapi.TeamsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.teams_players(id)
        print("The response of TeamsApi->teams_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_players: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[Player]**](Player.md)

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

# **teams_postseason_stats**
> TeamSeasonStats teams_postseason_stats(id, season=season)



Get postseason stats for a given team. (Default: Current Season)

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import rscapi
from rscapi.models.team_season_stats import TeamSeasonStats
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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with rscapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rscapi.TeamsApi(api_client)
    id = 'id_example' # str | 
    season = 56 # int | Specific season number to get stats for. (optional)

    try:
        api_response = await api_instance.teams_postseason_stats(id, season=season)
        print("The response of TeamsApi->teams_postseason_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_postseason_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **season** | **int**| Specific season number to get stats for. | [optional] 

### Return type

[**TeamSeasonStats**](TeamSeasonStats.md)

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

# **teams_read**
> Team teams_read(id)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import rscapi
from rscapi.models.team import Team
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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with rscapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rscapi.TeamsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.teams_read(id)
        print("The response of TeamsApi->teams_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_read: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Team**](Team.md)

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

# **teams_season_matches**
> List[Match] teams_season_matches(id, preseason=preseason, season=season)



Get all matches for a given team.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import rscapi
from rscapi.models.match import Match
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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with rscapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rscapi.TeamsApi(api_client)
    id = 'id_example' # str | 
    preseason = True # bool | If true, get preseason matches (Default: Regular) (optional)
    season = 56 # int | Season number to get matches for (Default: Current Season) (optional)

    try:
        api_response = await api_instance.teams_season_matches(id, preseason=preseason, season=season)
        print("The response of TeamsApi->teams_season_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_season_matches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **preseason** | **bool**| If true, get preseason matches (Default: Regular) | [optional] 
 **season** | **int**| Season number to get matches for (Default: Current Season) | [optional] 

### Return type

[**List[Match]**](Match.md)

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

# **teams_stats**
> TeamSeasonStats teams_stats(id, season=season)



Get regular season stats for a given team. (Default: Current Season)

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import rscapi
from rscapi.models.team_season_stats import TeamSeasonStats
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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with rscapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rscapi.TeamsApi(api_client)
    id = 'id_example' # str | 
    season = 56 # int | Specific season number to get stats for. (optional)

    try:
        api_response = await api_instance.teams_stats(id, season=season)
        print("The response of TeamsApi->teams_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **season** | **int**| Specific season number to get stats for. | [optional] 

### Return type

[**TeamSeasonStats**](TeamSeasonStats.md)

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


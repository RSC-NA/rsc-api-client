# openapi_client.LeaguePlayersApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**league_players_create**](LeaguePlayersApi.md#league_players_create) | **POST** /league-players/ | 
[**league_players_delete**](LeaguePlayersApi.md#league_players_delete) | **DELETE** /league-players/{id}/ | 
[**league_players_list**](LeaguePlayersApi.md#league_players_list) | **GET** /league-players/ | 
[**league_players_partial_update**](LeaguePlayersApi.md#league_players_partial_update) | **PATCH** /league-players/{id}/ | 
[**league_players_postseason_stats**](LeaguePlayersApi.md#league_players_postseason_stats) | **GET** /league-players/{id}/postseason_stats/ | 
[**league_players_read**](LeaguePlayersApi.md#league_players_read) | **GET** /league-players/{id}/ | 
[**league_players_set_captain**](LeaguePlayersApi.md#league_players_set_captain) | **PUT** /league-players/{id}/set_captain/ | 
[**league_players_stats**](LeaguePlayersApi.md#league_players_stats) | **GET** /league-players/{id}/stats/ | 
[**league_players_update**](LeaguePlayersApi.md#league_players_update) | **PUT** /league-players/{id}/ | 


# **league_players_create**
> LeaguePlayer league_players_create(data)



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
    api_instance = openapi_client.LeaguePlayersApi(api_client)
    data = openapi_client.LeaguePlayer() # LeaguePlayer | 

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

[api_key](../README.md#api_key)

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
    api_instance = openapi_client.LeaguePlayersApi(api_client)
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **league_players_list**
> LeaguePlayersList200Response league_players_list(status=status, name=name, tier=tier, tier_name=tier_name, season=season, season_number=season_number, league=league, team_name=team_name, limit=limit, offset=offset)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.league_players_list200_response import LeaguePlayersList200Response
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
    api_instance = openapi_client.LeaguePlayersApi(api_client)
    status = 'status_example' # str | Player Status (Rostered, IR, etc.) (optional)
    name = 'name_example' # str | name (optional)
    tier = 'tier_example' # str | tier (optional)
    tier_name = 'tier_name_example' # str | tier_name (optional)
    season = 'season_example' # str | season (optional)
    season_number = 'season_number_example' # str | season_number (optional)
    league = 'league_example' # str | league (optional)
    team_name = 'team_name_example' # str | team_name (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.league_players_list(status=status, name=name, tier=tier, tier_name=tier_name, season=season, season_number=season_number, league=league, team_name=team_name, limit=limit, offset=offset)
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
 **tier** | **str**| tier | [optional] 
 **tier_name** | **str**| tier_name | [optional] 
 **season** | **str**| season | [optional] 
 **season_number** | **str**| season_number | [optional] 
 **league** | **str**| league | [optional] 
 **team_name** | **str**| team_name | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**LeaguePlayersList200Response**](LeaguePlayersList200Response.md)

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

# **league_players_partial_update**
> LeaguePlayer league_players_partial_update(id, data)



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
    api_instance = openapi_client.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.
    data = openapi_client.LeaguePlayer() # LeaguePlayer | 

    try:
        api_response = await api_instance.league_players_partial_update(id, data)
        print("The response of LeaguePlayersApi->league_players_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league player. | 
 **data** | [**LeaguePlayer**](LeaguePlayer.md)|  | 

### Return type

[**LeaguePlayer**](LeaguePlayer.md)

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

# **league_players_postseason_stats**
> PlayerSeasonStats league_players_postseason_stats(id)



Get postseason stats for a specific league player.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.player_season_stats import PlayerSeasonStats
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
    api_instance = openapi_client.LeaguePlayersApi(api_client)
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **league_players_read**
> LeaguePlayer league_players_read(id)



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
    api_instance = openapi_client.LeaguePlayersApi(api_client)
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **league_players_set_captain**
> LeaguePlayer league_players_set_captain(id, data)



Set (Or unset) a player to be captain of their team.

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
    api_instance = openapi_client.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.
    data = openapi_client.LeaguePlayer() # LeaguePlayer | 

    try:
        api_response = await api_instance.league_players_set_captain(id, data)
        print("The response of LeaguePlayersApi->league_players_set_captain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaguePlayersApi->league_players_set_captain: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league player. | 
 **data** | [**LeaguePlayer**](LeaguePlayer.md)|  | 

### Return type

[**LeaguePlayer**](LeaguePlayer.md)

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

# **league_players_stats**
> PlayerSeasonStats league_players_stats(id)



Get stats for a specific league player.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.player_season_stats import PlayerSeasonStats
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
    api_instance = openapi_client.LeaguePlayersApi(api_client)
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **league_players_update**
> LeaguePlayer league_players_update(id, data)



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
    api_instance = openapi_client.LeaguePlayersApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.
    data = openapi_client.LeaguePlayer() # LeaguePlayer | 

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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


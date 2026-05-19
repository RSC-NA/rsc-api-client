# rscapi.StatsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stats_flagged_matches_list**](StatsApi.md#stats_flagged_matches_list) | **GET** /stats/flagged-matches/ | 
[**stats_flagged_matches_retrieve**](StatsApi.md#stats_flagged_matches_retrieve) | **GET** /stats/flagged-matches/{id}/ | 
[**stats_sbv_list**](StatsApi.md#stats_sbv_list) | **GET** /stats/sbv/ | 
[**stats_sbv_retrieve**](StatsApi.md#stats_sbv_retrieve) | **GET** /stats/sbv/{id}/ | 


# **stats_flagged_matches_list**
> PaginatedFlaggedMatchList stats_flagged_matches_list(day=day, league=league, limit=limit, match_type=match_type, missing_ballchasing_group=missing_ballchasing_group, missing_result=missing_result, missing_stats=missing_stats, offset=offset, search=search, season=season)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.paginated_flagged_match_list import PaginatedFlaggedMatchList
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
    api_instance = rscapi.StatsApi(api_client)
    day = 56 # int | Match day (optional)
    league = 56 # int | League ID (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    match_type = 'match_type_example' # str | Match type filter (optional)
    missing_ballchasing_group = True # bool | Filter by missing ballchasing group flag (optional)
    missing_result = True # bool | Filter by missing result flag (optional)
    missing_stats = True # bool | Filter by missing stats flag (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    search = 'search_example' # str | Case-insensitive search across team and franchise names (optional)
    season = 56 # int | Season ID (optional)

    try:
        api_response = await api_instance.stats_flagged_matches_list(day=day, league=league, limit=limit, match_type=match_type, missing_ballchasing_group=missing_ballchasing_group, missing_result=missing_result, missing_stats=missing_stats, offset=offset, search=search, season=season)
        print("The response of StatsApi->stats_flagged_matches_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->stats_flagged_matches_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **day** | **int**| Match day | [optional] 
 **league** | **int**| League ID | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **match_type** | **str**| Match type filter | [optional] 
 **missing_ballchasing_group** | **bool**| Filter by missing ballchasing group flag | [optional] 
 **missing_result** | **bool**| Filter by missing result flag | [optional] 
 **missing_stats** | **bool**| Filter by missing stats flag | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **search** | **str**| Case-insensitive search across team and franchise names | [optional] 
 **season** | **int**| Season ID | [optional] 

### Return type

[**PaginatedFlaggedMatchList**](PaginatedFlaggedMatchList.md)

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

# **stats_flagged_matches_retrieve**
> FlaggedMatch stats_flagged_matches_retrieve(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.flagged_match import FlaggedMatch
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
    api_instance = rscapi.StatsApi(api_client)
    id = 56 # int | A unique integer value identifying this match.

    try:
        api_response = await api_instance.stats_flagged_matches_retrieve(id)
        print("The response of StatsApi->stats_flagged_matches_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->stats_flagged_matches_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this match. | 

### Return type

[**FlaggedMatch**](FlaggedMatch.md)

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

# **stats_sbv_list**
> List[SBVResult] stats_sbv_list(league, season, tier, stats_type=stats_type)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.sbv_result import SBVResult
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
    api_instance = rscapi.StatsApi(api_client)
    league = 56 # int | League ID
    season = 56 # int | Season ID
    tier = 56 # int | Tier ID
    stats_type = REG # str | Stats type filter  * `REG` - Regular Season Stats * `PST` - Post Season Stats (optional) (default to REG)

    try:
        api_response = await api_instance.stats_sbv_list(league, season, tier, stats_type=stats_type)
        print("The response of StatsApi->stats_sbv_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->stats_sbv_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league** | **int**| League ID | 
 **season** | **int**| Season ID | 
 **tier** | **int**| Tier ID | 
 **stats_type** | **str**| Stats type filter  * &#x60;REG&#x60; - Regular Season Stats * &#x60;PST&#x60; - Post Season Stats | [optional] [default to REG]

### Return type

[**List[SBVResult]**](SBVResult.md)

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

# **stats_sbv_retrieve**
> SBVResult stats_sbv_retrieve(id, league, pk, season=season, season_id=season_id, season_number=season_number, stats_type=stats_type)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.sbv_result import SBVResult
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
    api_instance = rscapi.StatsApi(api_client)
    id = 56 # int | A unique integer value identifying this league player.
    league = 56 # int | League ID
    pk = 'pk_example' # str | LeaguePlayer ID or Member discord_id
    season = 56 # int | Season Number (alias) (optional)
    season_id = 56 # int | Season ID (optional)
    season_number = 56 # int | Season Number (optional)
    stats_type = REG # str | Stats type filter  * `REG` - Regular Season Stats * `PST` - Post Season Stats (optional) (default to REG)

    try:
        api_response = await api_instance.stats_sbv_retrieve(id, league, pk, season=season, season_id=season_id, season_number=season_number, stats_type=stats_type)
        print("The response of StatsApi->stats_sbv_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->stats_sbv_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league player. | 
 **league** | **int**| League ID | 
 **pk** | **str**| LeaguePlayer ID or Member discord_id | 
 **season** | **int**| Season Number (alias) | [optional] 
 **season_id** | **int**| Season ID | [optional] 
 **season_number** | **int**| Season Number | [optional] 
 **stats_type** | **str**| Stats type filter  * &#x60;REG&#x60; - Regular Season Stats * &#x60;PST&#x60; - Post Season Stats | [optional] [default to REG]

### Return type

[**SBVResult**](SBVResult.md)

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


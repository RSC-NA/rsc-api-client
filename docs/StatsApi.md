# rscapi.StatsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stats_flagged_matches_list**](StatsApi.md#stats_flagged_matches_list) | **GET** /stats/flagged-matches/ | 
[**stats_flagged_matches_retrieve**](StatsApi.md#stats_flagged_matches_retrieve) | **GET** /stats/flagged-matches/{id}/ | 
[**stats_idr_list**](StatsApi.md#stats_idr_list) | **GET** /stats/idr/ | 
[**stats_idr_retrieve**](StatsApi.md#stats_idr_retrieve) | **GET** /stats/idr/{id}/ | 
[**stats_sbv_list**](StatsApi.md#stats_sbv_list) | **GET** /stats/sbv/ | 
[**stats_sbv_retrieve**](StatsApi.md#stats_sbv_retrieve) | **GET** /stats/sbv/{id}/ | 


# **stats_flagged_matches_list**
> PaginatedFlaggedMatchList stats_flagged_matches_list(day=day, league=league, limit=limit, match_type=match_type, missing_ballchasing_group=missing_ballchasing_group, missing_result=missing_result, missing_stats=missing_stats, offset=offset, search=search, season=season, season_number=season_number)

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
    league = 56 # int | League ID. (Default: the default league) (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    match_type = 'match_type_example' # str | Match type filter (optional)
    missing_ballchasing_group = True # bool | Filter by missing ballchasing group flag (optional)
    missing_result = True # bool | Filter by missing result flag (optional)
    missing_stats = True # bool | Filter by missing stats flag (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    search = 'search_example' # str | Case-insensitive search across team and franchise names (optional)
    season = 56 # int | Season ID, within the league. (Default: the league's current season) (optional)
    season_number = 56 # int | Season number, within the league. Ignored when `season` is given. (optional)

    try:
        api_response = await api_instance.stats_flagged_matches_list(day=day, league=league, limit=limit, match_type=match_type, missing_ballchasing_group=missing_ballchasing_group, missing_result=missing_result, missing_stats=missing_stats, offset=offset, search=search, season=season, season_number=season_number)
        print("The response of StatsApi->stats_flagged_matches_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->stats_flagged_matches_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **day** | **int**| Match day | [optional] 
 **league** | **int**| League ID. (Default: the default league) | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **match_type** | **str**| Match type filter | [optional] 
 **missing_ballchasing_group** | **bool**| Filter by missing ballchasing group flag | [optional] 
 **missing_result** | **bool**| Filter by missing result flag | [optional] 
 **missing_stats** | **bool**| Filter by missing stats flag | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **search** | **str**| Case-insensitive search across team and franchise names | [optional] 
 **season** | **int**| Season ID, within the league. (Default: the league&#39;s current season) | [optional] 
 **season_number** | **int**| Season number, within the league. Ignored when &#x60;season&#x60; is given. | [optional] 

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

# **stats_idr_list**
> List[IDRResult] stats_idr_list(tier, league=league, qualified_only=qualified_only, season=season, season_number=season_number, stats_type=stats_type)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.idr_result import IDRResult
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
    tier = 56 # int | Tier ID
    league = 56 # int | League ID (Default: the default league) (optional)
    qualified_only = False # bool | Only return players meeting the tier's games-played threshold. (optional) (default to False)
    season = 56 # int | Season ID (Default: the league's current season) (optional)
    season_number = 56 # int | Season number (optional)
    stats_type = 'REG' # str | Stats type filter  * `REG` - Regular Season Stats * `PRE` - Pre-season Stats * `PST` - Post Season Stats (optional) (default to 'REG')

    try:
        api_response = await api_instance.stats_idr_list(tier, league=league, qualified_only=qualified_only, season=season, season_number=season_number, stats_type=stats_type)
        print("The response of StatsApi->stats_idr_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->stats_idr_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tier** | **int**| Tier ID | 
 **league** | **int**| League ID (Default: the default league) | [optional] 
 **qualified_only** | **bool**| Only return players meeting the tier&#39;s games-played threshold. | [optional] [default to False]
 **season** | **int**| Season ID (Default: the league&#39;s current season) | [optional] 
 **season_number** | **int**| Season number | [optional] 
 **stats_type** | **str**| Stats type filter  * &#x60;REG&#x60; - Regular Season Stats * &#x60;PRE&#x60; - Pre-season Stats * &#x60;PST&#x60; - Post Season Stats | [optional] [default to &#39;REG&#39;]

### Return type

[**List[IDRResult]**](IDRResult.md)

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

# **stats_idr_retrieve**
> IDRResult stats_idr_retrieve(id, league=league, season=season, season_id=season_id, season_number=season_number, stats_type=stats_type)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.idr_result import IDRResult
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
    id = 56 # int | LeaguePlayer ID or Member discord_id
    league = 56 # int | League ID (Default: the default league) (optional)
    season = 56 # int | Season ID (Default: the league's current season) (optional)
    season_id = 56 # int | Deprecated spelling of `season`. (optional)
    season_number = 56 # int | Season number (optional)
    stats_type = 'REG' # str | Stats type filter  * `REG` - Regular Season Stats * `PRE` - Pre-season Stats * `PST` - Post Season Stats (optional) (default to 'REG')

    try:
        api_response = await api_instance.stats_idr_retrieve(id, league=league, season=season, season_id=season_id, season_number=season_number, stats_type=stats_type)
        print("The response of StatsApi->stats_idr_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->stats_idr_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| LeaguePlayer ID or Member discord_id | 
 **league** | **int**| League ID (Default: the default league) | [optional] 
 **season** | **int**| Season ID (Default: the league&#39;s current season) | [optional] 
 **season_id** | **int**| Deprecated spelling of &#x60;season&#x60;. | [optional] 
 **season_number** | **int**| Season number | [optional] 
 **stats_type** | **str**| Stats type filter  * &#x60;REG&#x60; - Regular Season Stats * &#x60;PRE&#x60; - Pre-season Stats * &#x60;PST&#x60; - Post Season Stats | [optional] [default to &#39;REG&#39;]

### Return type

[**IDRResult**](IDRResult.md)

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

# **stats_sbv_list**
> List[SBVResult] stats_sbv_list(tier, league=league, qualified_only=qualified_only, season=season, season_number=season_number, stats_type=stats_type)

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
    tier = 56 # int | Tier ID
    league = 56 # int | League ID (Default: the default league) (optional)
    qualified_only = False # bool | Only return players meeting the tier's games-played threshold. (optional) (default to False)
    season = 56 # int | Season ID (Default: the league's current season) (optional)
    season_number = 56 # int | Season number (optional)
    stats_type = 'REG' # str | Stats type filter  * `REG` - Regular Season Stats * `PRE` - Pre-season Stats * `PST` - Post Season Stats (optional) (default to 'REG')

    try:
        api_response = await api_instance.stats_sbv_list(tier, league=league, qualified_only=qualified_only, season=season, season_number=season_number, stats_type=stats_type)
        print("The response of StatsApi->stats_sbv_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->stats_sbv_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tier** | **int**| Tier ID | 
 **league** | **int**| League ID (Default: the default league) | [optional] 
 **qualified_only** | **bool**| Only return players meeting the tier&#39;s games-played threshold. | [optional] [default to False]
 **season** | **int**| Season ID (Default: the league&#39;s current season) | [optional] 
 **season_number** | **int**| Season number | [optional] 
 **stats_type** | **str**| Stats type filter  * &#x60;REG&#x60; - Regular Season Stats * &#x60;PRE&#x60; - Pre-season Stats * &#x60;PST&#x60; - Post Season Stats | [optional] [default to &#39;REG&#39;]

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
> SBVResult stats_sbv_retrieve(id, league=league, season=season, season_id=season_id, season_number=season_number, stats_type=stats_type)

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
    id = 56 # int | LeaguePlayer ID or Member discord_id
    league = 56 # int | League ID (Default: the default league) (optional)
    season = 56 # int | Season ID (Default: the league's current season) (optional)
    season_id = 56 # int | Deprecated spelling of `season`. (optional)
    season_number = 56 # int | Season number (optional)
    stats_type = 'REG' # str | Stats type filter  * `REG` - Regular Season Stats * `PRE` - Pre-season Stats * `PST` - Post Season Stats (optional) (default to 'REG')

    try:
        api_response = await api_instance.stats_sbv_retrieve(id, league=league, season=season, season_id=season_id, season_number=season_number, stats_type=stats_type)
        print("The response of StatsApi->stats_sbv_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->stats_sbv_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| LeaguePlayer ID or Member discord_id | 
 **league** | **int**| League ID (Default: the default league) | [optional] 
 **season** | **int**| Season ID (Default: the league&#39;s current season) | [optional] 
 **season_id** | **int**| Deprecated spelling of &#x60;season&#x60;. | [optional] 
 **season_number** | **int**| Season number | [optional] 
 **stats_type** | **str**| Stats type filter  * &#x60;REG&#x60; - Regular Season Stats * &#x60;PRE&#x60; - Pre-season Stats * &#x60;PST&#x60; - Post Season Stats | [optional] [default to &#39;REG&#39;]

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


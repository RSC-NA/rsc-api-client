# rscapi.DraftPicksApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**draft_picks_count_keeper_list**](DraftPicksApi.md#draft_picks_count_keeper_list) | **GET** /draft-picks/count-keeper/ | 
[**draft_picks_destroy**](DraftPicksApi.md#draft_picks_destroy) | **DELETE** /draft-picks/{id}/ | 
[**draft_picks_list**](DraftPicksApi.md#draft_picks_list) | **GET** /draft-picks/ | 
[**draft_picks_partial_update**](DraftPicksApi.md#draft_picks_partial_update) | **PATCH** /draft-picks/{id}/ | 
[**draft_picks_retrieve**](DraftPicksApi.md#draft_picks_retrieve) | **GET** /draft-picks/{id}/ | 
[**draft_picks_swap_create**](DraftPicksApi.md#draft_picks_swap_create) | **POST** /draft-picks/swap/ | 
[**draft_picks_update**](DraftPicksApi.md#draft_picks_update) | **PUT** /draft-picks/{id}/ | 


# **draft_picks_count_keeper_list**
> List[DraftTierCountKeeperExport] draft_picks_count_keeper_list(tier, count=count, format=format, keeper=keeper, league=league, season=season, season_number=season_number)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.draft_tier_count_keeper_export import DraftTierCountKeeperExport
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
    api_instance = rscapi.DraftPicksApi(api_client)
    tier = 'tier_example' # str | Tier id or exact tier name.
    count = 56 # int | Filter by calculated count value. (optional)
    format = 'format_example' # str |  (optional)
    keeper = 56 # int | Filter by keeper flag. Use 1 for keeper picks and 0 for non-keeper picks. (optional)
    league = 1 # int | League id. Defaults to 1. (optional) (default to 1)
    season = 56 # int | Season id. If omitted, current season for the league is used. (optional)
    season_number = 56 # int | Season number (alternative to season id). (optional)

    try:
        api_response = await api_instance.draft_picks_count_keeper_list(tier, count=count, format=format, keeper=keeper, league=league, season=season, season_number=season_number)
        print("The response of DraftPicksApi->draft_picks_count_keeper_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftPicksApi->draft_picks_count_keeper_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tier** | **str**| Tier id or exact tier name. | 
 **count** | **int**| Filter by calculated count value. | [optional] 
 **format** | **str**|  | [optional] 
 **keeper** | **int**| Filter by keeper flag. Use 1 for keeper picks and 0 for non-keeper picks. | [optional] 
 **league** | **int**| League id. Defaults to 1. | [optional] [default to 1]
 **season** | **int**| Season id. If omitted, current season for the league is used. | [optional] 
 **season_number** | **int**| Season number (alternative to season id). | [optional] 

### Return type

[**List[DraftTierCountKeeperExport]**](DraftTierCountKeeperExport.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **draft_picks_destroy**
> draft_picks_destroy(id)

A viewset that provides retrieve, update, partial_update, and destroy actions.

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
    api_instance = rscapi.DraftPicksApi(api_client)
    id = 56 # int | A unique integer value identifying this draft pick.

    try:
        await api_instance.draft_picks_destroy(id)
    except Exception as e:
        print("Exception when calling DraftPicksApi->draft_picks_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this draft pick. | 

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

# **draft_picks_list**
> PaginatedDraftPickListList draft_picks_list(deleted=deleted, franchise=franchise, future=future, future_season=future_season, limit=limit, number=number, offset=offset, original_pick=original_pick, pick_from=pick_from, round=round, season_number=season_number, tier=tier)

List all draft picks for a given league and season.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.paginated_draft_pick_list_list import PaginatedDraftPickListList
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
    api_instance = rscapi.DraftPicksApi(api_client)
    deleted = True # bool | Is this pick removed because someone lost a tier. (optional)
    franchise = 'franchise_example' # str | Franchise name contains. (optional)
    future = True # bool | Future pick. (optional)
    future_season = 56 # int | Future season number. (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    number = 56 # int | Pick number in the specific tier. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    original_pick = 'original_pick_example' # str | Pick this originally came from. (optional)
    pick_from = 'pick_from_example' # str | Prefix of who the pick came from. (optional)
    round = 56 # int | Specific round in the tier. (optional)
    season_number = 56 # int | Season number. (optional)
    tier = 'tier_example' # str | Tier name. (optional)

    try:
        api_response = await api_instance.draft_picks_list(deleted=deleted, franchise=franchise, future=future, future_season=future_season, limit=limit, number=number, offset=offset, original_pick=original_pick, pick_from=pick_from, round=round, season_number=season_number, tier=tier)
        print("The response of DraftPicksApi->draft_picks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftPicksApi->draft_picks_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deleted** | **bool**| Is this pick removed because someone lost a tier. | [optional] 
 **franchise** | **str**| Franchise name contains. | [optional] 
 **future** | **bool**| Future pick. | [optional] 
 **future_season** | **int**| Future season number. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **number** | **int**| Pick number in the specific tier. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **original_pick** | **str**| Pick this originally came from. | [optional] 
 **pick_from** | **str**| Prefix of who the pick came from. | [optional] 
 **round** | **int**| Specific round in the tier. | [optional] 
 **season_number** | **int**| Season number. | [optional] 
 **tier** | **str**| Tier name. | [optional] 

### Return type

[**PaginatedDraftPickListList**](PaginatedDraftPickListList.md)

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

# **draft_picks_partial_update**
> DraftPickDetails draft_picks_partial_update(id, patched_draft_pick_details=patched_draft_pick_details)

A viewset that provides retrieve, update, partial_update, and destroy actions.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.draft_pick_details import DraftPickDetails
from rscapi.models.patched_draft_pick_details import PatchedDraftPickDetails
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
    api_instance = rscapi.DraftPicksApi(api_client)
    id = 56 # int | A unique integer value identifying this draft pick.
    patched_draft_pick_details = rscapi.PatchedDraftPickDetails() # PatchedDraftPickDetails |  (optional)

    try:
        api_response = await api_instance.draft_picks_partial_update(id, patched_draft_pick_details=patched_draft_pick_details)
        print("The response of DraftPicksApi->draft_picks_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftPicksApi->draft_picks_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this draft pick. | 
 **patched_draft_pick_details** | [**PatchedDraftPickDetails**](PatchedDraftPickDetails.md)|  | [optional] 

### Return type

[**DraftPickDetails**](DraftPickDetails.md)

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

# **draft_picks_retrieve**
> DraftPickDetails draft_picks_retrieve(id)

A viewset that provides retrieve, update, partial_update, and destroy actions.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.draft_pick_details import DraftPickDetails
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
    api_instance = rscapi.DraftPicksApi(api_client)
    id = 56 # int | A unique integer value identifying this draft pick.

    try:
        api_response = await api_instance.draft_picks_retrieve(id)
        print("The response of DraftPicksApi->draft_picks_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftPicksApi->draft_picks_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this draft pick. | 

### Return type

[**DraftPickDetails**](DraftPickDetails.md)

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

# **draft_picks_swap_create**
> PaginatedDraftPickListList draft_picks_swap_create(draft_pick_swap, page=page)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.draft_pick_swap import DraftPickSwap
from rscapi.models.paginated_draft_pick_list_list import PaginatedDraftPickListList
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
    api_instance = rscapi.DraftPicksApi(api_client)
    draft_pick_swap = [rscapi.DraftPickSwap()] # List[DraftPickSwap] | 
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = await api_instance.draft_picks_swap_create(draft_pick_swap, page=page)
        print("The response of DraftPicksApi->draft_picks_swap_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftPicksApi->draft_picks_swap_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_pick_swap** | [**List[DraftPickSwap]**](DraftPickSwap.md)|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedDraftPickListList**](PaginatedDraftPickListList.md)

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

# **draft_picks_update**
> DraftPickDetails draft_picks_update(id, draft_pick_details)

A viewset that provides retrieve, update, partial_update, and destroy actions.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.draft_pick_details import DraftPickDetails
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
    api_instance = rscapi.DraftPicksApi(api_client)
    id = 56 # int | A unique integer value identifying this draft pick.
    draft_pick_details = rscapi.DraftPickDetails() # DraftPickDetails | 

    try:
        api_response = await api_instance.draft_picks_update(id, draft_pick_details)
        print("The response of DraftPicksApi->draft_picks_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftPicksApi->draft_picks_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this draft pick. | 
 **draft_pick_details** | [**DraftPickDetails**](DraftPickDetails.md)|  | 

### Return type

[**DraftPickDetails**](DraftPickDetails.md)

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


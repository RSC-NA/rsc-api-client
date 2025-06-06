# rscapi.DraftPicksApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**draft_picks_list**](DraftPicksApi.md#draft_picks_list) | **GET** /draft-picks/ | 
[**draft_picks_read**](DraftPicksApi.md#draft_picks_read) | **GET** /draft-picks/{id}/ | 
[**draft_picks_swap**](DraftPicksApi.md#draft_picks_swap) | **POST** /draft-picks/swap/ | 


# **draft_picks_list**
> DraftPicksList200Response draft_picks_list(number=number, round=round, franchise=franchise, future=future, future_season=future_season, deleted=deleted, pick_from=pick_from, original_pick=original_pick, season_number=season_number, tier=tier, page=page)

List all draft picks for a given league and season.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.draft_picks_list200_response import DraftPicksList200Response
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

# Configure API key authorization: Api-Key
configuration.api_key['Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
async with rscapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rscapi.DraftPicksApi(api_client)
    number = 'number_example' # str | number (optional)
    round = 'round_example' # str | round (optional)
    franchise = 'franchise_example' # str | franchise (optional)
    future = 'future_example' # str | future (optional)
    future_season = 'future_season_example' # str | future_season (optional)
    deleted = 'deleted_example' # str | deleted (optional)
    pick_from = 'pick_from_example' # str | pick_from (optional)
    original_pick = 'original_pick_example' # str | original_pick (optional)
    season_number = 'season_number_example' # str | season_number (optional)
    tier = 'tier_example' # str | tier (optional)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = await api_instance.draft_picks_list(number=number, round=round, franchise=franchise, future=future, future_season=future_season, deleted=deleted, pick_from=pick_from, original_pick=original_pick, season_number=season_number, tier=tier, page=page)
        print("The response of DraftPicksApi->draft_picks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftPicksApi->draft_picks_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| number | [optional] 
 **round** | **str**| round | [optional] 
 **franchise** | **str**| franchise | [optional] 
 **future** | **str**| future | [optional] 
 **future_season** | **str**| future_season | [optional] 
 **deleted** | **str**| deleted | [optional] 
 **pick_from** | **str**| pick_from | [optional] 
 **original_pick** | **str**| original_pick | [optional] 
 **season_number** | **str**| season_number | [optional] 
 **tier** | **str**| tier | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**DraftPicksList200Response**](DraftPicksList200Response.md)

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

# **draft_picks_read**
> DraftPicks draft_picks_read(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.draft_picks import DraftPicks
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

# Configure API key authorization: Api-Key
configuration.api_key['Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
async with rscapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rscapi.DraftPicksApi(api_client)
    id = 56 # int | A unique integer value identifying this draft picks.

    try:
        api_response = await api_instance.draft_picks_read(id)
        print("The response of DraftPicksApi->draft_picks_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftPicksApi->draft_picks_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this draft picks. | 

### Return type

[**DraftPicks**](DraftPicks.md)

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

# **draft_picks_swap**
> List[DraftPicks] draft_picks_swap(data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.draft_pick_swap import DraftPickSwap
from rscapi.models.draft_picks import DraftPicks
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

# Configure API key authorization: Api-Key
configuration.api_key['Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
async with rscapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rscapi.DraftPicksApi(api_client)
    data = [rscapi.DraftPickSwap()] # List[DraftPickSwap] | 

    try:
        api_response = await api_instance.draft_picks_swap(data)
        print("The response of DraftPicksApi->draft_picks_swap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftPicksApi->draft_picks_swap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**List[DraftPickSwap]**](DraftPickSwap.md)|  | 

### Return type

[**List[DraftPicks]**](DraftPicks.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


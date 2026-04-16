# rscapi.DraftPicksApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**draft_picks_delete**](DraftPicksApi.md#draft_picks_delete) | **DELETE** /draft-picks/{id}/ | 
[**draft_picks_list**](DraftPicksApi.md#draft_picks_list) | **GET** /draft-picks/ | 
[**draft_picks_partial_update**](DraftPicksApi.md#draft_picks_partial_update) | **PATCH** /draft-picks/{id}/ | 
[**draft_picks_read**](DraftPicksApi.md#draft_picks_read) | **GET** /draft-picks/{id}/ | 
[**draft_picks_swap**](DraftPicksApi.md#draft_picks_swap) | **POST** /draft-picks/swap/ | 
[**draft_picks_update**](DraftPicksApi.md#draft_picks_update) | **PUT** /draft-picks/{id}/ | 


# **draft_picks_delete**
> draft_picks_delete(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
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
    id = 56 # int | A unique integer value identifying this draft pick.

    try:
        await api_instance.draft_picks_delete(id)
    except Exception as e:
        print("Exception when calling DraftPicksApi->draft_picks_delete: %s\n" % e)
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
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **draft_picks_list**
> DraftPicksList200Response draft_picks_list(number=number, round=round, franchise=franchise, future=future, future_season=future_season, deleted=deleted, pick_from=pick_from, original_pick=original_pick, season_number=season_number, tier=tier, limit=limit, offset=offset)

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
    number = 56 # int | Pick number in the specific tier. (optional)
    round = 56 # int | Specific round in the tier. (optional)
    franchise = 'franchise_example' # str | Franchise name contains. (optional)
    future = True # bool | Future pick. (optional)
    future_season = 56 # int | Future season number. (optional)
    deleted = True # bool | Is this pick removed because someone lost a tier. (optional)
    pick_from = 'pick_from_example' # str | Prefix of who the pick came from. (optional)
    original_pick = 'original_pick_example' # str | Pick this originally came from. (optional)
    season_number = 56 # int | Season number. (optional)
    tier = 'tier_example' # str | Tier name. (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.draft_picks_list(number=number, round=round, franchise=franchise, future=future, future_season=future_season, deleted=deleted, pick_from=pick_from, original_pick=original_pick, season_number=season_number, tier=tier, limit=limit, offset=offset)
        print("The response of DraftPicksApi->draft_picks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftPicksApi->draft_picks_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **int**| Pick number in the specific tier. | [optional] 
 **round** | **int**| Specific round in the tier. | [optional] 
 **franchise** | **str**| Franchise name contains. | [optional] 
 **future** | **bool**| Future pick. | [optional] 
 **future_season** | **int**| Future season number. | [optional] 
 **deleted** | **bool**| Is this pick removed because someone lost a tier. | [optional] 
 **pick_from** | **str**| Prefix of who the pick came from. | [optional] 
 **original_pick** | **str**| Pick this originally came from. | [optional] 
 **season_number** | **int**| Season number. | [optional] 
 **tier** | **str**| Tier name. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

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

# **draft_picks_partial_update**
> DraftPickDetails draft_picks_partial_update(id, data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.draft_pick_details import DraftPickDetails
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
    id = 56 # int | A unique integer value identifying this draft pick.
    data = rscapi.DraftPickDetails() # DraftPickDetails | 

    try:
        api_response = await api_instance.draft_picks_partial_update(id, data)
        print("The response of DraftPicksApi->draft_picks_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftPicksApi->draft_picks_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this draft pick. | 
 **data** | [**DraftPickDetails**](DraftPickDetails.md)|  | 

### Return type

[**DraftPickDetails**](DraftPickDetails.md)

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

# **draft_picks_read**
> DraftPickDetails draft_picks_read(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.draft_pick_details import DraftPickDetails
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
    id = 56 # int | A unique integer value identifying this draft pick.

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

# **draft_picks_swap**
> List[DraftPickList] draft_picks_swap(data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.draft_pick_list import DraftPickList
from rscapi.models.draft_pick_swap import DraftPickSwap
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

[**List[DraftPickList]**](DraftPickList.md)

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

# **draft_picks_update**
> DraftPickDetails draft_picks_update(id, data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.draft_pick_details import DraftPickDetails
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
    id = 56 # int | A unique integer value identifying this draft pick.
    data = rscapi.DraftPickDetails() # DraftPickDetails | 

    try:
        api_response = await api_instance.draft_picks_update(id, data)
        print("The response of DraftPicksApi->draft_picks_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftPicksApi->draft_picks_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this draft pick. | 
 **data** | [**DraftPickDetails**](DraftPickDetails.md)|  | 

### Return type

[**DraftPickDetails**](DraftPickDetails.md)

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


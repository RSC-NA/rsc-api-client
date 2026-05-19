# rscapi.TrackerLinksApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tracker_links_create**](TrackerLinksApi.md#tracker_links_create) | **POST** /tracker-links/ | 
[**tracker_links_dedup_mmr_pulls_create**](TrackerLinksApi.md#tracker_links_dedup_mmr_pulls_create) | **POST** /tracker-links/dedup_mmr_pulls/ | 
[**tracker_links_dedup_mmr_pulls_retrieve**](TrackerLinksApi.md#tracker_links_dedup_mmr_pulls_retrieve) | **GET** /tracker-links/dedup_mmr_pulls/ | 
[**tracker_links_dedup_pulls_create**](TrackerLinksApi.md#tracker_links_dedup_pulls_create) | **POST** /tracker-links/{id}/dedup_pulls/ | 
[**tracker_links_dedup_pulls_retrieve**](TrackerLinksApi.md#tracker_links_dedup_pulls_retrieve) | **GET** /tracker-links/{id}/dedup_pulls/ | 
[**tracker_links_destroy**](TrackerLinksApi.md#tracker_links_destroy) | **DELETE** /tracker-links/{id}/ | 
[**tracker_links_fix_duplicate_links_retrieve**](TrackerLinksApi.md#tracker_links_fix_duplicate_links_retrieve) | **GET** /tracker-links/fix_duplicate_links/ | 
[**tracker_links_invalidate_links_create**](TrackerLinksApi.md#tracker_links_invalidate_links_create) | **POST** /tracker-links/invalidate_links/ | 
[**tracker_links_link_create**](TrackerLinksApi.md#tracker_links_link_create) | **POST** /tracker-links/{id}/link/ | 
[**tracker_links_links_stats_list**](TrackerLinksApi.md#tracker_links_links_stats_list) | **GET** /tracker-links/links_stats/ | 
[**tracker_links_list**](TrackerLinksApi.md#tracker_links_list) | **GET** /tracker-links/ | 
[**tracker_links_migrate_pulls_create**](TrackerLinksApi.md#tracker_links_migrate_pulls_create) | **POST** /tracker-links/{id}/migrate_pulls/ | 
[**tracker_links_next_list**](TrackerLinksApi.md#tracker_links_next_list) | **GET** /tracker-links/next/ | 
[**tracker_links_peak_stats_retrieve**](TrackerLinksApi.md#tracker_links_peak_stats_retrieve) | **GET** /tracker-links/{id}/peak_stats/ | 
[**tracker_links_retrieve**](TrackerLinksApi.md#tracker_links_retrieve) | **GET** /tracker-links/{id}/ | 
[**tracker_links_status_partial_update**](TrackerLinksApi.md#tracker_links_status_partial_update) | **PATCH** /tracker-links/{id}/status/ | 
[**tracker_links_status_retrieve**](TrackerLinksApi.md#tracker_links_status_retrieve) | **GET** /tracker-links/{id}/status/ | 
[**tracker_links_unlink_create**](TrackerLinksApi.md#tracker_links_unlink_create) | **POST** /tracker-links/{id}/unlink/ | 


# **tracker_links_create**
> TrackerLink tracker_links_create(tracker_link, format=format)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    tracker_link = rscapi.TrackerLink() # TrackerLink | 
    format = 'format_example' # str |  (optional)

    try:
        api_response = await api_instance.tracker_links_create(tracker_link, format=format)
        print("The response of TrackerLinksApi->tracker_links_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_link** | [**TrackerLink**](TrackerLink.md)|  | 
 **format** | **str**|  | [optional] 

### Return type

[**TrackerLink**](TrackerLink.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tracker_links_dedup_mmr_pulls_create**
> TrackerLink tracker_links_dedup_mmr_pulls_create()

Deduplicate PlayerMMRPull records (ignoring date_pulled and notes).

GET:  Dry-run. Returns duplicate counts and the IDs that would be deleted.
POST: Actually deletes the duplicates (keeps earliest record per group).

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
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
    api_instance = rscapi.TrackerLinksApi(api_client)

    try:
        api_response = await api_instance.tracker_links_dedup_mmr_pulls_create()
        print("The response of TrackerLinksApi->tracker_links_dedup_mmr_pulls_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_dedup_mmr_pulls_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TrackerLink**](TrackerLink.md)

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

# **tracker_links_dedup_mmr_pulls_retrieve**
> TrackerLink tracker_links_dedup_mmr_pulls_retrieve()

Deduplicate PlayerMMRPull records (ignoring date_pulled and notes).

GET:  Dry-run. Returns duplicate counts and the IDs that would be deleted.
POST: Actually deletes the duplicates (keeps earliest record per group).

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
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
    api_instance = rscapi.TrackerLinksApi(api_client)

    try:
        api_response = await api_instance.tracker_links_dedup_mmr_pulls_retrieve()
        print("The response of TrackerLinksApi->tracker_links_dedup_mmr_pulls_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_dedup_mmr_pulls_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TrackerLink**](TrackerLink.md)

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

# **tracker_links_dedup_pulls_create**
> TrackerLink tracker_links_dedup_pulls_create(id)

Deduplicate PlayerMMRPull records for a single tracker link.

GET:  Dry-run. Returns duplicate counts, IDs to delete, and max field
      stats before/after so you can validate no data is lost.
POST: Actually deletes the duplicates (keeps newest date_pulled per group).
      Aborts if max field stats would change.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker link.

    try:
        api_response = await api_instance.tracker_links_dedup_pulls_create(id)
        print("The response of TrackerLinksApi->tracker_links_dedup_pulls_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_dedup_pulls_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker link. | 

### Return type

[**TrackerLink**](TrackerLink.md)

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

# **tracker_links_dedup_pulls_retrieve**
> TrackerLink tracker_links_dedup_pulls_retrieve(id)

Deduplicate PlayerMMRPull records for a single tracker link.

GET:  Dry-run. Returns duplicate counts, IDs to delete, and max field
      stats before/after so you can validate no data is lost.
POST: Actually deletes the duplicates (keeps newest date_pulled per group).
      Aborts if max field stats would change.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker link.

    try:
        api_response = await api_instance.tracker_links_dedup_pulls_retrieve(id)
        print("The response of TrackerLinksApi->tracker_links_dedup_pulls_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_dedup_pulls_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker link. | 

### Return type

[**TrackerLink**](TrackerLink.md)

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

# **tracker_links_destroy**
> tracker_links_destroy(id, format=format)

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
    api_instance = rscapi.TrackerLinksApi(api_client)
    id = 'id_example' # str | 
    format = 'format_example' # str |  (optional)

    try:
        await api_instance.tracker_links_destroy(id, format=format)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **format** | **str**|  | [optional] 

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

# **tracker_links_fix_duplicate_links_retrieve**
> TrackerLink tracker_links_fix_duplicate_links_retrieve()

Fixes duplicate tracker links by merging MMR pulls and removing duplicates.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
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
    api_instance = rscapi.TrackerLinksApi(api_client)

    try:
        api_response = await api_instance.tracker_links_fix_duplicate_links_retrieve()
        print("The response of TrackerLinksApi->tracker_links_fix_duplicate_links_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_fix_duplicate_links_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TrackerLink**](TrackerLink.md)

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

# **tracker_links_invalidate_links_create**
> TrackerLink tracker_links_invalidate_links_create(tracker_link_invalidate_object=tracker_link_invalidate_object)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
from rscapi.models.tracker_link_invalidate_object import TrackerLinkInvalidateObject
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    tracker_link_invalidate_object = rscapi.TrackerLinkInvalidateObject() # TrackerLinkInvalidateObject |  (optional)

    try:
        api_response = await api_instance.tracker_links_invalidate_links_create(tracker_link_invalidate_object=tracker_link_invalidate_object)
        print("The response of TrackerLinksApi->tracker_links_invalidate_links_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_invalidate_links_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_link_invalidate_object** | [**TrackerLinkInvalidateObject**](TrackerLinkInvalidateObject.md)|  | [optional] 

### Return type

[**TrackerLink**](TrackerLink.md)

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

# **tracker_links_link_create**
> TrackerLink tracker_links_link_create(id, tracker_link_linking)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
from rscapi.models.tracker_link_linking import TrackerLinkLinking
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker link.
    tracker_link_linking = rscapi.TrackerLinkLinking() # TrackerLinkLinking | 

    try:
        api_response = await api_instance.tracker_links_link_create(id, tracker_link_linking)
        print("The response of TrackerLinksApi->tracker_links_link_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_link_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker link. | 
 **tracker_link_linking** | [**TrackerLinkLinking**](TrackerLinkLinking.md)|  | 

### Return type

[**TrackerLink**](TrackerLink.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tracker_links_links_stats_list**
> List[TrackerLinkStats] tracker_links_links_stats_list(format=format)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link_stats import TrackerLinkStats
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    format = 'format_example' # str |  (optional)

    try:
        api_response = await api_instance.tracker_links_links_stats_list(format=format)
        print("The response of TrackerLinksApi->tracker_links_links_stats_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_links_stats_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] 

### Return type

[**List[TrackerLinkStats]**](TrackerLinkStats.md)

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

# **tracker_links_list**
> PaginatedTrackerLinkList tracker_links_list(discord_id=discord_id, format=format, is_active=is_active, limit=limit, link=link, member_name=member_name, offset=offset, platform=platform, platform_id=platform_id, status=status)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.paginated_tracker_link_list import PaginatedTrackerLinkList
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    discord_id = 56 # int | Discord ID of member to find links for. (optional)
    format = 'format_example' # str |  (optional)
    is_active = True # bool | Only return active members. (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    link = 'link_example' # str | Filter by tracker link URL. (case-insensitive contains) (optional)
    member_name = 'member_name_example' # str | Link belonging to specific rsc member by name. (case-insensitive) (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    platform = 'platform_example' # str | Filter by platform. (optional)
    platform_id = 'platform_id_example' # str | Filter by platform ID. (case-insensitive) (optional)
    status = 'status_example' # str | Filter by tracker link status. (optional)

    try:
        api_response = await api_instance.tracker_links_list(discord_id=discord_id, format=format, is_active=is_active, limit=limit, link=link, member_name=member_name, offset=offset, platform=platform, platform_id=platform_id, status=status)
        print("The response of TrackerLinksApi->tracker_links_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discord_id** | **int**| Discord ID of member to find links for. | [optional] 
 **format** | **str**|  | [optional] 
 **is_active** | **bool**| Only return active members. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **link** | **str**| Filter by tracker link URL. (case-insensitive contains) | [optional] 
 **member_name** | **str**| Link belonging to specific rsc member by name. (case-insensitive) | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **platform** | **str**| Filter by platform. | [optional] 
 **platform_id** | **str**| Filter by platform ID. (case-insensitive) | [optional] 
 **status** | **str**| Filter by tracker link status. | [optional] 

### Return type

[**PaginatedTrackerLinkList**](PaginatedTrackerLinkList.md)

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

# **tracker_links_migrate_pulls_create**
> TrackerLink tracker_links_migrate_pulls_create(id, tracker_id_input)

Migrates MMR pulls from one tracker link to another.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_id_input import TrackerIDInput
from rscapi.models.tracker_link import TrackerLink
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker link.
    tracker_id_input = rscapi.TrackerIDInput() # TrackerIDInput | 

    try:
        api_response = await api_instance.tracker_links_migrate_pulls_create(id, tracker_id_input)
        print("The response of TrackerLinksApi->tracker_links_migrate_pulls_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_migrate_pulls_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker link. | 
 **tracker_id_input** | [**TrackerIDInput**](TrackerIDInput.md)|  | 

### Return type

[**TrackerLink**](TrackerLink.md)

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

# **tracker_links_next_list**
> List[TrackerLink] tracker_links_next_list(format=format, limit=limit)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    format = 'format_example' # str |  (optional)
    limit = 56 # int | Number of tracker links to grab (Default: 1, Max:25) (optional)

    try:
        api_response = await api_instance.tracker_links_next_list(format=format, limit=limit)
        print("The response of TrackerLinksApi->tracker_links_next_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_next_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] 
 **limit** | **int**| Number of tracker links to grab (Default: 1, Max:25) | [optional] 

### Return type

[**List[TrackerLink]**](TrackerLink.md)

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

# **tracker_links_peak_stats_retrieve**
> TrackerPeak tracker_links_peak_stats_retrieve(id, pysonix_season)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_peak import TrackerPeak
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker link.
    pysonix_season = 56 # int | Psysonix season number to filter by.

    try:
        api_response = await api_instance.tracker_links_peak_stats_retrieve(id, pysonix_season)
        print("The response of TrackerLinksApi->tracker_links_peak_stats_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_peak_stats_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker link. | 
 **pysonix_season** | **int**| Psysonix season number to filter by. | 

### Return type

[**TrackerPeak**](TrackerPeak.md)

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

# **tracker_links_retrieve**
> TrackerLink tracker_links_retrieve(id, format=format)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    id = 'id_example' # str | 
    format = 'format_example' # str |  (optional)

    try:
        api_response = await api_instance.tracker_links_retrieve(id, format=format)
        print("The response of TrackerLinksApi->tracker_links_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **format** | **str**|  | [optional] 

### Return type

[**TrackerLink**](TrackerLink.md)

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

# **tracker_links_status_partial_update**
> TrackerStatus tracker_links_status_partial_update(id, patched_tracker_status=patched_tracker_status)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.patched_tracker_status import PatchedTrackerStatus
from rscapi.models.tracker_status import TrackerStatus
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker link.
    patched_tracker_status = rscapi.PatchedTrackerStatus() # PatchedTrackerStatus |  (optional)

    try:
        api_response = await api_instance.tracker_links_status_partial_update(id, patched_tracker_status=patched_tracker_status)
        print("The response of TrackerLinksApi->tracker_links_status_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_status_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker link. | 
 **patched_tracker_status** | [**PatchedTrackerStatus**](PatchedTrackerStatus.md)|  | [optional] 

### Return type

[**TrackerStatus**](TrackerStatus.md)

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

# **tracker_links_status_retrieve**
> TrackerStatus tracker_links_status_retrieve(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_status import TrackerStatus
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker link.

    try:
        api_response = await api_instance.tracker_links_status_retrieve(id)
        print("The response of TrackerLinksApi->tracker_links_status_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_status_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker link. | 

### Return type

[**TrackerStatus**](TrackerStatus.md)

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

# **tracker_links_unlink_create**
> TrackerLink tracker_links_unlink_create(id, tracker_link_linking)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
from rscapi.models.tracker_link_linking import TrackerLinkLinking
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker link.
    tracker_link_linking = rscapi.TrackerLinkLinking() # TrackerLinkLinking | 

    try:
        api_response = await api_instance.tracker_links_unlink_create(id, tracker_link_linking)
        print("The response of TrackerLinksApi->tracker_links_unlink_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_unlink_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker link. | 
 **tracker_link_linking** | [**TrackerLinkLinking**](TrackerLinkLinking.md)|  | 

### Return type

[**TrackerLink**](TrackerLink.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


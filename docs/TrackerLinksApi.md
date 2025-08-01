# rscapi.TrackerLinksApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tracker_links_create**](TrackerLinksApi.md#tracker_links_create) | **POST** /tracker-links/ | 
[**tracker_links_delete**](TrackerLinksApi.md#tracker_links_delete) | **DELETE** /tracker-links/{id}/ | 
[**tracker_links_fix_duplicate_links**](TrackerLinksApi.md#tracker_links_fix_duplicate_links) | **GET** /tracker-links/fix_duplicate_links/ | 
[**tracker_links_invalidate_links**](TrackerLinksApi.md#tracker_links_invalidate_links) | **POST** /tracker-links/invalidate_links/ | 
[**tracker_links_link**](TrackerLinksApi.md#tracker_links_link) | **POST** /tracker-links/{id}/link/ | 
[**tracker_links_links_stats**](TrackerLinksApi.md#tracker_links_links_stats) | **GET** /tracker-links/links_stats/ | 
[**tracker_links_list**](TrackerLinksApi.md#tracker_links_list) | **GET** /tracker-links/ | 
[**tracker_links_migrate_pulls**](TrackerLinksApi.md#tracker_links_migrate_pulls) | **POST** /tracker-links/{id}/migrate_pulls/ | 
[**tracker_links_next**](TrackerLinksApi.md#tracker_links_next) | **GET** /tracker-links/next/ | 
[**tracker_links_peak_stats**](TrackerLinksApi.md#tracker_links_peak_stats) | **GET** /tracker-links/{id}/peak_stats/ | 
[**tracker_links_read**](TrackerLinksApi.md#tracker_links_read) | **GET** /tracker-links/{id}/ | 
[**tracker_links_unlink**](TrackerLinksApi.md#tracker_links_unlink) | **POST** /tracker-links/{id}/unlink/ | 


# **tracker_links_create**
> TrackerLink tracker_links_create(data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    data = rscapi.TrackerLink() # TrackerLink | 

    try:
        api_response = await api_instance.tracker_links_create(data)
        print("The response of TrackerLinksApi->tracker_links_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TrackerLink**](TrackerLink.md)|  | 

### Return type

[**TrackerLink**](TrackerLink.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tracker_links_delete**
> tracker_links_delete(id)

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
    api_instance = rscapi.TrackerLinksApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker links.

    try:
        await api_instance.tracker_links_delete(id)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker links. | 

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

# **tracker_links_fix_duplicate_links**
> List[TrackerLink] tracker_links_fix_duplicate_links()

Fixes duplicate tracker links by merging MMR pulls and removing duplicates.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
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
    api_instance = rscapi.TrackerLinksApi(api_client)

    try:
        api_response = await api_instance.tracker_links_fix_duplicate_links()
        print("The response of TrackerLinksApi->tracker_links_fix_duplicate_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_fix_duplicate_links: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **tracker_links_invalidate_links**
> TrackerLinkInvalidateObject tracker_links_invalidate_links(data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link_invalidate_object import TrackerLinkInvalidateObject
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    data = rscapi.TrackerLinkInvalidateObject() # TrackerLinkInvalidateObject | 

    try:
        api_response = await api_instance.tracker_links_invalidate_links(data)
        print("The response of TrackerLinksApi->tracker_links_invalidate_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_invalidate_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TrackerLinkInvalidateObject**](TrackerLinkInvalidateObject.md)|  | 

### Return type

[**TrackerLinkInvalidateObject**](TrackerLinkInvalidateObject.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tracker_links_link**
> TrackerLink tracker_links_link(id, data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
from rscapi.models.tracker_link_linking import TrackerLinkLinking
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker links.
    data = rscapi.TrackerLinkLinking() # TrackerLinkLinking | 

    try:
        api_response = await api_instance.tracker_links_link(id, data)
        print("The response of TrackerLinksApi->tracker_links_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker links. | 
 **data** | [**TrackerLinkLinking**](TrackerLinkLinking.md)|  | 

### Return type

[**TrackerLink**](TrackerLink.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tracker_links_links_stats**
> List[TrackerLinkStats] tracker_links_links_stats()

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link_stats import TrackerLinkStats
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
    api_instance = rscapi.TrackerLinksApi(api_client)

    try:
        api_response = await api_instance.tracker_links_links_stats()
        print("The response of TrackerLinksApi->tracker_links_links_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_links_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
> TrackerLinksList200Response tracker_links_list(status=status, member_name=member_name, discord_id=discord_id, limit=limit, offset=offset)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_links_list200_response import TrackerLinksList200Response
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    status = 'status_example' # str | status (optional)
    member_name = 'member_name_example' # str | member_name (optional)
    discord_id = 56 # int | Member Discord ID (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.tracker_links_list(status=status, member_name=member_name, discord_id=discord_id, limit=limit, offset=offset)
        print("The response of TrackerLinksApi->tracker_links_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| status | [optional] 
 **member_name** | **str**| member_name | [optional] 
 **discord_id** | **int**| Member Discord ID | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**TrackerLinksList200Response**](TrackerLinksList200Response.md)

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

# **tracker_links_migrate_pulls**
> TrackerIDInput tracker_links_migrate_pulls(id, data)

Migrates MMR pulls from one tracker link to another.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_id_input import TrackerIDInput
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker links.
    data = rscapi.TrackerIDInput() # TrackerIDInput | 

    try:
        api_response = await api_instance.tracker_links_migrate_pulls(id, data)
        print("The response of TrackerLinksApi->tracker_links_migrate_pulls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_migrate_pulls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker links. | 
 **data** | [**TrackerIDInput**](TrackerIDInput.md)|  | 

### Return type

[**TrackerIDInput**](TrackerIDInput.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tracker_links_next**
> List[TrackerLink] tracker_links_next(limit=limit)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    limit = 56 # int | Number of tracker links to grab (Default: 1, Max:25) (optional)

    try:
        api_response = await api_instance.tracker_links_next(limit=limit)
        print("The response of TrackerLinksApi->tracker_links_next:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_next: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **tracker_links_peak_stats**
> TrackerPeak tracker_links_peak_stats(id, pysonix_season)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_peak import TrackerPeak
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker links.
    pysonix_season = 56 # int | Psysonix season number to filter by.

    try:
        api_response = await api_instance.tracker_links_peak_stats(id, pysonix_season)
        print("The response of TrackerLinksApi->tracker_links_peak_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_peak_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker links. | 
 **pysonix_season** | **int**| Psysonix season number to filter by. | 

### Return type

[**TrackerPeak**](TrackerPeak.md)

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

# **tracker_links_read**
> TrackerLink tracker_links_read(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker links.

    try:
        api_response = await api_instance.tracker_links_read(id)
        print("The response of TrackerLinksApi->tracker_links_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker links. | 

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

# **tracker_links_unlink**
> TrackerLink tracker_links_unlink(id, data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_link import TrackerLink
from rscapi.models.tracker_link_linking import TrackerLinkLinking
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
    api_instance = rscapi.TrackerLinksApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker links.
    data = rscapi.TrackerLinkLinking() # TrackerLinkLinking | 

    try:
        api_response = await api_instance.tracker_links_unlink(id, data)
        print("The response of TrackerLinksApi->tracker_links_unlink:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_unlink: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker links. | 
 **data** | [**TrackerLinkLinking**](TrackerLinkLinking.md)|  | 

### Return type

[**TrackerLink**](TrackerLink.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


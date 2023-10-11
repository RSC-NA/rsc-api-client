# openapi_client.TrackerLinksApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tracker_links_create**](TrackerLinksApi.md#tracker_links_create) | **POST** /tracker-links/ | 
[**tracker_links_delete**](TrackerLinksApi.md#tracker_links_delete) | **DELETE** /tracker-links/{id}/ | 
[**tracker_links_invalidate_links**](TrackerLinksApi.md#tracker_links_invalidate_links) | **POST** /tracker-links/invalidate_links/ | 
[**tracker_links_links_stats**](TrackerLinksApi.md#tracker_links_links_stats) | **GET** /tracker-links/links_stats/ | 
[**tracker_links_list**](TrackerLinksApi.md#tracker_links_list) | **GET** /tracker-links/ | 
[**tracker_links_next**](TrackerLinksApi.md#tracker_links_next) | **GET** /tracker-links/next/ | 
[**tracker_links_partial_update**](TrackerLinksApi.md#tracker_links_partial_update) | **PATCH** /tracker-links/{id}/ | 
[**tracker_links_read**](TrackerLinksApi.md#tracker_links_read) | **GET** /tracker-links/{id}/ | 
[**tracker_links_update**](TrackerLinksApi.md#tracker_links_update) | **PUT** /tracker-links/{id}/ | 


# **tracker_links_create**
> TrackerLink tracker_links_create(data)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.tracker_link import TrackerLink
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
    api_instance = openapi_client.TrackerLinksApi(api_client)
    data = openapi_client.TrackerLink() # TrackerLink | 

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

[api_key](../README.md#api_key)

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
    api_instance = openapi_client.TrackerLinksApi(api_client)
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tracker_links_invalidate_links**
> TrackerLinkInvalidateObject tracker_links_invalidate_links(data)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.tracker_link_invalidate_object import TrackerLinkInvalidateObject
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
    api_instance = openapi_client.TrackerLinksApi(api_client)
    data = openapi_client.TrackerLinkInvalidateObject() # TrackerLinkInvalidateObject | 

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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tracker_links_links_stats**
> List[TrackerLink] tracker_links_links_stats(status=status, member=member)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.tracker_link import TrackerLink
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
    api_instance = openapi_client.TrackerLinksApi(api_client)
    status = 'status_example' # str | status (optional)
    member = 'member_example' # str | member (optional)

    try:
        api_response = await api_instance.tracker_links_links_stats(status=status, member=member)
        print("The response of TrackerLinksApi->tracker_links_links_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_links_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| status | [optional] 
 **member** | **str**| member | [optional] 

### Return type

[**List[TrackerLink]**](TrackerLink.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tracker_links_list**
> List[TrackerLink] tracker_links_list(status=status, member=member)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.tracker_link import TrackerLink
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
    api_instance = openapi_client.TrackerLinksApi(api_client)
    status = 'status_example' # str | Tracker Link Status (Pulled, Failed, etc.) (optional)
    member = 'member_example' # str | member (optional)

    try:
        api_response = await api_instance.tracker_links_list(status=status, member=member)
        print("The response of TrackerLinksApi->tracker_links_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Tracker Link Status (Pulled, Failed, etc.) | [optional] 
 **member** | **str**| member | [optional] 

### Return type

[**List[TrackerLink]**](TrackerLink.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tracker_links_next**
> List[TrackerLink] tracker_links_next(status=status, member=member, limit=limit)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.tracker_link import TrackerLink
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
    api_instance = openapi_client.TrackerLinksApi(api_client)
    status = 'status_example' # str | status (optional)
    member = 'member_example' # str | member (optional)
    limit = 56 # int | Number of tracker links to grab (Default: 1, Max:25) (optional)

    try:
        api_response = await api_instance.tracker_links_next(status=status, member=member, limit=limit)
        print("The response of TrackerLinksApi->tracker_links_next:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_next: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| status | [optional] 
 **member** | **str**| member | [optional] 
 **limit** | **int**| Number of tracker links to grab (Default: 1, Max:25) | [optional] 

### Return type

[**List[TrackerLink]**](TrackerLink.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tracker_links_partial_update**
> TrackerLink tracker_links_partial_update(id, data)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.tracker_link import TrackerLink
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
    api_instance = openapi_client.TrackerLinksApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker links.
    data = openapi_client.TrackerLink() # TrackerLink | 

    try:
        api_response = await api_instance.tracker_links_partial_update(id, data)
        print("The response of TrackerLinksApi->tracker_links_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker links. | 
 **data** | [**TrackerLink**](TrackerLink.md)|  | 

### Return type

[**TrackerLink**](TrackerLink.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tracker_links_read**
> TrackerLink tracker_links_read(id)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.tracker_link import TrackerLink
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
    api_instance = openapi_client.TrackerLinksApi(api_client)
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tracker_links_update**
> TrackerLink tracker_links_update(id, data)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.tracker_link import TrackerLink
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
    api_instance = openapi_client.TrackerLinksApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker links.
    data = openapi_client.TrackerLink() # TrackerLink | 

    try:
        api_response = await api_instance.tracker_links_update(id, data)
        print("The response of TrackerLinksApi->tracker_links_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerLinksApi->tracker_links_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker links. | 
 **data** | [**TrackerLink**](TrackerLink.md)|  | 

### Return type

[**TrackerLink**](TrackerLink.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


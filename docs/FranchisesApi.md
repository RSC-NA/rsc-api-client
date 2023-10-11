# openapi_client.FranchisesApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**franchises_create**](FranchisesApi.md#franchises_create) | **POST** /franchises/ | 
[**franchises_delete**](FranchisesApi.md#franchises_delete) | **DELETE** /franchises/{id}/ | 
[**franchises_list**](FranchisesApi.md#franchises_list) | **GET** /franchises/ | 
[**franchises_partial_update**](FranchisesApi.md#franchises_partial_update) | **PATCH** /franchises/{id}/ | 
[**franchises_read**](FranchisesApi.md#franchises_read) | **GET** /franchises/{id}/ | 
[**franchises_transfer_franchise**](FranchisesApi.md#franchises_transfer_franchise) | **PUT** /franchises/{id}/transfer_franchise/ | 
[**franchises_update**](FranchisesApi.md#franchises_update) | **PUT** /franchises/{id}/ | 
[**franchises_upload_logo**](FranchisesApi.md#franchises_upload_logo) | **PUT** /franchises/{id}/upload_logo/ | 


# **franchises_create**
> FranchiseList franchises_create(data)



Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.franchise_list import FranchiseList
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
    api_instance = openapi_client.FranchisesApi(api_client)
    data = openapi_client.FranchiseList() # FranchiseList | 

    try:
        api_response = await api_instance.franchises_create(data)
        print("The response of FranchisesApi->franchises_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FranchiseList**](FranchiseList.md)|  | 

### Return type

[**FranchiseList**](FranchiseList.md)

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

# **franchises_delete**
> franchises_delete(id)



Viewset for the franchise model. Contains endpoints related to working with franchises.

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
    api_instance = openapi_client.FranchisesApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.

    try:
        await api_instance.franchises_delete(id)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 

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

# **franchises_list**
> List[FranchiseList] franchises_list(prefix=prefix, league=league, gm_name=gm_name, name=name, tier=tier, tier_name=tier_name)



Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.franchise_list import FranchiseList
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
    api_instance = openapi_client.FranchisesApi(api_client)
    prefix = 'prefix_example' # str | prefix (optional)
    league = 'league_example' # str | league (optional)
    gm_name = 'gm_name_example' # str | gm_name (optional)
    name = 'name_example' # str | name (optional)
    tier = 'tier_example' # str | tier (optional)
    tier_name = 'tier_name_example' # str | tier_name (optional)

    try:
        api_response = await api_instance.franchises_list(prefix=prefix, league=league, gm_name=gm_name, name=name, tier=tier, tier_name=tier_name)
        print("The response of FranchisesApi->franchises_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| prefix | [optional] 
 **league** | **str**| league | [optional] 
 **gm_name** | **str**| gm_name | [optional] 
 **name** | **str**| name | [optional] 
 **tier** | **str**| tier | [optional] 
 **tier_name** | **str**| tier_name | [optional] 

### Return type

[**List[FranchiseList]**](FranchiseList.md)

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

# **franchises_partial_update**
> FranchiseList franchises_partial_update(id, data)



Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.franchise_list import FranchiseList
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
    api_instance = openapi_client.FranchisesApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.
    data = openapi_client.FranchiseList() # FranchiseList | 

    try:
        api_response = await api_instance.franchises_partial_update(id, data)
        print("The response of FranchisesApi->franchises_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 
 **data** | [**FranchiseList**](FranchiseList.md)|  | 

### Return type

[**FranchiseList**](FranchiseList.md)

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

# **franchises_read**
> Franchise franchises_read(id)



Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.franchise import Franchise
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
    api_instance = openapi_client.FranchisesApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.

    try:
        api_response = await api_instance.franchises_read(id)
        print("The response of FranchisesApi->franchises_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_read: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 

### Return type

[**Franchise**](Franchise.md)

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

# **franchises_transfer_franchise**
> TransferFranchise franchises_transfer_franchise(id, data)



PUT /franchises/{id}/transfer_franchise/

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.transfer_franchise import TransferFranchise
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
    api_instance = openapi_client.FranchisesApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.
    data = openapi_client.TransferFranchise() # TransferFranchise | 

    try:
        api_response = await api_instance.franchises_transfer_franchise(id, data)
        print("The response of FranchisesApi->franchises_transfer_franchise:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_transfer_franchise: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 
 **data** | [**TransferFranchise**](TransferFranchise.md)|  | 

### Return type

[**TransferFranchise**](TransferFranchise.md)

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

# **franchises_update**
> FranchiseList franchises_update(id, data)



Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.franchise_list import FranchiseList
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
    api_instance = openapi_client.FranchisesApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.
    data = openapi_client.FranchiseList() # FranchiseList | 

    try:
        api_response = await api_instance.franchises_update(id, data)
        print("The response of FranchisesApi->franchises_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 
 **data** | [**FranchiseList**](FranchiseList.md)|  | 

### Return type

[**FranchiseList**](FranchiseList.md)

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

# **franchises_upload_logo**
> FranchiseList franchises_upload_logo(id, logo)



Update a franchise logo.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.franchise_list import FranchiseList
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
    api_instance = openapi_client.FranchisesApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.
    logo = None # bytearray | Logo content.

    try:
        api_response = await api_instance.franchises_upload_logo(id, logo)
        print("The response of FranchisesApi->franchises_upload_logo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_upload_logo: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 
 **logo** | **bytearray**| Logo content. | 

### Return type

[**FranchiseList**](FranchiseList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


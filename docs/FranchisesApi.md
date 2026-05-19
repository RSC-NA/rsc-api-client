# rscapi.FranchisesApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**franchises_create**](FranchisesApi.md#franchises_create) | **POST** /franchises/ | 
[**franchises_destroy**](FranchisesApi.md#franchises_destroy) | **DELETE** /franchises/{id}/ | 
[**franchises_list**](FranchisesApi.md#franchises_list) | **GET** /franchises/ | 
[**franchises_logo_retrieve**](FranchisesApi.md#franchises_logo_retrieve) | **GET** /franchises/{id}/logo/ | 
[**franchises_partial_update**](FranchisesApi.md#franchises_partial_update) | **PATCH** /franchises/{id}/ | 
[**franchises_rebrand_update**](FranchisesApi.md#franchises_rebrand_update) | **PUT** /franchises/{id}/rebrand/ | 
[**franchises_retrieve**](FranchisesApi.md#franchises_retrieve) | **GET** /franchises/{id}/ | 
[**franchises_transfer_franchise_update**](FranchisesApi.md#franchises_transfer_franchise_update) | **PUT** /franchises/{id}/transfer_franchise/ | 
[**franchises_update**](FranchisesApi.md#franchises_update) | **PUT** /franchises/{id}/ | 
[**franchises_upload_logo_update**](FranchisesApi.md#franchises_upload_logo_update) | **PUT** /franchises/{id}/upload_logo/ | 


# **franchises_create**
> Franchise franchises_create(franchise)

Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise import Franchise
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
    api_instance = rscapi.FranchisesApi(api_client)
    franchise = rscapi.Franchise() # Franchise | 

    try:
        api_response = await api_instance.franchises_create(franchise)
        print("The response of FranchisesApi->franchises_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **franchise** | [**Franchise**](Franchise.md)|  | 

### Return type

[**Franchise**](Franchise.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **franchises_destroy**
> franchises_destroy(id)

Viewset for the franchise model. Contains endpoints related to working with franchises.

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
    api_instance = rscapi.FranchisesApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.

    try:
        await api_instance.franchises_destroy(id)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 

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

# **franchises_list**
> List[FranchiseList] franchises_list(gm_discord_id=gm_discord_id, gm_name=gm_name, league=league, name=name, prefix=prefix, tier=tier, tier_name=tier_name)

Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise_list import FranchiseList
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
    api_instance = rscapi.FranchisesApi(api_client)
    gm_discord_id = 56 # int | Discord id of GM (optional)
    gm_name = 'gm_name_example' # str | GM Name Contains (optional)
    league = 56 # int | League id (optional)
    name = 'name_example' # str | Franchise Name Contains (optional)
    prefix = 'prefix_example' # str |  (optional)
    tier = 56 # int | ID of Tier players are in. (optional)
    tier_name = ['tier_name_example'] # List[str] | Franchise With Tiers (Using Tier Name) (optional)

    try:
        api_response = await api_instance.franchises_list(gm_discord_id=gm_discord_id, gm_name=gm_name, league=league, name=name, prefix=prefix, tier=tier, tier_name=tier_name)
        print("The response of FranchisesApi->franchises_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gm_discord_id** | **int**| Discord id of GM | [optional] 
 **gm_name** | **str**| GM Name Contains | [optional] 
 **league** | **int**| League id | [optional] 
 **name** | **str**| Franchise Name Contains | [optional] 
 **prefix** | **str**|  | [optional] 
 **tier** | **int**| ID of Tier players are in. | [optional] 
 **tier_name** | [**List[str]**](str.md)| Franchise With Tiers (Using Tier Name) | [optional] 

### Return type

[**List[FranchiseList]**](FranchiseList.md)

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

# **franchises_logo_retrieve**
> FranchiseLogo franchises_logo_retrieve(id)

Get direct link for logo of a franchise

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise_logo import FranchiseLogo
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
    api_instance = rscapi.FranchisesApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.

    try:
        api_response = await api_instance.franchises_logo_retrieve(id)
        print("The response of FranchisesApi->franchises_logo_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_logo_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 

### Return type

[**FranchiseLogo**](FranchiseLogo.md)

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

# **franchises_partial_update**
> Franchise franchises_partial_update(id, patched_franchise=patched_franchise)

Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise import Franchise
from rscapi.models.patched_franchise import PatchedFranchise
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
    api_instance = rscapi.FranchisesApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.
    patched_franchise = rscapi.PatchedFranchise() # PatchedFranchise |  (optional)

    try:
        api_response = await api_instance.franchises_partial_update(id, patched_franchise=patched_franchise)
        print("The response of FranchisesApi->franchises_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 
 **patched_franchise** | [**PatchedFranchise**](PatchedFranchise.md)|  | [optional] 

### Return type

[**Franchise**](Franchise.md)

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

# **franchises_rebrand_update**
> Franchise franchises_rebrand_update(id, franchise_rebrand)

Rebrand a franchise.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise import Franchise
from rscapi.models.franchise_rebrand import FranchiseRebrand
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
    api_instance = rscapi.FranchisesApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.
    franchise_rebrand = rscapi.FranchiseRebrand() # FranchiseRebrand | 

    try:
        api_response = await api_instance.franchises_rebrand_update(id, franchise_rebrand)
        print("The response of FranchisesApi->franchises_rebrand_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_rebrand_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 
 **franchise_rebrand** | [**FranchiseRebrand**](FranchiseRebrand.md)|  | 

### Return type

[**Franchise**](Franchise.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **franchises_retrieve**
> Franchise franchises_retrieve(id)

Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise import Franchise
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
    api_instance = rscapi.FranchisesApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.

    try:
        api_response = await api_instance.franchises_retrieve(id)
        print("The response of FranchisesApi->franchises_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 

### Return type

[**Franchise**](Franchise.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **franchises_transfer_franchise_update**
> Franchise franchises_transfer_franchise_update(id, franchise_transfer_request)

Transfer a franchise to a new general manager in the specified league.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise import Franchise
from rscapi.models.franchise_transfer_request import FranchiseTransferRequest
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
    api_instance = rscapi.FranchisesApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.
    franchise_transfer_request = rscapi.FranchiseTransferRequest() # FranchiseTransferRequest | 

    try:
        api_response = await api_instance.franchises_transfer_franchise_update(id, franchise_transfer_request)
        print("The response of FranchisesApi->franchises_transfer_franchise_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_transfer_franchise_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 
 **franchise_transfer_request** | [**FranchiseTransferRequest**](FranchiseTransferRequest.md)|  | 

### Return type

[**Franchise**](Franchise.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |
**404** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **franchises_update**
> Franchise franchises_update(id, franchise)

Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise import Franchise
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
    api_instance = rscapi.FranchisesApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.
    franchise = rscapi.Franchise() # Franchise | 

    try:
        api_response = await api_instance.franchises_update(id, franchise)
        print("The response of FranchisesApi->franchises_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 
 **franchise** | [**Franchise**](Franchise.md)|  | 

### Return type

[**Franchise**](Franchise.md)

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

# **franchises_upload_logo_update**
> Franchise franchises_upload_logo_update(id, logo)

Update a franchise logo.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise import Franchise
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
    api_instance = rscapi.FranchisesApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.
    logo = None # bytes | Logo content.

    try:
        api_response = await api_instance.franchises_upload_logo_update(id, logo)
        print("The response of FranchisesApi->franchises_upload_logo_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_upload_logo_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 
 **logo** | **bytes**| Logo content. | 

### Return type

[**Franchise**](Franchise.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


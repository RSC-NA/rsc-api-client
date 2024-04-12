# rscapi.FranchisesApi

All URIs are relative to *http://localhost:3000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**franchises_create**](FranchisesApi.md#franchises_create) | **POST** /franchises/ | 
[**franchises_delete**](FranchisesApi.md#franchises_delete) | **DELETE** /franchises/{id}/ | 
[**franchises_list**](FranchisesApi.md#franchises_list) | **GET** /franchises/ | 
[**franchises_logo**](FranchisesApi.md#franchises_logo) | **GET** /franchises/{id}/logo/ | 
[**franchises_partial_update**](FranchisesApi.md#franchises_partial_update) | **PATCH** /franchises/{id}/ | 
[**franchises_read**](FranchisesApi.md#franchises_read) | **GET** /franchises/{id}/ | 
[**franchises_rebrand**](FranchisesApi.md#franchises_rebrand) | **PUT** /franchises/{id}/rebrand/ | 
[**franchises_transfer_franchise**](FranchisesApi.md#franchises_transfer_franchise) | **PUT** /franchises/{id}/transfer_franchise/ | 
[**franchises_update**](FranchisesApi.md#franchises_update) | **PUT** /franchises/{id}/ | 
[**franchises_upload_logo**](FranchisesApi.md#franchises_upload_logo) | **PUT** /franchises/{id}/upload_logo/ | 


# **franchises_create**
> Franchise franchises_create(data)



Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise import Franchise
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://localhost:3000/api/v1"
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
    data = rscapi.Franchise() # Franchise | 

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
 **data** | [**Franchise**](Franchise.md)|  | 

### Return type

[**Franchise**](Franchise.md)

### Authorization

[Api-Key](../README.md#Api-Key)

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

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://localhost:3000/api/v1"
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

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **franchises_list**
> List[FranchiseList] franchises_list(prefix=prefix, league=league, gm_name=gm_name, gm_discord_id=gm_discord_id, name=name, tier=tier, tier_name=tier_name)



Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise_list import FranchiseList
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://localhost:3000/api/v1"
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
    prefix = 'prefix_example' # str | prefix (optional)
    league = 56 # int | League id (optional)
    gm_name = 'gm_name_example' # str | gm_name (optional)
    gm_discord_id = 56 # int | Discord id of GM (optional)
    name = 'name_example' # str | name (optional)
    tier = 56 # int | ID of Tier players are in. (optional)
    tier_name = 'tier_name_example' # str | tier_name (optional)

    try:
        api_response = await api_instance.franchises_list(prefix=prefix, league=league, gm_name=gm_name, gm_discord_id=gm_discord_id, name=name, tier=tier, tier_name=tier_name)
        print("The response of FranchisesApi->franchises_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| prefix | [optional] 
 **league** | **int**| League id | [optional] 
 **gm_name** | **str**| gm_name | [optional] 
 **gm_discord_id** | **int**| Discord id of GM | [optional] 
 **name** | **str**| name | [optional] 
 **tier** | **int**| ID of Tier players are in. | [optional] 
 **tier_name** | **str**| tier_name | [optional] 

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

# **franchises_logo**
> FranchiseLogo franchises_logo(id)



Get direct link for logo of a franchise

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise_logo import FranchiseLogo
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://localhost:3000/api/v1"
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
        api_response = await api_instance.franchises_logo(id)
        print("The response of FranchisesApi->franchises_logo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_logo: %s\n" % e)
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
> Franchise franchises_partial_update(id, data)



Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise import Franchise
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://localhost:3000/api/v1"
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
    data = rscapi.Franchise() # Franchise | 

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
 **data** | [**Franchise**](Franchise.md)|  | 

### Return type

[**Franchise**](Franchise.md)

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

# **franchises_read**
> Franchise franchises_read(id)



Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise import Franchise
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://localhost:3000/api/v1"
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

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **franchises_rebrand**
> Franchise franchises_rebrand(id, data)



Rebrand a franchise.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise import Franchise
from rscapi.models.rebrand_a_franchise import RebrandAFranchise
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://localhost:3000/api/v1"
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
    data = rscapi.RebrandAFranchise() # RebrandAFranchise | 

    try:
        api_response = await api_instance.franchises_rebrand(id, data)
        print("The response of FranchisesApi->franchises_rebrand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FranchisesApi->franchises_rebrand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 
 **data** | [**RebrandAFranchise**](RebrandAFranchise.md)|  | 

### Return type

[**Franchise**](Franchise.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **franchises_transfer_franchise**
> Franchise franchises_transfer_franchise(id, data)



PUT /franchises/{id}/transfer_franchise/

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise import Franchise
from rscapi.models.transfer_franchise import TransferFranchise
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://localhost:3000/api/v1"
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
    data = rscapi.TransferFranchise() # TransferFranchise | 

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

[**Franchise**](Franchise.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |
**404** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **franchises_update**
> Franchise franchises_update(id, data)



Viewset for the franchise model. Contains endpoints related to working with franchises.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise import Franchise
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://localhost:3000/api/v1"
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
    data = rscapi.Franchise() # Franchise | 

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
 **data** | [**Franchise**](Franchise.md)|  | 

### Return type

[**Franchise**](Franchise.md)

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

# **franchises_upload_logo**
> Franchise franchises_upload_logo(id, logo)



Update a franchise logo.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise import Franchise
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "http://localhost:3000/api/v1"
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


# rscapi.NumbersApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**numbers_mmr_bulk_submit**](NumbersApi.md#numbers_mmr_bulk_submit) | **POST** /numbers/mmr/bulk_submit/ | 
[**numbers_mmr_create**](NumbersApi.md#numbers_mmr_create) | **POST** /numbers/mmr/ | 
[**numbers_mmr_delete**](NumbersApi.md#numbers_mmr_delete) | **DELETE** /numbers/mmr/{id}/ | 
[**numbers_mmr_list**](NumbersApi.md#numbers_mmr_list) | **GET** /numbers/mmr/ | 
[**numbers_mmr_partial_update**](NumbersApi.md#numbers_mmr_partial_update) | **PATCH** /numbers/mmr/{id}/ | 
[**numbers_mmr_read**](NumbersApi.md#numbers_mmr_read) | **GET** /numbers/mmr/{id}/ | 
[**numbers_mmr_update**](NumbersApi.md#numbers_mmr_update) | **PUT** /numbers/mmr/{id}/ | 


# **numbers_mmr_bulk_submit**
> List[PlayerMMR] numbers_mmr_bulk_submit(data)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.bulk_mmr_schema_submission import BulkMMRSchemaSubmission
from rscapi.models.player_mmr import PlayerMMR
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
    api_instance = rscapi.NumbersApi(api_client)
    data = rscapi.BulkMMRSchemaSubmission() # BulkMMRSchemaSubmission | 

    try:
        api_response = await api_instance.numbers_mmr_bulk_submit(data)
        print("The response of NumbersApi->numbers_mmr_bulk_submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NumbersApi->numbers_mmr_bulk_submit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**BulkMMRSchemaSubmission**](BulkMMRSchemaSubmission.md)|  | 

### Return type

[**List[PlayerMMR]**](PlayerMMR.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numbers_mmr_create**
> PlayerMMR numbers_mmr_create(data)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_mmr import PlayerMMR
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
    api_instance = rscapi.NumbersApi(api_client)
    data = rscapi.PlayerMMR() # PlayerMMR | 

    try:
        api_response = await api_instance.numbers_mmr_create(data)
        print("The response of NumbersApi->numbers_mmr_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NumbersApi->numbers_mmr_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PlayerMMR**](PlayerMMR.md)|  | 

### Return type

[**PlayerMMR**](PlayerMMR.md)

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

# **numbers_mmr_delete**
> numbers_mmr_delete(id)



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
    api_instance = rscapi.NumbersApi(api_client)
    id = 56 # int | A unique integer value identifying this player mmr pull.

    try:
        await api_instance.numbers_mmr_delete(id)
    except Exception as e:
        print("Exception when calling NumbersApi->numbers_mmr_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this player mmr pull. | 

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

# **numbers_mmr_list**
> List[PlayerMMR] numbers_mmr_list(pulled=pulled, rscid=rscid, discord_id=discord_id, rscid_begin=rscid_begin, rscid_end=rscid_end, psyonix_season=psyonix_season, pulled_before=pulled_before, pulled_after=pulled_after)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_mmr import PlayerMMR
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
    api_instance = rscapi.NumbersApi(api_client)
    pulled = 'pulled_example' # str | pulled (optional)
    rscid = 'rscid_example' # str | Specific Member RSC ID (E.g: RSC002918) (optional)
    discord_id = 56 # int | Member discord ID (optional)
    rscid_begin = 'rscid_begin_example' # str | Starting RSC ID for a range of RSC IDs (optional)
    rscid_end = 'rscid_end_example' # str | Ending RSC ID for a range of RSC IDs (optional)
    psyonix_season = 'psyonix_season_example' # str | psyonix_season (optional)
    pulled_before = 'pulled_before_example' # str | MMR pulled before date in YYYY-MM-DD format. (optional)
    pulled_after = 'pulled_after_example' # str | MMR pulled after date in YYYY-MM-DD format. (optional)

    try:
        api_response = await api_instance.numbers_mmr_list(pulled=pulled, rscid=rscid, discord_id=discord_id, rscid_begin=rscid_begin, rscid_end=rscid_end, psyonix_season=psyonix_season, pulled_before=pulled_before, pulled_after=pulled_after)
        print("The response of NumbersApi->numbers_mmr_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NumbersApi->numbers_mmr_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulled** | **str**| pulled | [optional] 
 **rscid** | **str**| Specific Member RSC ID (E.g: RSC002918) | [optional] 
 **discord_id** | **int**| Member discord ID | [optional] 
 **rscid_begin** | **str**| Starting RSC ID for a range of RSC IDs | [optional] 
 **rscid_end** | **str**| Ending RSC ID for a range of RSC IDs | [optional] 
 **psyonix_season** | **str**| psyonix_season | [optional] 
 **pulled_before** | **str**| MMR pulled before date in YYYY-MM-DD format. | [optional] 
 **pulled_after** | **str**| MMR pulled after date in YYYY-MM-DD format. | [optional] 

### Return type

[**List[PlayerMMR]**](PlayerMMR.md)

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

# **numbers_mmr_partial_update**
> PlayerMMR numbers_mmr_partial_update(id, data)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_mmr import PlayerMMR
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
    api_instance = rscapi.NumbersApi(api_client)
    id = 56 # int | A unique integer value identifying this player mmr pull.
    data = rscapi.PlayerMMR() # PlayerMMR | 

    try:
        api_response = await api_instance.numbers_mmr_partial_update(id, data)
        print("The response of NumbersApi->numbers_mmr_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NumbersApi->numbers_mmr_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this player mmr pull. | 
 **data** | [**PlayerMMR**](PlayerMMR.md)|  | 

### Return type

[**PlayerMMR**](PlayerMMR.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numbers_mmr_read**
> PlayerMMR numbers_mmr_read(id)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_mmr import PlayerMMR
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
    api_instance = rscapi.NumbersApi(api_client)
    id = 56 # int | A unique integer value identifying this player mmr pull.

    try:
        api_response = await api_instance.numbers_mmr_read(id)
        print("The response of NumbersApi->numbers_mmr_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NumbersApi->numbers_mmr_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this player mmr pull. | 

### Return type

[**PlayerMMR**](PlayerMMR.md)

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

# **numbers_mmr_update**
> PlayerMMR numbers_mmr_update(id, data)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_mmr import PlayerMMR
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
    api_instance = rscapi.NumbersApi(api_client)
    id = 56 # int | A unique integer value identifying this player mmr pull.
    data = rscapi.PlayerMMR() # PlayerMMR | 

    try:
        api_response = await api_instance.numbers_mmr_update(id, data)
        print("The response of NumbersApi->numbers_mmr_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NumbersApi->numbers_mmr_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this player mmr pull. | 
 **data** | [**PlayerMMR**](PlayerMMR.md)|  | 

### Return type

[**PlayerMMR**](PlayerMMR.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


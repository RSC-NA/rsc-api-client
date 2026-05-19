# rscapi.NumbersApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**numbers_mmr_bulk_submit_create**](NumbersApi.md#numbers_mmr_bulk_submit_create) | **POST** /numbers/mmr/bulk_submit/ | 
[**numbers_mmr_create**](NumbersApi.md#numbers_mmr_create) | **POST** /numbers/mmr/ | 
[**numbers_mmr_destroy**](NumbersApi.md#numbers_mmr_destroy) | **DELETE** /numbers/mmr/{id}/ | 
[**numbers_mmr_list**](NumbersApi.md#numbers_mmr_list) | **GET** /numbers/mmr/ | 
[**numbers_mmr_partial_update**](NumbersApi.md#numbers_mmr_partial_update) | **PATCH** /numbers/mmr/{id}/ | 
[**numbers_mmr_retrieve**](NumbersApi.md#numbers_mmr_retrieve) | **GET** /numbers/mmr/{id}/ | 
[**numbers_mmr_update**](NumbersApi.md#numbers_mmr_update) | **PUT** /numbers/mmr/{id}/ | 


# **numbers_mmr_bulk_submit_create**
> PaginatedPlayerMMRList numbers_mmr_bulk_submit_create(discord_id=discord_id, format=format, limit=limit, offset=offset, psyonix_season=psyonix_season, pulled=pulled, pulled_after_after=pulled_after_after, pulled_after_before=pulled_after_before, pulled_before_after=pulled_before_after, pulled_before_before=pulled_before_before, rscid=rscid, rscid_begin=rscid_begin, rscid_end=rscid_end, bulk_mmr_schema_submission=bulk_mmr_schema_submission)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.bulk_mmr_schema_submission import BulkMMRSchemaSubmission
from rscapi.models.paginated_player_mmr_list import PaginatedPlayerMMRList
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
    api_instance = rscapi.NumbersApi(api_client)
    discord_id = 56 # int | Member discord ID. (optional)
    format = 'format_example' # str |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    psyonix_season = 56 # int | Psyonix Season (as internal value. E.g F2P S14 = 28) (optional)
    pulled = '2013-10-20T19:20:30+01:00' # datetime | Specific date pulled (YYYY-MM-DD) (optional)
    pulled_after_after = '2013-10-20' # date | Date pulled is greater than or equal to this date (YYYY-MM-DD) (optional)
    pulled_after_before = '2013-10-20' # date | Date pulled is greater than or equal to this date (YYYY-MM-DD) (optional)
    pulled_before_after = '2013-10-20' # date | Date pulled is less than or equal to this date (YYYY-MM-DD) (optional)
    pulled_before_before = '2013-10-20' # date | Date pulled is less than or equal to this date (YYYY-MM-DD) (optional)
    rscid = 'rscid_example' # str |  (optional)
    rscid_begin = 'rscid_begin_example' # str | Starting RSC ID (optional)
    rscid_end = 'rscid_end_example' # str | Ending RSC ID (optional)
    bulk_mmr_schema_submission = rscapi.BulkMMRSchemaSubmission() # BulkMMRSchemaSubmission |  (optional)

    try:
        api_response = await api_instance.numbers_mmr_bulk_submit_create(discord_id=discord_id, format=format, limit=limit, offset=offset, psyonix_season=psyonix_season, pulled=pulled, pulled_after_after=pulled_after_after, pulled_after_before=pulled_after_before, pulled_before_after=pulled_before_after, pulled_before_before=pulled_before_before, rscid=rscid, rscid_begin=rscid_begin, rscid_end=rscid_end, bulk_mmr_schema_submission=bulk_mmr_schema_submission)
        print("The response of NumbersApi->numbers_mmr_bulk_submit_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NumbersApi->numbers_mmr_bulk_submit_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discord_id** | **int**| Member discord ID. | [optional] 
 **format** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **psyonix_season** | **int**| Psyonix Season (as internal value. E.g F2P S14 &#x3D; 28) | [optional] 
 **pulled** | **datetime**| Specific date pulled (YYYY-MM-DD) | [optional] 
 **pulled_after_after** | **date**| Date pulled is greater than or equal to this date (YYYY-MM-DD) | [optional] 
 **pulled_after_before** | **date**| Date pulled is greater than or equal to this date (YYYY-MM-DD) | [optional] 
 **pulled_before_after** | **date**| Date pulled is less than or equal to this date (YYYY-MM-DD) | [optional] 
 **pulled_before_before** | **date**| Date pulled is less than or equal to this date (YYYY-MM-DD) | [optional] 
 **rscid** | **str**|  | [optional] 
 **rscid_begin** | **str**| Starting RSC ID | [optional] 
 **rscid_end** | **str**| Ending RSC ID | [optional] 
 **bulk_mmr_schema_submission** | [**BulkMMRSchemaSubmission**](BulkMMRSchemaSubmission.md)|  | [optional] 

### Return type

[**PaginatedPlayerMMRList**](PaginatedPlayerMMRList.md)

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
> PlayerMMR numbers_mmr_create(player_mmr, format=format)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_mmr import PlayerMMR
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
    api_instance = rscapi.NumbersApi(api_client)
    player_mmr = rscapi.PlayerMMR() # PlayerMMR | 
    format = 'format_example' # str |  (optional)

    try:
        api_response = await api_instance.numbers_mmr_create(player_mmr, format=format)
        print("The response of NumbersApi->numbers_mmr_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NumbersApi->numbers_mmr_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_mmr** | [**PlayerMMR**](PlayerMMR.md)|  | 
 **format** | **str**|  | [optional] 

### Return type

[**PlayerMMR**](PlayerMMR.md)

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

# **numbers_mmr_destroy**
> numbers_mmr_destroy(id, format=format)

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
    api_instance = rscapi.NumbersApi(api_client)
    id = 56 # int | A unique integer value identifying this player mmr pull.
    format = 'format_example' # str |  (optional)

    try:
        await api_instance.numbers_mmr_destroy(id, format=format)
    except Exception as e:
        print("Exception when calling NumbersApi->numbers_mmr_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this player mmr pull. | 
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

# **numbers_mmr_list**
> PaginatedPlayerMMRList numbers_mmr_list(discord_id=discord_id, format=format, limit=limit, offset=offset, psyonix_season=psyonix_season, pulled=pulled, pulled_after=pulled_after, pulled_after_after=pulled_after_after, pulled_after_before=pulled_after_before, pulled_before=pulled_before, pulled_before_after=pulled_before_after, pulled_before_before=pulled_before_before, rscid=rscid, rscid_begin=rscid_begin, rscid_end=rscid_end)

List all player MMRs.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.paginated_player_mmr_list import PaginatedPlayerMMRList
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
    api_instance = rscapi.NumbersApi(api_client)
    discord_id = 56 # int | Member discord ID (optional)
    format = 'format_example' # str |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    psyonix_season = 56 # int | Psyonix Season Number (optional)
    pulled = '2013-10-20T19:20:30+01:00' # datetime | Specific date pulled (YYYY-MM-DD) (optional)
    pulled_after = 'pulled_after_example' # str | MMR pulled after date in YYYY-MM-DD format. (optional)
    pulled_after_after = '2013-10-20' # date | Date pulled is greater than or equal to this date (YYYY-MM-DD) (optional)
    pulled_after_before = '2013-10-20' # date | Date pulled is greater than or equal to this date (YYYY-MM-DD) (optional)
    pulled_before = 'pulled_before_example' # str | MMR pulled before date in YYYY-MM-DD format. (optional)
    pulled_before_after = '2013-10-20' # date | Date pulled is less than or equal to this date (YYYY-MM-DD) (optional)
    pulled_before_before = '2013-10-20' # date | Date pulled is less than or equal to this date (YYYY-MM-DD) (optional)
    rscid = 'rscid_example' # str | Specific Member RSC ID (E.g: RSC002918) (optional)
    rscid_begin = 'rscid_begin_example' # str | Starting RSC ID for a range of RSC IDs (optional)
    rscid_end = 'rscid_end_example' # str | Ending RSC ID for a range of RSC IDs (optional)

    try:
        api_response = await api_instance.numbers_mmr_list(discord_id=discord_id, format=format, limit=limit, offset=offset, psyonix_season=psyonix_season, pulled=pulled, pulled_after=pulled_after, pulled_after_after=pulled_after_after, pulled_after_before=pulled_after_before, pulled_before=pulled_before, pulled_before_after=pulled_before_after, pulled_before_before=pulled_before_before, rscid=rscid, rscid_begin=rscid_begin, rscid_end=rscid_end)
        print("The response of NumbersApi->numbers_mmr_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NumbersApi->numbers_mmr_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discord_id** | **int**| Member discord ID | [optional] 
 **format** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **psyonix_season** | **int**| Psyonix Season Number | [optional] 
 **pulled** | **datetime**| Specific date pulled (YYYY-MM-DD) | [optional] 
 **pulled_after** | **str**| MMR pulled after date in YYYY-MM-DD format. | [optional] 
 **pulled_after_after** | **date**| Date pulled is greater than or equal to this date (YYYY-MM-DD) | [optional] 
 **pulled_after_before** | **date**| Date pulled is greater than or equal to this date (YYYY-MM-DD) | [optional] 
 **pulled_before** | **str**| MMR pulled before date in YYYY-MM-DD format. | [optional] 
 **pulled_before_after** | **date**| Date pulled is less than or equal to this date (YYYY-MM-DD) | [optional] 
 **pulled_before_before** | **date**| Date pulled is less than or equal to this date (YYYY-MM-DD) | [optional] 
 **rscid** | **str**| Specific Member RSC ID (E.g: RSC002918) | [optional] 
 **rscid_begin** | **str**| Starting RSC ID for a range of RSC IDs | [optional] 
 **rscid_end** | **str**| Ending RSC ID for a range of RSC IDs | [optional] 

### Return type

[**PaginatedPlayerMMRList**](PaginatedPlayerMMRList.md)

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
> PlayerMMR numbers_mmr_partial_update(id, format=format, patched_player_mmr=patched_player_mmr)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.patched_player_mmr import PatchedPlayerMMR
from rscapi.models.player_mmr import PlayerMMR
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
    api_instance = rscapi.NumbersApi(api_client)
    id = 56 # int | A unique integer value identifying this player mmr pull.
    format = 'format_example' # str |  (optional)
    patched_player_mmr = rscapi.PatchedPlayerMMR() # PatchedPlayerMMR |  (optional)

    try:
        api_response = await api_instance.numbers_mmr_partial_update(id, format=format, patched_player_mmr=patched_player_mmr)
        print("The response of NumbersApi->numbers_mmr_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NumbersApi->numbers_mmr_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this player mmr pull. | 
 **format** | **str**|  | [optional] 
 **patched_player_mmr** | [**PatchedPlayerMMR**](PatchedPlayerMMR.md)|  | [optional] 

### Return type

[**PlayerMMR**](PlayerMMR.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numbers_mmr_retrieve**
> PlayerMMR numbers_mmr_retrieve(id, format=format)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_mmr import PlayerMMR
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
    api_instance = rscapi.NumbersApi(api_client)
    id = 56 # int | A unique integer value identifying this player mmr pull.
    format = 'format_example' # str |  (optional)

    try:
        api_response = await api_instance.numbers_mmr_retrieve(id, format=format)
        print("The response of NumbersApi->numbers_mmr_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NumbersApi->numbers_mmr_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this player mmr pull. | 
 **format** | **str**|  | [optional] 

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
> PlayerMMR numbers_mmr_update(id, player_mmr, format=format)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_mmr import PlayerMMR
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
    api_instance = rscapi.NumbersApi(api_client)
    id = 56 # int | A unique integer value identifying this player mmr pull.
    player_mmr = rscapi.PlayerMMR() # PlayerMMR | 
    format = 'format_example' # str |  (optional)

    try:
        api_response = await api_instance.numbers_mmr_update(id, player_mmr, format=format)
        print("The response of NumbersApi->numbers_mmr_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NumbersApi->numbers_mmr_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this player mmr pull. | 
 **player_mmr** | [**PlayerMMR**](PlayerMMR.md)|  | 
 **format** | **str**|  | [optional] 

### Return type

[**PlayerMMR**](PlayerMMR.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


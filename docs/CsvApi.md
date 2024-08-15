# rscapi.CsvApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**csv_franchise_contracts_data_list**](CsvApi.md#csv_franchise_contracts_data_list) | **GET** /csv/franchise-contracts-data/ | 
[**csv_franchise_contracts_data_read**](CsvApi.md#csv_franchise_contracts_data_read) | **GET** /csv/franchise-contracts-data/{id}/ | 
[**csv_master_contracts_data_list**](CsvApi.md#csv_master_contracts_data_list) | **GET** /csv/master-contracts-data/ | 
[**csv_master_contracts_data_read**](CsvApi.md#csv_master_contracts_data_read) | **GET** /csv/master-contracts-data/{id}/ | 
[**csv_master_member_sheet_list**](CsvApi.md#csv_master_member_sheet_list) | **GET** /csv/master-member-sheet/ | 
[**csv_master_member_sheet_read**](CsvApi.md#csv_master_member_sheet_read) | **GET** /csv/master-member-sheet/{id}/ | 
[**csv_teams_contracts_data_list**](CsvApi.md#csv_teams_contracts_data_list) | **GET** /csv/teams-contracts-data/ | 
[**csv_teams_contracts_data_read**](CsvApi.md#csv_teams_contracts_data_read) | **GET** /csv/teams-contracts-data/{id}/ | 
[**csv_tracker_links_data_list**](CsvApi.md#csv_tracker_links_data_list) | **GET** /csv/tracker-links-data/ | 
[**csv_tracker_links_data_read**](CsvApi.md#csv_tracker_links_data_read) | **GET** /csv/tracker-links-data/{id}/ | 


# **csv_franchise_contracts_data_list**
> List[FranchiseContracts] csv_franchise_contracts_data_list(league=league)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise_contracts import FranchiseContracts
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
    api_instance = rscapi.CsvApi(api_client)
    league = 'league_example' # str | League name to search for franchises in. (optional)

    try:
        api_response = await api_instance.csv_franchise_contracts_data_list(league=league)
        print("The response of CsvApi->csv_franchise_contracts_data_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_franchise_contracts_data_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league** | **str**| League name to search for franchises in. | [optional] 

### Return type

[**List[FranchiseContracts]**](FranchiseContracts.md)

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

# **csv_franchise_contracts_data_read**
> FranchiseContracts csv_franchise_contracts_data_read(id)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise_contracts import FranchiseContracts
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
    api_instance = rscapi.CsvApi(api_client)
    id = 56 # int | A unique integer value identifying this franchise.

    try:
        api_response = await api_instance.csv_franchise_contracts_data_read(id)
        print("The response of CsvApi->csv_franchise_contracts_data_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_franchise_contracts_data_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this franchise. | 

### Return type

[**FranchiseContracts**](FranchiseContracts.md)

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

# **csv_master_contracts_data_list**
> List[MasterContracts] csv_master_contracts_data_list()



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.master_contracts import MasterContracts
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
    api_instance = rscapi.CsvApi(api_client)

    try:
        api_response = await api_instance.csv_master_contracts_data_list()
        print("The response of CsvApi->csv_master_contracts_data_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_master_contracts_data_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MasterContracts]**](MasterContracts.md)

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

# **csv_master_contracts_data_read**
> MasterContracts csv_master_contracts_data_read(id)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.master_contracts import MasterContracts
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
    api_instance = rscapi.CsvApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.csv_master_contracts_data_read(id)
        print("The response of CsvApi->csv_master_contracts_data_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_master_contracts_data_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**MasterContracts**](MasterContracts.md)

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

# **csv_master_member_sheet_list**
> List[MasterMemberSheet] csv_master_member_sheet_list()



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.master_member_sheet import MasterMemberSheet
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
    api_instance = rscapi.CsvApi(api_client)

    try:
        api_response = await api_instance.csv_master_member_sheet_list()
        print("The response of CsvApi->csv_master_member_sheet_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_master_member_sheet_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MasterMemberSheet]**](MasterMemberSheet.md)

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

# **csv_master_member_sheet_read**
> MasterMemberSheet csv_master_member_sheet_read(id)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.master_member_sheet import MasterMemberSheet
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
    api_instance = rscapi.CsvApi(api_client)
    id = 56 # int | A unique integer value identifying this user.

    try:
        api_response = await api_instance.csv_master_member_sheet_read(id)
        print("The response of CsvApi->csv_master_member_sheet_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_master_member_sheet_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 

### Return type

[**MasterMemberSheet**](MasterMemberSheet.md)

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

# **csv_teams_contracts_data_list**
> List[TeamsContracts] csv_teams_contracts_data_list(league=league)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.teams_contracts import TeamsContracts
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
    api_instance = rscapi.CsvApi(api_client)
    league = 'league_example' # str | League name to search for franchises in. (optional)

    try:
        api_response = await api_instance.csv_teams_contracts_data_list(league=league)
        print("The response of CsvApi->csv_teams_contracts_data_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_teams_contracts_data_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league** | **str**| League name to search for franchises in. | [optional] 

### Return type

[**List[TeamsContracts]**](TeamsContracts.md)

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

# **csv_teams_contracts_data_read**
> TeamsContracts csv_teams_contracts_data_read(id)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.teams_contracts import TeamsContracts
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
    api_instance = rscapi.CsvApi(api_client)
    id = 56 # int | A unique integer value identifying this teams.

    try:
        api_response = await api_instance.csv_teams_contracts_data_read(id)
        print("The response of CsvApi->csv_teams_contracts_data_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_teams_contracts_data_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this teams. | 

### Return type

[**TeamsContracts**](TeamsContracts.md)

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

# **csv_tracker_links_data_list**
> List[TrackerLinksSheet] csv_tracker_links_data_list()



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_links_sheet import TrackerLinksSheet
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
    api_instance = rscapi.CsvApi(api_client)

    try:
        api_response = await api_instance.csv_tracker_links_data_list()
        print("The response of CsvApi->csv_tracker_links_data_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_tracker_links_data_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TrackerLinksSheet]**](TrackerLinksSheet.md)

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

# **csv_tracker_links_data_read**
> TrackerLinksSheet csv_tracker_links_data_read(id)



### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_links_sheet import TrackerLinksSheet
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
    api_instance = rscapi.CsvApi(api_client)
    id = 56 # int | A unique integer value identifying this tracker links.

    try:
        api_response = await api_instance.csv_tracker_links_data_read(id)
        print("The response of CsvApi->csv_tracker_links_data_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_tracker_links_data_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker links. | 

### Return type

[**TrackerLinksSheet**](TrackerLinksSheet.md)

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


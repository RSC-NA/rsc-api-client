# rscapi.CsvApi

All URIs are relative to *https://api.rscna.com/api/v1*

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
[**csv_tracker_links_detailed_data_list**](CsvApi.md#csv_tracker_links_detailed_data_list) | **GET** /csv/tracker-links-detailed-data/ | 
[**csv_tracker_links_detailed_data_read**](CsvApi.md#csv_tracker_links_detailed_data_read) | **GET** /csv/tracker-links-detailed-data/{id}/ | 
[**csv_tracker_links_peaks_list**](CsvApi.md#csv_tracker_links_peaks_list) | **GET** /csv/tracker-links-peaks/ | 
[**csv_tracker_links_peaks_read**](CsvApi.md#csv_tracker_links_peaks_read) | **GET** /csv/tracker-links-peaks/{id}/ | 
[**csv_twos_master_member_sheet_list**](CsvApi.md#csv_twos_master_member_sheet_list) | **GET** /csv/twos-master-member-sheet/ | 
[**csv_twos_master_member_sheet_read**](CsvApi.md#csv_twos_master_member_sheet_read) | **GET** /csv/twos-master-member-sheet/{id}/ | 


# **csv_franchise_contracts_data_list**
> List[FranchiseContracts] csv_franchise_contracts_data_list(league)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.franchise_contracts import FranchiseContracts
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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
    league = 'league_example' # str | League name to search for franchises in.

    try:
        api_response = await api_instance.csv_franchise_contracts_data_list(league)
        print("The response of CsvApi->csv_franchise_contracts_data_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_franchise_contracts_data_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league** | **str**| League name to search for franchises in. | 

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

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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
> List[MasterContracts] csv_master_contracts_data_list(league, season)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.master_contracts import MasterContracts
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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
    league = 'league_example' # str | League name to search for franchises in.
    season = 56 # int | RSC season number to filter by.

    try:
        api_response = await api_instance.csv_master_contracts_data_list(league, season)
        print("The response of CsvApi->csv_master_contracts_data_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_master_contracts_data_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league** | **str**| League name to search for franchises in. | 
 **season** | **int**| RSC season number to filter by. | 

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

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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
> List[TeamsContracts] csv_teams_contracts_data_list(league)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.teams_contracts import TeamsContracts
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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
    league = 'league_example' # str | League name to search for franchises in.

    try:
        api_response = await api_instance.csv_teams_contracts_data_list(league)
        print("The response of CsvApi->csv_teams_contracts_data_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_teams_contracts_data_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league** | **str**| League name to search for franchises in. | 

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

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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

# **csv_tracker_links_detailed_data_list**
> List[TrackerLinksDetailedSheet] csv_tracker_links_detailed_data_list(status=status, member_name=member_name, is_active=is_active, discord_id=discord_id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_links_detailed_sheet import TrackerLinksDetailedSheet
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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
    status = 'status_example' # str | Filter by tracker links status. (optional)
    member_name = 'member_name_example' # str | Filter by RSC member name (case-insensitive). (optional)
    is_active = True # bool | Filter by active members only. (optional) (default to True)
    discord_id = 56 # int | Filter by Discord ID of the member. (optional)

    try:
        api_response = await api_instance.csv_tracker_links_detailed_data_list(status=status, member_name=member_name, is_active=is_active, discord_id=discord_id)
        print("The response of CsvApi->csv_tracker_links_detailed_data_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_tracker_links_detailed_data_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter by tracker links status. | [optional] 
 **member_name** | **str**| Filter by RSC member name (case-insensitive). | [optional] 
 **is_active** | **bool**| Filter by active members only. | [optional] [default to True]
 **discord_id** | **int**| Filter by Discord ID of the member. | [optional] 

### Return type

[**List[TrackerLinksDetailedSheet]**](TrackerLinksDetailedSheet.md)

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

# **csv_tracker_links_detailed_data_read**
> TrackerLinksDetailedSheet csv_tracker_links_detailed_data_read(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_links_detailed_sheet import TrackerLinksDetailedSheet
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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
        api_response = await api_instance.csv_tracker_links_detailed_data_read(id)
        print("The response of CsvApi->csv_tracker_links_detailed_data_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_tracker_links_detailed_data_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tracker links. | 

### Return type

[**TrackerLinksDetailedSheet**](TrackerLinksDetailedSheet.md)

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

# **csv_tracker_links_peaks_list**
> List[TrackerPeak] csv_tracker_links_peaks_list(pysonix_season, status=status, member_name=member_name, discord_id=discord_id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_peak import TrackerPeak
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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
    pysonix_season = 56 # int | Psysonix season number to filter by.
    status = 'status_example' # str | Filter by tracker links status. (optional)
    member_name = 'member_name_example' # str | Filter by RSC member name (case-insensitive). (optional)
    discord_id = 56 # int | Filter by Discord ID of the member. (optional)

    try:
        api_response = await api_instance.csv_tracker_links_peaks_list(pysonix_season, status=status, member_name=member_name, discord_id=discord_id)
        print("The response of CsvApi->csv_tracker_links_peaks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_tracker_links_peaks_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pysonix_season** | **int**| Psysonix season number to filter by. | 
 **status** | **str**| Filter by tracker links status. | [optional] 
 **member_name** | **str**| Filter by RSC member name (case-insensitive). | [optional] 
 **discord_id** | **int**| Filter by Discord ID of the member. | [optional] 

### Return type

[**List[TrackerPeak]**](TrackerPeak.md)

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

# **csv_tracker_links_peaks_read**
> TrackerPeak csv_tracker_links_peaks_read(id, pysonix_season)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.tracker_peak import TrackerPeak
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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
    pysonix_season = 56 # int | Psysonix season number to filter by.

    try:
        api_response = await api_instance.csv_tracker_links_peaks_read(id, pysonix_season)
        print("The response of CsvApi->csv_tracker_links_peaks_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_tracker_links_peaks_read: %s\n" % e)
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

# **csv_twos_master_member_sheet_list**
> List[TwosMasterMemberSheet] csv_twos_master_member_sheet_list()

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.twos_master_member_sheet import TwosMasterMemberSheet
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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
        api_response = await api_instance.csv_twos_master_member_sheet_list()
        print("The response of CsvApi->csv_twos_master_member_sheet_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_twos_master_member_sheet_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TwosMasterMemberSheet]**](TwosMasterMemberSheet.md)

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

# **csv_twos_master_member_sheet_read**
> TwosMasterMemberSheet csv_twos_master_member_sheet_read(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.twos_master_member_sheet import TwosMasterMemberSheet
from rscapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rscna.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rscapi.Configuration(
    host = "https://api.rscna.com/api/v1"
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
        api_response = await api_instance.csv_twos_master_member_sheet_read(id)
        print("The response of CsvApi->csv_twos_master_member_sheet_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CsvApi->csv_twos_master_member_sheet_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 

### Return type

[**TwosMasterMemberSheet**](TwosMasterMemberSheet.md)

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


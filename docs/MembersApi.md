# rscapi.MembersApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**members_accounts_retrieve**](MembersApi.md#members_accounts_retrieve) | **GET** /members/{id}/accounts/ | 
[**members_activity_check_create**](MembersApi.md#members_activity_check_create) | **POST** /members/{id}/activity_check/ | 
[**members_contract_status_retrieve**](MembersApi.md#members_contract_status_retrieve) | **GET** /members/{id}/contract_status/ | 
[**members_create**](MembersApi.md#members_create) | **POST** /members/ | 
[**members_destroy**](MembersApi.md#members_destroy) | **DELETE** /members/{id}/ | 
[**members_elevated_roles_create**](MembersApi.md#members_elevated_roles_create) | **POST** /members/{id}/elevated_roles/ | 
[**members_elevated_roles_destroy**](MembersApi.md#members_elevated_roles_destroy) | **DELETE** /members/{id}/elevated_roles/{id}/ | 
[**members_elevated_roles_list**](MembersApi.md#members_elevated_roles_list) | **GET** /members/{id}/elevated_roles/ | 
[**members_elevated_roles_partial_update**](MembersApi.md#members_elevated_roles_partial_update) | **PATCH** /members/{id}/elevated_roles/{id}/ | 
[**members_elevated_roles_retrieve**](MembersApi.md#members_elevated_roles_retrieve) | **GET** /members/{id}/elevated_roles/{id}/ | 
[**members_elevated_roles_update**](MembersApi.md#members_elevated_roles_update) | **PUT** /members/{id}/elevated_roles/{id}/ | 
[**members_intent_to_play_create**](MembersApi.md#members_intent_to_play_create) | **POST** /members/{id}/intent_to_play/ | 
[**members_list**](MembersApi.md#members_list) | **GET** /members/ | 
[**members_make_player_create**](MembersApi.md#members_make_player_create) | **POST** /members/{id}/make_player/ | 
[**members_member_league_drop_create**](MembersApi.md#members_member_league_drop_create) | **POST** /members/{id}/member_league_drop/ | 
[**members_name_change_partial_update**](MembersApi.md#members_name_change_partial_update) | **PATCH** /members/{id}/name_change/ | 
[**members_name_changes_list**](MembersApi.md#members_name_changes_list) | **GET** /members/{id}/name_changes/ | 
[**members_partial_update**](MembersApi.md#members_partial_update) | **PATCH** /members/{id}/ | 
[**members_permfa_signup_create**](MembersApi.md#members_permfa_signup_create) | **POST** /members/{id}/permfa_signup/ | 
[**members_postseason_stats_retrieve**](MembersApi.md#members_postseason_stats_retrieve) | **GET** /members/{id}/postseason_stats/ | 
[**members_retrieve**](MembersApi.md#members_retrieve) | **GET** /members/{id}/ | 
[**members_signup_create**](MembersApi.md#members_signup_create) | **POST** /members/{id}/signup/ | 
[**members_stats_retrieve**](MembersApi.md#members_stats_retrieve) | **GET** /members/{id}/stats/ | 
[**members_transfer_account_create**](MembersApi.md#members_transfer_account_create) | **POST** /members/{id}/transfer_account/ | 
[**members_update**](MembersApi.md#members_update) | **PUT** /members/{id}/ | 
[**members_update_discord_id_create**](MembersApi.md#members_update_discord_id_create) | **POST** /members/{id}/update_discord_id/ | 


# **members_accounts_retrieve**
> MemberTracker members_accounts_retrieve(id)

Get accounts for a user

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.member_tracker import MemberTracker
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.

    try:
        api_response = await api_instance.members_accounts_retrieve(id)
        print("The response of MembersApi->members_accounts_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_accounts_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 

### Return type

[**MemberTracker**](MemberTracker.md)

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

# **members_activity_check_create**
> ActivityCheck members_activity_check_create(id, activity_request)

Apply this mixin to any view or viewset to get multiple field filtering
based on a `lookup_fields` attribute, instead of the default single field filtering.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.activity_check import ActivityCheck
from rscapi.models.activity_request import ActivityRequest
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    activity_request = rscapi.ActivityRequest() # ActivityRequest | 

    try:
        api_response = await api_instance.members_activity_check_create(id, activity_request)
        print("The response of MembersApi->members_activity_check_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_activity_check_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **activity_request** | [**ActivityRequest**](ActivityRequest.md)|  | 

### Return type

[**ActivityCheck**](ActivityCheck.md)

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
**403** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_contract_status_retrieve**
> LeaguePlayer members_contract_status_retrieve(id, league)

GET /member/{id}/contract_status/

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    league = 56 # int | League ID to get player contract status of

    try:
        api_response = await api_instance.members_contract_status_retrieve(id, league)
        print("The response of MembersApi->members_contract_status_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_contract_status_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **league** | **int**| League ID to get player contract status of | 

### Return type

[**LeaguePlayer**](LeaguePlayer.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_create**
> Member members_create(create_member_input)

Create a new member.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.create_member_input import CreateMemberInput
from rscapi.models.member import Member
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
    api_instance = rscapi.MembersApi(api_client)
    create_member_input = rscapi.CreateMemberInput() # CreateMemberInput | 

    try:
        api_response = await api_instance.members_create(create_member_input)
        print("The response of MembersApi->members_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_member_input** | [**CreateMemberInput**](CreateMemberInput.md)|  | 

### Return type

[**Member**](Member.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_destroy**
> members_destroy(id)

Apply this mixin to any view or viewset to get multiple field filtering
based on a `lookup_fields` attribute, instead of the default single field filtering.

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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.

    try:
        await api_instance.members_destroy(id)
    except Exception as e:
        print("Exception when calling MembersApi->members_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 

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

# **members_elevated_roles_create**
> Member members_elevated_roles_create(id, elevated_role_input)

Create a new elevated role for member.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.elevated_role_input import ElevatedRoleInput
from rscapi.models.member import Member
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this elevated role.
    elevated_role_input = rscapi.ElevatedRoleInput() # ElevatedRoleInput | 

    try:
        api_response = await api_instance.members_elevated_roles_create(id, elevated_role_input)
        print("The response of MembersApi->members_elevated_roles_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_elevated_roles_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this elevated role. | 
 **elevated_role_input** | [**ElevatedRoleInput**](ElevatedRoleInput.md)|  | 

### Return type

[**Member**](Member.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_elevated_roles_destroy**
> members_elevated_roles_destroy(id)

Delete an elevated role by its ID

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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this elevated role.

    try:
        await api_instance.members_elevated_roles_destroy(id)
    except Exception as e:
        print("Exception when calling MembersApi->members_elevated_roles_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this elevated role. | 

### Return type

void (empty response body)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**404** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_elevated_roles_list**
> List[ElevatedRole] members_elevated_roles_list(id, agm=agm, gm=gm, league=league, position=position)

List elevated roles for a member.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.elevated_role import ElevatedRole
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this elevated role.
    agm = True # bool | Assistant GM (optional)
    gm = True # bool | General Manager (optional)
    league = 56 # int | League ID (optional)
    position = 'position_example' # str | Staff position (optional)

    try:
        api_response = await api_instance.members_elevated_roles_list(id, agm=agm, gm=gm, league=league, position=position)
        print("The response of MembersApi->members_elevated_roles_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_elevated_roles_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this elevated role. | 
 **agm** | **bool**| Assistant GM | [optional] 
 **gm** | **bool**| General Manager | [optional] 
 **league** | **int**| League ID | [optional] 
 **position** | **str**| Staff position | [optional] 

### Return type

[**List[ElevatedRole]**](ElevatedRole.md)

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

# **members_elevated_roles_partial_update**
> ElevatedRole members_elevated_roles_partial_update(id, patched_elevated_role=patched_elevated_role)

Apply this mixin to any view or viewset to get multiple field filtering
based on a `lookup_fields` attribute, instead of the default single field filtering.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.elevated_role import ElevatedRole
from rscapi.models.patched_elevated_role import PatchedElevatedRole
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this elevated role.
    patched_elevated_role = rscapi.PatchedElevatedRole() # PatchedElevatedRole |  (optional)

    try:
        api_response = await api_instance.members_elevated_roles_partial_update(id, patched_elevated_role=patched_elevated_role)
        print("The response of MembersApi->members_elevated_roles_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_elevated_roles_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this elevated role. | 
 **patched_elevated_role** | [**PatchedElevatedRole**](PatchedElevatedRole.md)|  | [optional] 

### Return type

[**ElevatedRole**](ElevatedRole.md)

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

# **members_elevated_roles_retrieve**
> ElevatedRole members_elevated_roles_retrieve(id)

Apply this mixin to any view or viewset to get multiple field filtering
based on a `lookup_fields` attribute, instead of the default single field filtering.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.elevated_role import ElevatedRole
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this elevated role.

    try:
        api_response = await api_instance.members_elevated_roles_retrieve(id)
        print("The response of MembersApi->members_elevated_roles_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_elevated_roles_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this elevated role. | 

### Return type

[**ElevatedRole**](ElevatedRole.md)

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

# **members_elevated_roles_update**
> ElevatedRole members_elevated_roles_update(id, elevated_role)

Apply this mixin to any view or viewset to get multiple field filtering
based on a `lookup_fields` attribute, instead of the default single field filtering.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.elevated_role import ElevatedRole
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this elevated role.
    elevated_role = rscapi.ElevatedRole() # ElevatedRole | 

    try:
        api_response = await api_instance.members_elevated_roles_update(id, elevated_role)
        print("The response of MembersApi->members_elevated_roles_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_elevated_roles_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this elevated role. | 
 **elevated_role** | [**ElevatedRole**](ElevatedRole.md)|  | 

### Return type

[**ElevatedRole**](ElevatedRole.md)

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

# **members_intent_to_play_create**
> Deleted members_intent_to_play_create(id, intent_to_play_request)

Intent to play endpoint for returning players.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.deleted import Deleted
from rscapi.models.intent_to_play_request import IntentToPlayRequest
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    intent_to_play_request = rscapi.IntentToPlayRequest() # IntentToPlayRequest | 

    try:
        api_response = await api_instance.members_intent_to_play_create(id, intent_to_play_request)
        print("The response of MembersApi->members_intent_to_play_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_intent_to_play_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **intent_to_play_request** | [**IntentToPlayRequest**](IntentToPlayRequest.md)|  | 

### Return type

[**Deleted**](Deleted.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**201** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_list**
> PaginatedMemberList members_list(discord_id=discord_id, discord_username=discord_username, limit=limit, offset=offset, rsc_name=rsc_name)

Apply this mixin to any view or viewset to get multiple field filtering
based on a `lookup_fields` attribute, instead of the default single field filtering.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.paginated_member_list import PaginatedMemberList
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
    api_instance = rscapi.MembersApi(api_client)
    discord_id = 56 # int | Discord ID of member to search for (optional)
    discord_username = 'discord_username_example' # str | Discord Username Contains (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    rsc_name = 'rsc_name_example' # str | RSC Username Contains (optional)

    try:
        api_response = await api_instance.members_list(discord_id=discord_id, discord_username=discord_username, limit=limit, offset=offset, rsc_name=rsc_name)
        print("The response of MembersApi->members_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discord_id** | **int**| Discord ID of member to search for | [optional] 
 **discord_username** | **str**| Discord Username Contains | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **rsc_name** | **str**| RSC Username Contains | [optional] 

### Return type

[**PaginatedMemberList**](PaginatedMemberList.md)

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

# **members_make_player_create**
> LeaguePlayerPatch members_make_player_create(id, league_player_signup)

Make a player a league player

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player_patch import LeaguePlayerPatch
from rscapi.models.league_player_signup import LeaguePlayerSignup
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    league_player_signup = rscapi.LeaguePlayerSignup() # LeaguePlayerSignup | 

    try:
        api_response = await api_instance.members_make_player_create(id, league_player_signup)
        print("The response of MembersApi->members_make_player_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_make_player_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **league_player_signup** | [**LeaguePlayerSignup**](LeaguePlayerSignup.md)|  | 

### Return type

[**LeaguePlayerPatch**](LeaguePlayerPatch.md)

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

# **members_member_league_drop_create**
> Member members_member_league_drop_create(id, league_player_signup)

Apply this mixin to any view or viewset to get multiple field filtering
based on a `lookup_fields` attribute, instead of the default single field filtering.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player_signup import LeaguePlayerSignup
from rscapi.models.member import Member
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    league_player_signup = rscapi.LeaguePlayerSignup() # LeaguePlayerSignup | 

    try:
        api_response = await api_instance.members_member_league_drop_create(id, league_player_signup)
        print("The response of MembersApi->members_member_league_drop_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_member_league_drop_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **league_player_signup** | [**LeaguePlayerSignup**](LeaguePlayerSignup.md)|  | 

### Return type

[**Member**](Member.md)

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

# **members_name_change_partial_update**
> Member members_name_change_partial_update(id, patched_member_name_change_request=patched_member_name_change_request)

Apply this mixin to any view or viewset to get multiple field filtering
based on a `lookup_fields` attribute, instead of the default single field filtering.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.member import Member
from rscapi.models.patched_member_name_change_request import PatchedMemberNameChangeRequest
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    patched_member_name_change_request = rscapi.PatchedMemberNameChangeRequest() # PatchedMemberNameChangeRequest |  (optional)

    try:
        api_response = await api_instance.members_name_change_partial_update(id, patched_member_name_change_request=patched_member_name_change_request)
        print("The response of MembersApi->members_name_change_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_name_change_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **patched_member_name_change_request** | [**PatchedMemberNameChangeRequest**](PatchedMemberNameChangeRequest.md)|  | [optional] 

### Return type

[**Member**](Member.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_name_changes_list**
> PaginatedNameChangeHistoryList members_name_changes_list(id, discord_id=discord_id, discord_username=discord_username, limit=limit, offset=offset, rsc_name=rsc_name)

Apply this mixin to any view or viewset to get multiple field filtering
based on a `lookup_fields` attribute, instead of the default single field filtering.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.paginated_name_change_history_list import PaginatedNameChangeHistoryList
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    discord_id = 56 # int | Discord ID. (optional)
    discord_username = 'discord_username_example' # str | Discord Username Contains (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    rsc_name = 'rsc_name_example' # str | RSC Username Contains (optional)

    try:
        api_response = await api_instance.members_name_changes_list(id, discord_id=discord_id, discord_username=discord_username, limit=limit, offset=offset, rsc_name=rsc_name)
        print("The response of MembersApi->members_name_changes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_name_changes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **discord_id** | **int**| Discord ID. | [optional] 
 **discord_username** | **str**| Discord Username Contains | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **rsc_name** | **str**| RSC Username Contains | [optional] 

### Return type

[**PaginatedNameChangeHistoryList**](PaginatedNameChangeHistoryList.md)

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

# **members_partial_update**
> Member members_partial_update(id, patched_member=patched_member)

Apply this mixin to any view or viewset to get multiple field filtering
based on a `lookup_fields` attribute, instead of the default single field filtering.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.member import Member
from rscapi.models.patched_member import PatchedMember
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    patched_member = rscapi.PatchedMember() # PatchedMember |  (optional)

    try:
        api_response = await api_instance.members_partial_update(id, patched_member=patched_member)
        print("The response of MembersApi->members_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **patched_member** | [**PatchedMember**](PatchedMember.md)|  | [optional] 

### Return type

[**Member**](Member.md)

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

# **members_permfa_signup_create**
> LeaguePlayer members_permfa_signup_create(id, perm_fa_signup_details)

PermFA signup endpoint

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
from rscapi.models.perm_fa_signup_details import PermFASignupDetails
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    perm_fa_signup_details = rscapi.PermFASignupDetails() # PermFASignupDetails | 

    try:
        api_response = await api_instance.members_permfa_signup_create(id, perm_fa_signup_details)
        print("The response of MembersApi->members_permfa_signup_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_permfa_signup_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **perm_fa_signup_details** | [**PermFASignupDetails**](PermFASignupDetails.md)|  | 

### Return type

[**LeaguePlayer**](LeaguePlayer.md)

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
**403** |  |  -  |
**405** |  |  -  |
**409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_postseason_stats_retrieve**
> PlayerSeasonStats members_postseason_stats_retrieve(id, league, season=season)

Get postseason stats for a player.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_season_stats import PlayerSeasonStats
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    league = 56 # int | League to get stats from season for.
    season = 56 # int | Specific season number to get stats for (optional)

    try:
        api_response = await api_instance.members_postseason_stats_retrieve(id, league, season=season)
        print("The response of MembersApi->members_postseason_stats_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_postseason_stats_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **league** | **int**| League to get stats from season for. | 
 **season** | **int**| Specific season number to get stats for | [optional] 

### Return type

[**PlayerSeasonStats**](PlayerSeasonStats.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_retrieve**
> Member members_retrieve(id)

Apply this mixin to any view or viewset to get multiple field filtering
based on a `lookup_fields` attribute, instead of the default single field filtering.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.member import Member
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.

    try:
        api_response = await api_instance.members_retrieve(id)
        print("The response of MembersApi->members_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 

### Return type

[**Member**](Member.md)

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

# **members_signup_create**
> LeaguePlayer members_signup_create(id, signup_details_request)

Member signup endpoint so a player can play.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
from rscapi.models.signup_details_request import SignupDetailsRequest
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    signup_details_request = rscapi.SignupDetailsRequest() # SignupDetailsRequest | 

    try:
        api_response = await api_instance.members_signup_create(id, signup_details_request)
        print("The response of MembersApi->members_signup_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_signup_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **signup_details_request** | [**SignupDetailsRequest**](SignupDetailsRequest.md)|  | 

### Return type

[**LeaguePlayer**](LeaguePlayer.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |
**405** |  |  -  |
**409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_stats_retrieve**
> PlayerSeasonStats members_stats_retrieve(id, league, season=season)

Get regular season stats for a player.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_season_stats import PlayerSeasonStats
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    league = 56 # int | League to get stats from season for.
    season = 56 # int | Specific season number to get stats for (optional)

    try:
        api_response = await api_instance.members_stats_retrieve(id, league, season=season)
        print("The response of MembersApi->members_stats_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_stats_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **league** | **int**| League to get stats from season for. | 
 **season** | **int**| Specific season number to get stats for | [optional] 

### Return type

[**PlayerSeasonStats**](PlayerSeasonStats.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_transfer_account_create**
> Member members_transfer_account_create(id, member_transfer_request)

Apply this mixin to any view or viewset to get multiple field filtering
based on a `lookup_fields` attribute, instead of the default single field filtering.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.member import Member
from rscapi.models.member_transfer_request import MemberTransferRequest
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    member_transfer_request = rscapi.MemberTransferRequest() # MemberTransferRequest | 

    try:
        api_response = await api_instance.members_transfer_account_create(id, member_transfer_request)
        print("The response of MembersApi->members_transfer_account_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_transfer_account_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **member_transfer_request** | [**MemberTransferRequest**](MemberTransferRequest.md)|  | 

### Return type

[**Member**](Member.md)

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

# **members_update**
> Member members_update(id, member)

Apply this mixin to any view or viewset to get multiple field filtering
based on a `lookup_fields` attribute, instead of the default single field filtering.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.member import Member
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    member = rscapi.Member() # Member | 

    try:
        api_response = await api_instance.members_update(id, member)
        print("The response of MembersApi->members_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **member** | [**Member**](Member.md)|  | 

### Return type

[**Member**](Member.md)

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

# **members_update_discord_id_create**
> Member members_update_discord_id_create(id, member_transfer_request)

Apply this mixin to any view or viewset to get multiple field filtering
based on a `lookup_fields` attribute, instead of the default single field filtering.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.member import Member
from rscapi.models.member_transfer_request import MemberTransferRequest
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    member_transfer_request = rscapi.MemberTransferRequest() # MemberTransferRequest | 

    try:
        api_response = await api_instance.members_update_discord_id_create(id, member_transfer_request)
        print("The response of MembersApi->members_update_discord_id_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_update_discord_id_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **member_transfer_request** | [**MemberTransferRequest**](MemberTransferRequest.md)|  | 

### Return type

[**Member**](Member.md)

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


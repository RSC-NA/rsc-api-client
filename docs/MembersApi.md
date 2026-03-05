# rscapi.MembersApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**members_accounts**](MembersApi.md#members_accounts) | **GET** /members/{id}/accounts/ | 
[**members_activity_check**](MembersApi.md#members_activity_check) | **POST** /members/{id}/activity_check/ | 
[**members_contract_status**](MembersApi.md#members_contract_status) | **GET** /members/{id}/contract_status/ | 
[**members_create**](MembersApi.md#members_create) | **POST** /members/ | 
[**members_delete**](MembersApi.md#members_delete) | **DELETE** /members/{id}/ | 
[**members_elevated_roles_create**](MembersApi.md#members_elevated_roles_create) | **POST** /members/{member_id}/elevated_roles/ | 
[**members_elevated_roles_delete**](MembersApi.md#members_elevated_roles_delete) | **DELETE** /members/{member_id}/elevated_roles/{id}/ | 
[**members_elevated_roles_list**](MembersApi.md#members_elevated_roles_list) | **GET** /members/{member_id}/elevated_roles/ | 
[**members_elevated_roles_partial_update**](MembersApi.md#members_elevated_roles_partial_update) | **PATCH** /members/{member_id}/elevated_roles/{id}/ | 
[**members_elevated_roles_read**](MembersApi.md#members_elevated_roles_read) | **GET** /members/{member_id}/elevated_roles/{id}/ | 
[**members_elevated_roles_update**](MembersApi.md#members_elevated_roles_update) | **PUT** /members/{member_id}/elevated_roles/{id}/ | 
[**members_intent_to_play**](MembersApi.md#members_intent_to_play) | **POST** /members/{id}/intent_to_play/ | 
[**members_list**](MembersApi.md#members_list) | **GET** /members/ | 
[**members_make_player**](MembersApi.md#members_make_player) | **POST** /members/{id}/make_player/ | 
[**members_member_league_drop**](MembersApi.md#members_member_league_drop) | **POST** /members/{id}/member_league_drop/ | 
[**members_name_change**](MembersApi.md#members_name_change) | **PATCH** /members/{id}/name_change/ | 
[**members_name_changes**](MembersApi.md#members_name_changes) | **GET** /members/{id}/name_changes/ | 
[**members_partial_update**](MembersApi.md#members_partial_update) | **PATCH** /members/{id}/ | 
[**members_permfa_signup**](MembersApi.md#members_permfa_signup) | **POST** /members/{id}/permfa_signup/ | 
[**members_postseason_stats**](MembersApi.md#members_postseason_stats) | **GET** /members/{id}/postseason_stats/ | 
[**members_read**](MembersApi.md#members_read) | **GET** /members/{id}/ | 
[**members_signup**](MembersApi.md#members_signup) | **POST** /members/{id}/signup/ | 
[**members_stats**](MembersApi.md#members_stats) | **GET** /members/{id}/stats/ | 
[**members_transfer_account**](MembersApi.md#members_transfer_account) | **POST** /members/{id}/transfer_account/ | 
[**members_update**](MembersApi.md#members_update) | **PUT** /members/{id}/ | 
[**members_update_discord_id**](MembersApi.md#members_update_discord_id) | **POST** /members/{id}/update_discord_id/ | 


# **members_accounts**
> MemberTracker members_accounts(id)

Get accounts for a user

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.member_tracker import MemberTracker
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.

    try:
        api_response = await api_instance.members_accounts(id)
        print("The response of MembersApi->members_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_accounts: %s\n" % e)
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

# **members_activity_check**
> ActivityCheck members_activity_check(id, data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.activity_check import ActivityCheck
from rscapi.models.player_activity_check_schema import PlayerActivityCheckSchema
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    data = rscapi.PlayerActivityCheckSchema() # PlayerActivityCheckSchema | 

    try:
        api_response = await api_instance.members_activity_check(id, data)
        print("The response of MembersApi->members_activity_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_activity_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **data** | [**PlayerActivityCheckSchema**](PlayerActivityCheckSchema.md)|  | 

### Return type

[**ActivityCheck**](ActivityCheck.md)

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
**403** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_contract_status**
> LeaguePlayer members_contract_status(id, league)

GET /member/{id}/contract_status/

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    league = 56 # int | League ID to get player contract status of

    try:
        api_response = await api_instance.members_contract_status(id, league)
        print("The response of MembersApi->members_contract_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_contract_status: %s\n" % e)
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
> Member members_create(data)

Create a new member.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.create_member_input import CreateMemberInput
from rscapi.models.member import Member
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
    api_instance = rscapi.MembersApi(api_client)
    data = rscapi.CreateMemberInput() # CreateMemberInput | 

    try:
        api_response = await api_instance.members_create(data)
        print("The response of MembersApi->members_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CreateMemberInput**](CreateMemberInput.md)|  | 

### Return type

[**Member**](Member.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_delete**
> members_delete(id)

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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.

    try:
        await api_instance.members_delete(id)
    except Exception as e:
        print("Exception when calling MembersApi->members_delete: %s\n" % e)
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
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_elevated_roles_create**
> Member members_elevated_roles_create(member_id, data)

Create a new elevated role for member.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.elevated_role_input import ElevatedRoleInput
from rscapi.models.member import Member
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
    api_instance = rscapi.MembersApi(api_client)
    member_id = 'member_id_example' # str | 
    data = rscapi.ElevatedRoleInput() # ElevatedRoleInput | 

    try:
        api_response = await api_instance.members_elevated_roles_create(member_id, data)
        print("The response of MembersApi->members_elevated_roles_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_elevated_roles_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | 
 **data** | [**ElevatedRoleInput**](ElevatedRoleInput.md)|  | 

### Return type

[**Member**](Member.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_elevated_roles_delete**
> members_elevated_roles_delete(member_id, id)

Delete an elevated role by its ID

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
    api_instance = rscapi.MembersApi(api_client)
    member_id = 'member_id_example' # str | 
    id = 56 # int | A unique integer value identifying this elevated role.

    try:
        await api_instance.members_elevated_roles_delete(member_id, id)
    except Exception as e:
        print("Exception when calling MembersApi->members_elevated_roles_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | 
 **id** | **int**| A unique integer value identifying this elevated role. | 

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
**204** | Role successfully deleted |  -  |
**404** | Role not found |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_elevated_roles_list**
> List[ElevatedRole] members_elevated_roles_list(member_id, discord_id=discord_id, position=position, league=league, gm=gm, agm=agm)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.elevated_role import ElevatedRole
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
    api_instance = rscapi.MembersApi(api_client)
    member_id = 'member_id_example' # str | 
    discord_id = 'discord_id_example' # str | discord_id (optional)
    position = 'position_example' # str | position (optional)
    league = 'league_example' # str | league (optional)
    gm = 'gm_example' # str | gm (optional)
    agm = 'agm_example' # str | agm (optional)

    try:
        api_response = await api_instance.members_elevated_roles_list(member_id, discord_id=discord_id, position=position, league=league, gm=gm, agm=agm)
        print("The response of MembersApi->members_elevated_roles_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_elevated_roles_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | 
 **discord_id** | **str**| discord_id | [optional] 
 **position** | **str**| position | [optional] 
 **league** | **str**| league | [optional] 
 **gm** | **str**| gm | [optional] 
 **agm** | **str**| agm | [optional] 

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
> ElevatedRole members_elevated_roles_partial_update(member_id, id, data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.elevated_role import ElevatedRole
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
    api_instance = rscapi.MembersApi(api_client)
    member_id = 'member_id_example' # str | 
    id = 56 # int | A unique integer value identifying this elevated role.
    data = rscapi.ElevatedRole() # ElevatedRole | 

    try:
        api_response = await api_instance.members_elevated_roles_partial_update(member_id, id, data)
        print("The response of MembersApi->members_elevated_roles_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_elevated_roles_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | 
 **id** | **int**| A unique integer value identifying this elevated role. | 
 **data** | [**ElevatedRole**](ElevatedRole.md)|  | 

### Return type

[**ElevatedRole**](ElevatedRole.md)

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

# **members_elevated_roles_read**
> ElevatedRole members_elevated_roles_read(member_id, id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.elevated_role import ElevatedRole
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
    api_instance = rscapi.MembersApi(api_client)
    member_id = 'member_id_example' # str | 
    id = 56 # int | A unique integer value identifying this elevated role.

    try:
        api_response = await api_instance.members_elevated_roles_read(member_id, id)
        print("The response of MembersApi->members_elevated_roles_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_elevated_roles_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | 
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
> ElevatedRole members_elevated_roles_update(member_id, id, data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.elevated_role import ElevatedRole
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
    api_instance = rscapi.MembersApi(api_client)
    member_id = 'member_id_example' # str | 
    id = 56 # int | A unique integer value identifying this elevated role.
    data = rscapi.ElevatedRole() # ElevatedRole | 

    try:
        api_response = await api_instance.members_elevated_roles_update(member_id, id, data)
        print("The response of MembersApi->members_elevated_roles_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_elevated_roles_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | 
 **id** | **int**| A unique integer value identifying this elevated role. | 
 **data** | [**ElevatedRole**](ElevatedRole.md)|  | 

### Return type

[**ElevatedRole**](ElevatedRole.md)

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

# **members_intent_to_play**
> Deleted members_intent_to_play(id, data)

Intent to play endpoint for returning players.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.deleted import Deleted
from rscapi.models.intent_to_play_schema import IntentToPlaySchema
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    data = rscapi.IntentToPlaySchema() # IntentToPlaySchema | 

    try:
        api_response = await api_instance.members_intent_to_play(id, data)
        print("The response of MembersApi->members_intent_to_play:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_intent_to_play: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **data** | [**IntentToPlaySchema**](IntentToPlaySchema.md)|  | 

### Return type

[**Deleted**](Deleted.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
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
> MembersList200Response members_list(rsc_name=rsc_name, discord_username=discord_username, discord_id=discord_id, limit=limit, offset=offset)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.members_list200_response import MembersList200Response
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
    api_instance = rscapi.MembersApi(api_client)
    rsc_name = 'rsc_name_example' # str | rsc_name (optional)
    discord_username = 'discord_username_example' # str | discord_username (optional)
    discord_id = 56 # int | Discord ID of member to search for (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.members_list(rsc_name=rsc_name, discord_username=discord_username, discord_id=discord_id, limit=limit, offset=offset)
        print("The response of MembersApi->members_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rsc_name** | **str**| rsc_name | [optional] 
 **discord_username** | **str**| discord_username | [optional] 
 **discord_id** | **int**| Discord ID of member to search for | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**MembersList200Response**](MembersList200Response.md)

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

# **members_make_player**
> LeaguePlayerPatch members_make_player(id, data)

Make a player a league player

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player_patch import LeaguePlayerPatch
from rscapi.models.league_player_signup import LeaguePlayerSignup
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    data = rscapi.LeaguePlayerSignup() # LeaguePlayerSignup | 

    try:
        api_response = await api_instance.members_make_player(id, data)
        print("The response of MembersApi->members_make_player:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_make_player: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **data** | [**LeaguePlayerSignup**](LeaguePlayerSignup.md)|  | 

### Return type

[**LeaguePlayerPatch**](LeaguePlayerPatch.md)

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

# **members_member_league_drop**
> Member members_member_league_drop(id, data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.drop_a_player_from_a_league import DropAPlayerFromALeague
from rscapi.models.member import Member
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    data = rscapi.DropAPlayerFromALeague() # DropAPlayerFromALeague | 

    try:
        api_response = await api_instance.members_member_league_drop(id, data)
        print("The response of MembersApi->members_member_league_drop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_member_league_drop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **data** | [**DropAPlayerFromALeague**](DropAPlayerFromALeague.md)|  | 

### Return type

[**Member**](Member.md)

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

# **members_name_change**
> Member members_name_change(id, data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.member import Member
from rscapi.models.update_member_rsc_name import UpdateMemberRSCName
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    data = rscapi.UpdateMemberRSCName() # UpdateMemberRSCName | 

    try:
        api_response = await api_instance.members_name_change(id, data)
        print("The response of MembersApi->members_name_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_name_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **data** | [**UpdateMemberRSCName**](UpdateMemberRSCName.md)|  | 

### Return type

[**Member**](Member.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_name_changes**
> List[NameChangeHistory] members_name_changes(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.name_change_history import NameChangeHistory
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.

    try:
        api_response = await api_instance.members_name_changes(id)
        print("The response of MembersApi->members_name_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_name_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 

### Return type

[**List[NameChangeHistory]**](NameChangeHistory.md)

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
> Member members_partial_update(id, data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.member import Member
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    data = rscapi.Member() # Member | 

    try:
        api_response = await api_instance.members_partial_update(id, data)
        print("The response of MembersApi->members_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **data** | [**Member**](Member.md)|  | 

### Return type

[**Member**](Member.md)

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

# **members_permfa_signup**
> LeaguePlayer members_permfa_signup(id, data)

PermFA signup endpoint

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
from rscapi.models.player_signup_schema import PlayerSignupSchema
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    data = rscapi.PlayerSignupSchema() # PlayerSignupSchema | 

    try:
        api_response = await api_instance.members_permfa_signup(id, data)
        print("The response of MembersApi->members_permfa_signup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_permfa_signup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **data** | [**PlayerSignupSchema**](PlayerSignupSchema.md)|  | 

### Return type

[**LeaguePlayer**](LeaguePlayer.md)

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
**403** |  |  -  |
**405** |  |  -  |
**409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_postseason_stats**
> PlayerSeasonStats members_postseason_stats(id, league, season=season)

Get postseason stats for a player.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_season_stats import PlayerSeasonStats
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    league = 56 # int | League to get stats from season for.
    season = 56 # int | Specific season number to get stats for (optional)

    try:
        api_response = await api_instance.members_postseason_stats(id, league, season=season)
        print("The response of MembersApi->members_postseason_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_postseason_stats: %s\n" % e)
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

# **members_read**
> Member members_read(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.member import Member
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.

    try:
        api_response = await api_instance.members_read(id)
        print("The response of MembersApi->members_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_read: %s\n" % e)
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

# **members_signup**
> LeaguePlayer members_signup(id, data)

Member signup endpoint so a player can play.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
from rscapi.models.player_signup_schema import PlayerSignupSchema
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    data = rscapi.PlayerSignupSchema() # PlayerSignupSchema | 

    try:
        api_response = await api_instance.members_signup(id, data)
        print("The response of MembersApi->members_signup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_signup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **data** | [**PlayerSignupSchema**](PlayerSignupSchema.md)|  | 

### Return type

[**LeaguePlayer**](LeaguePlayer.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
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

# **members_stats**
> PlayerSeasonStats members_stats(id, league, season=season)

Get regular season stats for a player.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_season_stats import PlayerSeasonStats
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    league = 56 # int | League to get stats from season for.
    season = 56 # int | Specific season number to get stats for (optional)

    try:
        api_response = await api_instance.members_stats(id, league, season=season)
        print("The response of MembersApi->members_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_stats: %s\n" % e)
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

# **members_transfer_account**
> Member members_transfer_account(id, data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.member import Member
from rscapi.models.member_transfer_schema import MemberTransferSchema
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    data = rscapi.MemberTransferSchema() # MemberTransferSchema | 

    try:
        api_response = await api_instance.members_transfer_account(id, data)
        print("The response of MembersApi->members_transfer_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_transfer_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **data** | [**MemberTransferSchema**](MemberTransferSchema.md)|  | 

### Return type

[**Member**](Member.md)

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

# **members_update**
> Member members_update(id, data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.member import Member
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    data = rscapi.Member() # Member | 

    try:
        api_response = await api_instance.members_update(id, data)
        print("The response of MembersApi->members_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **data** | [**Member**](Member.md)|  | 

### Return type

[**Member**](Member.md)

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

# **members_update_discord_id**
> Member members_update_discord_id(id, data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.member import Member
from rscapi.models.member_transfer_schema import MemberTransferSchema
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
    api_instance = rscapi.MembersApi(api_client)
    id = 56 # int | A unique integer value identifying this user.
    data = rscapi.MemberTransferSchema() # MemberTransferSchema | 

    try:
        api_response = await api_instance.members_update_discord_id(id, data)
        print("The response of MembersApi->members_update_discord_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_update_discord_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 
 **data** | [**MemberTransferSchema**](MemberTransferSchema.md)|  | 

### Return type

[**Member**](Member.md)

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


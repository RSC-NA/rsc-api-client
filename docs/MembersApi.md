# rscapi.MembersApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**members_accounts**](MembersApi.md#members_accounts) | **GET** /members/{id}/accounts/ | 
[**members_contract_status**](MembersApi.md#members_contract_status) | **GET** /members/{id}/contract_status/ | 
[**members_create**](MembersApi.md#members_create) | **POST** /members/ | 
[**members_delete**](MembersApi.md#members_delete) | **DELETE** /members/{id}/ | 
[**members_intent_to_play**](MembersApi.md#members_intent_to_play) | **POST** /members/intent_to_play/ | 
[**members_list**](MembersApi.md#members_list) | **GET** /members/ | 
[**members_name_change**](MembersApi.md#members_name_change) | **PATCH** /members/{id}/name_change/ | 
[**members_partial_update**](MembersApi.md#members_partial_update) | **PATCH** /members/{id}/ | 
[**members_postseason_stats**](MembersApi.md#members_postseason_stats) | **GET** /members/{id}/postseason_stats/ | 
[**members_read**](MembersApi.md#members_read) | **GET** /members/{id}/ | 
[**members_signup**](MembersApi.md#members_signup) | **POST** /members/{id}/signup/ | 
[**members_stats**](MembersApi.md#members_stats) | **GET** /members/{id}/stats/ | 
[**members_update**](MembersApi.md#members_update) | **PUT** /members/{id}/ | 


# **members_accounts**
> MemberTracker members_accounts(id)



Get accounts for a user

### Example

* Api Key Authentication (Api-Key):
```python
import time
import os
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

# **members_contract_status**
> LeaguePlayer members_contract_status(id, league)



GET /member/{id}/contract_status/

### Example

* Api Key Authentication (Api-Key):
```python
import time
import os
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



### Example

* Api Key Authentication (Api-Key):
```python
import time
import os
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
    data = rscapi.Member() # Member | 

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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_delete**
> members_delete(id)



### Example

* Api Key Authentication (Api-Key):
```python
import time
import os
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

# **members_intent_to_play**
> List[LeaguePlayer] members_intent_to_play(data)



Intent to play endpoint for returning players.

### Example

* Api Key Authentication (Api-Key):
```python
import time
import os
import rscapi
from rscapi.models.intent_to_play_schema import IntentToPlaySchema
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
    data = rscapi.IntentToPlaySchema() # IntentToPlaySchema | 

    try:
        api_response = await api_instance.members_intent_to_play(data)
        print("The response of MembersApi->members_intent_to_play:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->members_intent_to_play: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**IntentToPlaySchema**](IntentToPlaySchema.md)|  | 

### Return type

[**List[LeaguePlayer]**](LeaguePlayer.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_list**
> MembersList200Response members_list(rsc_name=rsc_name, discord_username=discord_username, discord_id=discord_id, limit=limit, offset=offset)



### Example

* Api Key Authentication (Api-Key):
```python
import time
import os
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

# **members_name_change**
> Member members_name_change(id, data)



### Example

* Api Key Authentication (Api-Key):
```python
import time
import os
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

# **members_partial_update**
> Member members_partial_update(id, data)



### Example

* Api Key Authentication (Api-Key):
```python
import time
import os
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

# **members_postseason_stats**
> PlayerSeasonStats members_postseason_stats(id, league, season=season)



Get postseason stats for a player.

### Example

* Api Key Authentication (Api-Key):
```python
import time
import os
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
import time
import os
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
import time
import os
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
**200** |  |  -  |
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
import time
import os
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

# **members_update**
> Member members_update(id, data)



### Example

* Api Key Authentication (Api-Key):
```python
import time
import os
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


# rscapi.TransactionsApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactions_cut_and_sign_create**](TransactionsApi.md#transactions_cut_and_sign_create) | **POST** /transactions/cut_and_sign/ | 
[**transactions_cut_create**](TransactionsApi.md#transactions_cut_create) | **POST** /transactions/cut/ | 
[**transactions_draft_create**](TransactionsApi.md#transactions_draft_create) | **POST** /transactions/draft/ | 
[**transactions_expire_create**](TransactionsApi.md#transactions_expire_create) | **POST** /transactions/expire/ | 
[**transactions_history_list**](TransactionsApi.md#transactions_history_list) | **GET** /transactions/history/ | 
[**transactions_history_read**](TransactionsApi.md#transactions_history_read) | **GET** /transactions/history/{id}/ | 
[**transactions_inactive_reserve_create**](TransactionsApi.md#transactions_inactive_reserve_create) | **POST** /transactions/inactive-reserve/ | 
[**transactions_resign_create**](TransactionsApi.md#transactions_resign_create) | **POST** /transactions/resign/ | 
[**transactions_retire_create**](TransactionsApi.md#transactions_retire_create) | **POST** /transactions/retire/ | 
[**transactions_sign_create**](TransactionsApi.md#transactions_sign_create) | **POST** /transactions/sign/ | 
[**transactions_substitution_create**](TransactionsApi.md#transactions_substitution_create) | **POST** /transactions/substitution/ | 
[**transactions_trade_create**](TransactionsApi.md#transactions_trade_create) | **POST** /transactions/trade/ | 


# **transactions_cut_and_sign_create**
> List[TransactionResponse] transactions_cut_and_sign_create(data)

Cut a player and sign another.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.cut_a_player_and_sign_another import CutAPlayerAndSignAnother
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    data = rscapi.CutAPlayerAndSignAnother() # CutAPlayerAndSignAnother | 

    try:
        api_response = await api_instance.transactions_cut_and_sign_create(data)
        print("The response of TransactionsApi->transactions_cut_and_sign_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_cut_and_sign_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CutAPlayerAndSignAnother**](CutAPlayerAndSignAnother.md)|  | 

### Return type

[**List[TransactionResponse]**](TransactionResponse.md)

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

# **transactions_cut_create**
> TransactionResponse transactions_cut_create(data)

Cut a player

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.cut_a_player_from_a_league import CutAPlayerFromALeague
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    data = rscapi.CutAPlayerFromALeague() # CutAPlayerFromALeague | 

    try:
        api_response = await api_instance.transactions_cut_create(data)
        print("The response of TransactionsApi->transactions_cut_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_cut_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CutAPlayerFromALeague**](CutAPlayerFromALeague.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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

# **transactions_draft_create**
> TransactionResponse transactions_draft_create(data)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.draft_a_player_to_a_team import DraftAPlayerToATeam
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    data = rscapi.DraftAPlayerToATeam() # DraftAPlayerToATeam | 

    try:
        api_response = await api_instance.transactions_draft_create(data)
        print("The response of TransactionsApi->transactions_draft_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_draft_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DraftAPlayerToATeam**](DraftAPlayerToATeam.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_expire_create**
> LeaguePlayer transactions_expire_create(data)

Manually expire a sub for a team.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.expire_a_player_sub import ExpireAPlayerSub
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
    api_instance = rscapi.TransactionsApi(api_client)
    data = rscapi.ExpireAPlayerSub() # ExpireAPlayerSub | 

    try:
        api_response = await api_instance.transactions_expire_create(data)
        print("The response of TransactionsApi->transactions_expire_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_expire_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ExpireAPlayerSub**](ExpireAPlayerSub.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_history_list**
> TransactionsHistoryList200Response transactions_history_list(league, season_number=season_number, player=player, transaction_type=transaction_type, executor=executor, limit=limit, offset=offset)

List all transactions for a given league and season.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.transactions_history_list200_response import TransactionsHistoryList200Response
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
    api_instance = rscapi.TransactionsApi(api_client)
    league = 56 # int | ID of the league to get team matches for
    season_number = 56 # int | Season number to search for. (E.g: 18) (optional)
    player = 56 # int | Discord ID of player for transaction history search. (optional)
    transaction_type = 'transaction_type_example' # str | transaction_type (optional)
    executor = 56 # int | Discord ID of the member who ran the transaction. (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.transactions_history_list(league, season_number=season_number, player=player, transaction_type=transaction_type, executor=executor, limit=limit, offset=offset)
        print("The response of TransactionsApi->transactions_history_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_history_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league** | **int**| ID of the league to get team matches for | 
 **season_number** | **int**| Season number to search for. (E.g: 18) | [optional] 
 **player** | **int**| Discord ID of player for transaction history search. | [optional] 
 **transaction_type** | **str**| transaction_type | [optional] 
 **executor** | **int**| Discord ID of the member who ran the transaction. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**TransactionsHistoryList200Response**](TransactionsHistoryList200Response.md)

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

# **transactions_history_read**
> TransactionResponse transactions_history_read(id)

Retrieve a specific transaction by ID.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    id = 56 # int | A unique integer value identifying this transactions.

    try:
        api_response = await api_instance.transactions_history_read(id)
        print("The response of TransactionsApi->transactions_history_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_history_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this transactions. | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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

# **transactions_inactive_reserve_create**
> TransactionResponse transactions_inactive_reserve_create(data)

Set or remove a player to IR

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.inactive_reserve import InactiveReserve
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    data = rscapi.InactiveReserve() # InactiveReserve | 

    try:
        api_response = await api_instance.transactions_inactive_reserve_create(data)
        print("The response of TransactionsApi->transactions_inactive_reserve_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_inactive_reserve_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InactiveReserve**](InactiveReserve.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_resign_create**
> TransactionResponse transactions_resign_create(data)

Re-sign a player

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.re_sign_player import ReSignPlayer
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    data = rscapi.ReSignPlayer() # ReSignPlayer | 

    try:
        api_response = await api_instance.transactions_resign_create(data)
        print("The response of TransactionsApi->transactions_resign_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_resign_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ReSignPlayer**](ReSignPlayer.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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
**404** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_retire_create**
> TransactionResponse transactions_retire_create(data)

Retire a player from a league.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.retire_a_player import RetireAPlayer
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    data = rscapi.RetireAPlayer() # RetireAPlayer | 

    try:
        api_response = await api_instance.transactions_retire_create(data)
        print("The response of TransactionsApi->transactions_retire_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_retire_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RetireAPlayer**](RetireAPlayer.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_sign_create**
> TransactionResponse transactions_sign_create(data)

Sign a player

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.sign_a_player_to_a_team_in_a_league import SignAPlayerToATeamInALeague
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    data = rscapi.SignAPlayerToATeamInALeague() # SignAPlayerToATeamInALeague | 

    try:
        api_response = await api_instance.transactions_sign_create(data)
        print("The response of TransactionsApi->transactions_sign_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_sign_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SignAPlayerToATeamInALeague**](SignAPlayerToATeamInALeague.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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

# **transactions_substitution_create**
> TransactionResponse transactions_substitution_create(data)

Substitute a player on a team

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.temporary_fa_sub import TemporaryFASub
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    data = rscapi.TemporaryFASub() # TemporaryFASub | 

    try:
        api_response = await api_instance.transactions_substitution_create(data)
        print("The response of TransactionsApi->transactions_substitution_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_substitution_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TemporaryFASub**](TemporaryFASub.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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
**404** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_trade_create**
> TransactionResponse transactions_trade_create(data)

Trade a player to a franchise, or two players to two franchises.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.trade_schema import TradeSchema
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    data = rscapi.TradeSchema() # TradeSchema | 

    try:
        api_response = await api_instance.transactions_trade_create(data)
        print("The response of TransactionsApi->transactions_trade_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_trade_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TradeSchema**](TradeSchema.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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


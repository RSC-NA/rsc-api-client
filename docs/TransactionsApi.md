# rscapi.TransactionsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactions_cut_and_sign_create**](TransactionsApi.md#transactions_cut_and_sign_create) | **POST** /transactions/cut_and_sign/ | 
[**transactions_cut_create**](TransactionsApi.md#transactions_cut_create) | **POST** /transactions/cut/ | 
[**transactions_draft_create**](TransactionsApi.md#transactions_draft_create) | **POST** /transactions/draft/ | 
[**transactions_expire_create**](TransactionsApi.md#transactions_expire_create) | **POST** /transactions/expire/ | 
[**transactions_history_list**](TransactionsApi.md#transactions_history_list) | **GET** /transactions/history/ | 
[**transactions_history_retrieve**](TransactionsApi.md#transactions_history_retrieve) | **GET** /transactions/history/{id}/ | 
[**transactions_inactive_reserve_create**](TransactionsApi.md#transactions_inactive_reserve_create) | **POST** /transactions/inactive-reserve/ | 
[**transactions_resign_create**](TransactionsApi.md#transactions_resign_create) | **POST** /transactions/resign/ | 
[**transactions_retire_create**](TransactionsApi.md#transactions_retire_create) | **POST** /transactions/retire/ | 
[**transactions_sign_create**](TransactionsApi.md#transactions_sign_create) | **POST** /transactions/sign/ | 
[**transactions_substitution_create**](TransactionsApi.md#transactions_substitution_create) | **POST** /transactions/substitution/ | 
[**transactions_trade_create**](TransactionsApi.md#transactions_trade_create) | **POST** /transactions/trade/ | 


# **transactions_cut_and_sign_create**
> List[TransactionResponse] transactions_cut_and_sign_create(cut_sign_input)

Cut a player and sign another.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.cut_sign_input import CutSignInput
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    cut_sign_input = rscapi.CutSignInput() # CutSignInput | 

    try:
        api_response = await api_instance.transactions_cut_and_sign_create(cut_sign_input)
        print("The response of TransactionsApi->transactions_cut_and_sign_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_cut_and_sign_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cut_sign_input** | [**CutSignInput**](CutSignInput.md)|  | 

### Return type

[**List[TransactionResponse]**](TransactionResponse.md)

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

# **transactions_cut_create**
> TransactionResponse transactions_cut_create(player_input)

Cut a player

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_input import PlayerInput
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    player_input = rscapi.PlayerInput() # PlayerInput | 

    try:
        api_response = await api_instance.transactions_cut_create(player_input)
        print("The response of TransactionsApi->transactions_cut_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_cut_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_input** | [**PlayerInput**](PlayerInput.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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

# **transactions_draft_create**
> TransactionResponse transactions_draft_create(draft_input)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.draft_input import DraftInput
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    draft_input = rscapi.DraftInput() # DraftInput | 

    try:
        api_response = await api_instance.transactions_draft_create(draft_input)
        print("The response of TransactionsApi->transactions_draft_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_draft_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_input** | [**DraftInput**](DraftInput.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_expire_create**
> LeaguePlayer transactions_expire_create(player_input)

Manually expire a sub for a team.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_player import LeaguePlayer
from rscapi.models.player_input import PlayerInput
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
    api_instance = rscapi.TransactionsApi(api_client)
    player_input = rscapi.PlayerInput() # PlayerInput | 

    try:
        api_response = await api_instance.transactions_expire_create(player_input)
        print("The response of TransactionsApi->transactions_expire_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_expire_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_input** | [**PlayerInput**](PlayerInput.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_history_list**
> PaginatedTransactionResponseList transactions_history_list(league, executor=executor, limit=limit, offset=offset, player=player, season_number=season_number, transaction_type=transaction_type)

List all transactions for a given league and season.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.paginated_transaction_response_list import PaginatedTransactionResponseList
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
    api_instance = rscapi.TransactionsApi(api_client)
    league = 56 # int | ID of the league to get team matches for
    executor = 56 # int | Discord ID of the member who ran the transaction. (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    player = 56 # int | Discord ID of player for transaction history search. (optional)
    season_number = 56 # int | Season number to search for. (E.g: 18) (optional)
    transaction_type = 'transaction_type_example' # str | Filter based on a specific transaction Type.  * `AIR` - AGM Inactive Reserve * `CUT` - Cut * `DFT` - Draft Player * `IR` - Inactive Reserve * `INT` - Intent to Play * `IRT` - IR Return * `NON` - Invalid Transaction * `PCH` - Patched Player * `PKU` - Pickup * `PTD` - Player Trade * `PRO` - Promotion * `RLG` - Relegation * `RES` - Re-sign * `RET` - Retire * `SGN` - Sign Up * `PSG` - Permanent FA Sign Up * `SUB` - Substitution * `TMP` - Temporary Free Agent * `TRD` - Trade * `WVR` - Waiver Release (optional)

    try:
        api_response = await api_instance.transactions_history_list(league, executor=executor, limit=limit, offset=offset, player=player, season_number=season_number, transaction_type=transaction_type)
        print("The response of TransactionsApi->transactions_history_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_history_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league** | **int**| ID of the league to get team matches for | 
 **executor** | **int**| Discord ID of the member who ran the transaction. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **player** | **int**| Discord ID of player for transaction history search. | [optional] 
 **season_number** | **int**| Season number to search for. (E.g: 18) | [optional] 
 **transaction_type** | **str**| Filter based on a specific transaction Type.  * &#x60;AIR&#x60; - AGM Inactive Reserve * &#x60;CUT&#x60; - Cut * &#x60;DFT&#x60; - Draft Player * &#x60;IR&#x60; - Inactive Reserve * &#x60;INT&#x60; - Intent to Play * &#x60;IRT&#x60; - IR Return * &#x60;NON&#x60; - Invalid Transaction * &#x60;PCH&#x60; - Patched Player * &#x60;PKU&#x60; - Pickup * &#x60;PTD&#x60; - Player Trade * &#x60;PRO&#x60; - Promotion * &#x60;RLG&#x60; - Relegation * &#x60;RES&#x60; - Re-sign * &#x60;RET&#x60; - Retire * &#x60;SGN&#x60; - Sign Up * &#x60;PSG&#x60; - Permanent FA Sign Up * &#x60;SUB&#x60; - Substitution * &#x60;TMP&#x60; - Temporary Free Agent * &#x60;TRD&#x60; - Trade * &#x60;WVR&#x60; - Waiver Release | [optional] 

### Return type

[**PaginatedTransactionResponseList**](PaginatedTransactionResponseList.md)

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

# **transactions_history_retrieve**
> TransactionResponse transactions_history_retrieve(id)

Retrieve a specific transaction by ID.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    id = 56 # int | A unique integer value identifying this transaction.

    try:
        api_response = await api_instance.transactions_history_retrieve(id)
        print("The response of TransactionsApi->transactions_history_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_history_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this transaction. | 

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
> TransactionResponse transactions_inactive_reserve_create(ir_input)

Set or remove a player to IR

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.ir_input import IRInput
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    ir_input = rscapi.IRInput() # IRInput | 

    try:
        api_response = await api_instance.transactions_inactive_reserve_create(ir_input)
        print("The response of TransactionsApi->transactions_inactive_reserve_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_inactive_reserve_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ir_input** | [**IRInput**](IRInput.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_resign_create**
> TransactionResponse transactions_resign_create(player_team_input)

Re-sign a player

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_team_input import PlayerTeamInput
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    player_team_input = rscapi.PlayerTeamInput() # PlayerTeamInput | 

    try:
        api_response = await api_instance.transactions_resign_create(player_team_input)
        print("The response of TransactionsApi->transactions_resign_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_resign_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_team_input** | [**PlayerTeamInput**](PlayerTeamInput.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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
**404** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_retire_create**
> TransactionResponse transactions_retire_create(player_input)

Retire a player from a league.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_input import PlayerInput
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    player_input = rscapi.PlayerInput() # PlayerInput | 

    try:
        api_response = await api_instance.transactions_retire_create(player_input)
        print("The response of TransactionsApi->transactions_retire_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_retire_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_input** | [**PlayerInput**](PlayerInput.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_sign_create**
> TransactionResponse transactions_sign_create(player_team_input)

Sign a player

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.player_team_input import PlayerTeamInput
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    player_team_input = rscapi.PlayerTeamInput() # PlayerTeamInput | 

    try:
        api_response = await api_instance.transactions_sign_create(player_team_input)
        print("The response of TransactionsApi->transactions_sign_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_sign_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_team_input** | [**PlayerTeamInput**](PlayerTeamInput.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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

# **transactions_substitution_create**
> TransactionResponse transactions_substitution_create(sub_input)

Substitute a player on a team

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.sub_input import SubInput
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    sub_input = rscapi.SubInput() # SubInput | 

    try:
        api_response = await api_instance.transactions_substitution_create(sub_input)
        print("The response of TransactionsApi->transactions_substitution_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_substitution_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_input** | [**SubInput**](SubInput.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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
**404** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_trade_create**
> TransactionResponse transactions_trade_create(trade_transaction)

Trade a player to a franchise, or two players to two franchises.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.trade_transaction import TradeTransaction
from rscapi.models.transaction_response import TransactionResponse
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
    api_instance = rscapi.TransactionsApi(api_client)
    trade_transaction = rscapi.TradeTransaction() # TradeTransaction | 

    try:
        api_response = await api_instance.transactions_trade_create(trade_transaction)
        print("The response of TransactionsApi->transactions_trade_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_trade_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trade_transaction** | [**TradeTransaction**](TradeTransaction.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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


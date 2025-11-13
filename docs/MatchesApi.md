# rscapi.MatchesApi

All URIs are relative to *https://staging-api.rscna.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matches_find_match**](MatchesApi.md#matches_find_match) | **GET** /matches/find_match/ | 
[**matches_list**](MatchesApi.md#matches_list) | **GET** /matches/ | 
[**matches_process_stats**](MatchesApi.md#matches_process_stats) | **GET** /matches/{id}/process_stats/ | 
[**matches_read**](MatchesApi.md#matches_read) | **GET** /matches/{id}/ | 
[**matches_results**](MatchesApi.md#matches_results) | **GET** /matches/{id}/results/ | 


# **matches_find_match**
> List[Match] matches_find_match(league, teams, date__lt=date__lt, date__gt=date__gt, season=season, season_number=season_number, day=day, match_type=match_type, match_format=match_format, limit=limit, offset=offset, preseason=preseason)

Find a match for a team or teams.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.match import Match
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
    api_instance = rscapi.MatchesApi(api_client)
    league = 56 # int | ID of the league to get team matches for
    teams = 'teams_example' # str | Comma delimited list of teams to get names for.
    date__lt = 'date__lt_example' # str | Date less than in datetime isoformat. (optional)
    date__gt = 'date__gt_example' # str | Date greater than in datetime isoformat. (optional)
    season = 56 # int | ID of the season to search for match. (optional)
    season_number = 56 # int | Season Number (E.g: 24) (optional)
    day = 56 # int | Match day to query for. (optional)
    match_type = 'match_type_example' # str | Match Type (optional)
    match_format = 'match_format_example' # str | match_format (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    preseason = 56 # int | 1 If these matches are preseason, otherwise 0 (optional)

    try:
        api_response = await api_instance.matches_find_match(league, teams, date__lt=date__lt, date__gt=date__gt, season=season, season_number=season_number, day=day, match_type=match_type, match_format=match_format, limit=limit, offset=offset, preseason=preseason)
        print("The response of MatchesApi->matches_find_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_find_match: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league** | **int**| ID of the league to get team matches for | 
 **teams** | **str**| Comma delimited list of teams to get names for. | 
 **date__lt** | **str**| Date less than in datetime isoformat. | [optional] 
 **date__gt** | **str**| Date greater than in datetime isoformat. | [optional] 
 **season** | **int**| ID of the season to search for match. | [optional] 
 **season_number** | **int**| Season Number (E.g: 24) | [optional] 
 **day** | **int**| Match day to query for. | [optional] 
 **match_type** | **str**| Match Type | [optional] 
 **match_format** | **str**| match_format | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **preseason** | **int**| 1 If these matches are preseason, otherwise 0 | [optional] 

### Return type

[**List[Match]**](Match.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matches_list**
> MatchesList200Response matches_list(league, date__lt=date__lt, date__gt=date__gt, season=season, season_number=season_number, match_team_type=match_team_type, team_name=team_name, day=day, match_type=match_type, match_format=match_format, limit=limit, offset=offset)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.matches_list200_response import MatchesList200Response
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
    api_instance = rscapi.MatchesApi(api_client)
    league = 56 # int | ID of the league to get team matches for
    date__lt = 'date__lt_example' # str | Date less than in datetime isoformat. (optional)
    date__gt = 'date__gt_example' # str | Date greater than in datetime isoformat. (optional)
    season = 56 # int | ID of the season to search for match. (optional)
    season_number = 56 # int | Season Number (E.g: 24) (optional)
    match_team_type = 'match_team_type_example' # str | Game location. (Home, Away, or All. Default: All. Requires a team name) (optional)
    team_name = 'team_name_example' # str | team_name (optional)
    day = 56 # int | Match day to query for. (optional)
    match_type = 'match_type_example' # str | match_type (optional)
    match_format = 'match_format_example' # str | match_format (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.matches_list(league, date__lt=date__lt, date__gt=date__gt, season=season, season_number=season_number, match_team_type=match_team_type, team_name=team_name, day=day, match_type=match_type, match_format=match_format, limit=limit, offset=offset)
        print("The response of MatchesApi->matches_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league** | **int**| ID of the league to get team matches for | 
 **date__lt** | **str**| Date less than in datetime isoformat. | [optional] 
 **date__gt** | **str**| Date greater than in datetime isoformat. | [optional] 
 **season** | **int**| ID of the season to search for match. | [optional] 
 **season_number** | **int**| Season Number (E.g: 24) | [optional] 
 **match_team_type** | **str**| Game location. (Home, Away, or All. Default: All. Requires a team name) | [optional] 
 **team_name** | **str**| team_name | [optional] 
 **day** | **int**| Match day to query for. | [optional] 
 **match_type** | **str**| match_type | [optional] 
 **match_format** | **str**| match_format | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**MatchesList200Response**](MatchesList200Response.md)

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

# **matches_process_stats**
> MatchList matches_process_stats(id)

Process ballchasing stats for a given match

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.match_list import MatchList
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
    api_instance = rscapi.MatchesApi(api_client)
    id = 56 # int | A unique integer value identifying this matches.

    try:
        api_response = await api_instance.matches_process_stats(id)
        print("The response of MatchesApi->matches_process_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_process_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this matches. | 

### Return type

[**MatchList**](MatchList.md)

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

# **matches_read**
> Match matches_read(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.match import Match
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
    api_instance = rscapi.MatchesApi(api_client)
    id = 56 # int | A unique integer value identifying this matches.

    try:
        api_response = await api_instance.matches_read(id)
        print("The response of MatchesApi->matches_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this matches. | 

### Return type

[**Match**](Match.md)

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

# **matches_results**
> MatchResults matches_results(id)

Get results for a given match

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.match_results import MatchResults
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
    api_instance = rscapi.MatchesApi(api_client)
    id = 56 # int | A unique integer value identifying this matches.

    try:
        api_response = await api_instance.matches_results(id)
        print("The response of MatchesApi->matches_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this matches. | 

### Return type

[**MatchResults**](MatchResults.md)

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


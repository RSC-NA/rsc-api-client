# rscapi.MatchesApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matches_create**](MatchesApi.md#matches_create) | **POST** /matches/ | 
[**matches_destroy**](MatchesApi.md#matches_destroy) | **DELETE** /matches/{id}/ | 
[**matches_find_match_retrieve**](MatchesApi.md#matches_find_match_retrieve) | **GET** /matches/find_match/ | 
[**matches_list**](MatchesApi.md#matches_list) | **GET** /matches/ | 
[**matches_partial_update**](MatchesApi.md#matches_partial_update) | **PATCH** /matches/{id}/ | 
[**matches_process_stats_create**](MatchesApi.md#matches_process_stats_create) | **POST** /matches/{id}/process_stats/ | 
[**matches_results_list**](MatchesApi.md#matches_results_list) | **GET** /matches/results/ | 
[**matches_results_retrieve**](MatchesApi.md#matches_results_retrieve) | **GET** /matches/{id}/results/ | 
[**matches_retrieve**](MatchesApi.md#matches_retrieve) | **GET** /matches/{id}/ | 
[**matches_score_report_create**](MatchesApi.md#matches_score_report_create) | **POST** /matches/{id}/score_report/ | 
[**matches_update**](MatchesApi.md#matches_update) | **PUT** /matches/{id}/ | 


# **matches_create**
> Match matches_create(match_submission)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.match import Match
from rscapi.models.match_submission import MatchSubmission
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
    api_instance = rscapi.MatchesApi(api_client)
    match_submission = rscapi.MatchSubmission() # MatchSubmission | 

    try:
        api_response = await api_instance.matches_create(match_submission)
        print("The response of MatchesApi->matches_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_submission** | [**MatchSubmission**](MatchSubmission.md)|  | 

### Return type

[**Match**](Match.md)

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

# **matches_destroy**
> matches_destroy(id)

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
    api_instance = rscapi.MatchesApi(api_client)
    id = 56 # int | A unique integer value identifying this match.

    try:
        await api_instance.matches_destroy(id)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this match. | 

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

# **matches_find_match_retrieve**
> PaginatedMatch matches_find_match_retrieve(teams, date__gt=date__gt, date__lt=date__lt, day=day, league=league, match_format=match_format, match_type=match_type, season=season, season_number=season_number)

Find a match for a team or teams.

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.paginated_match import PaginatedMatch
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
    api_instance = rscapi.MatchesApi(api_client)
    teams = 'teams_example' # str | Team names separated by comma
    date__gt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    date__lt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    day = 56 # int |  (optional)
    league = 56 # int | League ID (Default: the default league) (optional)
    match_format = 'match_format_example' # str | * `GMS` - Game Series * `BO3` - Best of Three * `BO5` - Best of Five * `BO7` - Best of Seven (optional)
    match_type = 'REG' # str | * `REG` - Regular Season * `PRE` - Pre-season * `PST` - Post-Season * `FNL` - Finals * `ANY` - Any (optional) (default to 'REG')
    season = 56 # int | Season ID (Default: the league's current season) (optional)
    season_number = 56 # int | Season number (optional)

    try:
        api_response = await api_instance.matches_find_match_retrieve(teams, date__gt=date__gt, date__lt=date__lt, day=day, league=league, match_format=match_format, match_type=match_type, season=season, season_number=season_number)
        print("The response of MatchesApi->matches_find_match_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_find_match_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teams** | **str**| Team names separated by comma | 
 **date__gt** | **datetime**|  | [optional] 
 **date__lt** | **datetime**|  | [optional] 
 **day** | **int**|  | [optional] 
 **league** | **int**| League ID (Default: the default league) | [optional] 
 **match_format** | **str**| * &#x60;GMS&#x60; - Game Series * &#x60;BO3&#x60; - Best of Three * &#x60;BO5&#x60; - Best of Five * &#x60;BO7&#x60; - Best of Seven | [optional] 
 **match_type** | **str**| * &#x60;REG&#x60; - Regular Season * &#x60;PRE&#x60; - Pre-season * &#x60;PST&#x60; - Post-Season * &#x60;FNL&#x60; - Finals * &#x60;ANY&#x60; - Any | [optional] [default to &#39;REG&#39;]
 **season** | **int**| Season ID (Default: the league&#39;s current season) | [optional] 
 **season_number** | **int**| Season number | [optional] 

### Return type

[**PaginatedMatch**](PaginatedMatch.md)

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
> PaginatedMatchListList matches_list(date__gt=date__gt, date__lt=date__lt, day=day, league=league, limit=limit, match_format=match_format, match_team_type=match_team_type, match_type=match_type, offset=offset, season=season, season_number=season_number, team_name=team_name)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.paginated_match_list_list import PaginatedMatchListList
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
    api_instance = rscapi.MatchesApi(api_client)
    date__gt = 'date__gt_example' # str | Date greater than in datetime isoformat. (optional)
    date__lt = 'date__lt_example' # str | Date less than in datetime isoformat. (optional)
    day = 56 # int | Match day to query for. (optional)
    league = 56 # int | ID of the league to get team matches for. (Default: the default league) (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    match_format = 'match_format_example' # str | Match Format Equals  * `GMS` - Game Series * `BO3` - Best of Three * `BO5` - Best of Five * `BO7` - Best of Seven (optional)
    match_team_type = 'match_team_type_example' # str | Game location. (Home, Away, or All. Default: All. Requires a team name) (optional)
    match_type = 'match_type_example' # str | Match Type Equals (ANY: every type)  * `REG` - Regular Season * `PRE` - Pre-season * `PST` - Post-Season * `FNL` - Finals * `ANY` - Any (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    season = 56 # int | ID of the season to search for match. (Default: the league's current season) (optional)
    season_number = 56 # int | Season number to search for. (E.g: 18) (optional)
    team_name = 'team_name_example' # str | Specific team name to search for. (optional)

    try:
        api_response = await api_instance.matches_list(date__gt=date__gt, date__lt=date__lt, day=day, league=league, limit=limit, match_format=match_format, match_team_type=match_team_type, match_type=match_type, offset=offset, season=season, season_number=season_number, team_name=team_name)
        print("The response of MatchesApi->matches_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date__gt** | **str**| Date greater than in datetime isoformat. | [optional] 
 **date__lt** | **str**| Date less than in datetime isoformat. | [optional] 
 **day** | **int**| Match day to query for. | [optional] 
 **league** | **int**| ID of the league to get team matches for. (Default: the default league) | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **match_format** | **str**| Match Format Equals  * &#x60;GMS&#x60; - Game Series * &#x60;BO3&#x60; - Best of Three * &#x60;BO5&#x60; - Best of Five * &#x60;BO7&#x60; - Best of Seven | [optional] 
 **match_team_type** | **str**| Game location. (Home, Away, or All. Default: All. Requires a team name) | [optional] 
 **match_type** | **str**| Match Type Equals (ANY: every type)  * &#x60;REG&#x60; - Regular Season * &#x60;PRE&#x60; - Pre-season * &#x60;PST&#x60; - Post-Season * &#x60;FNL&#x60; - Finals * &#x60;ANY&#x60; - Any | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **season** | **int**| ID of the season to search for match. (Default: the league&#39;s current season) | [optional] 
 **season_number** | **int**| Season number to search for. (E.g: 18) | [optional] 
 **team_name** | **str**| Specific team name to search for. | [optional] 

### Return type

[**PaginatedMatchListList**](PaginatedMatchListList.md)

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

# **matches_partial_update**
> Match matches_partial_update(id, patched_match_update=patched_match_update)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.match import Match
from rscapi.models.patched_match_update import PatchedMatchUpdate
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
    api_instance = rscapi.MatchesApi(api_client)
    id = 56 # int | A unique integer value identifying this match.
    patched_match_update = rscapi.PatchedMatchUpdate() # PatchedMatchUpdate |  (optional)

    try:
        api_response = await api_instance.matches_partial_update(id, patched_match_update=patched_match_update)
        print("The response of MatchesApi->matches_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this match. | 
 **patched_match_update** | [**PatchedMatchUpdate**](PatchedMatchUpdate.md)|  | [optional] 

### Return type

[**Match**](Match.md)

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

# **matches_process_stats_create**
> matches_process_stats_create(id)

Process ballchasing stats for a given match. League admins only.

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
    api_instance = rscapi.MatchesApi(api_client)
    id = 56 # int | A unique integer value identifying this match.

    try:
        await api_instance.matches_process_stats_create(id)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_process_stats_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this match. | 

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
**400** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matches_results_list**
> PaginatedMatchResultListList matches_results_list(date__gt=date__gt, date__lt=date__lt, day=day, latest=latest, league=league, limit=limit, match_format=match_format, match_team_type=match_team_type, match_type=match_type, offset=offset, reported=reported, season=season, season_number=season_number, team_name=team_name, tier=tier, tier_name=tier_name)

List matches with their scores. Score fields are null for a match not yet reported. (Default: the default league's current season)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.paginated_match_result_list_list import PaginatedMatchResultListList
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
    api_instance = rscapi.MatchesApi(api_client)
    date__gt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    date__lt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    day = 56 # int | Match Day Equals (optional)
    latest = True # bool | Only the most recent match day already played (day and match type) with a reported score, among the matches the other filters select. (optional)
    league = 3.4 # float | Matches by League ID (Default: System Default League) (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    match_format = 'match_format_example' # str | Match Format Equals  * `GMS` - Game Series * `BO3` - Best of Three * `BO5` - Best of Five * `BO7` - Best of Seven (optional)
    match_team_type = 'match_team_type_example' # str | * `HME` - Home * `AWY` - Away * `ALL` - All Games (optional)
    match_type = 'match_type_example' # str | Match Type Equals (ANY: every type)  * `REG` - Regular Season * `PRE` - Pre-season * `PST` - Post-Season * `FNL` - Finals * `ANY` - Any (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    reported = True # bool | Only matches with (true) or without (false) a reported score. (optional)
    season = 3.4 # float | Matches by Season ID (Default: the league's current season) (optional)
    season_number = 56 # int | Matches by Season Number (optional)
    team_name = 'team_name_example' # str | Specific team name to search for. (optional)
    tier = 3.4 # float | Matches in Tier (Tier ID Equals) (optional)
    tier_name = 'tier_name_example' # str | Matches in Tier (Tier Name Equals, case-insensitive) (optional)

    try:
        api_response = await api_instance.matches_results_list(date__gt=date__gt, date__lt=date__lt, day=day, latest=latest, league=league, limit=limit, match_format=match_format, match_team_type=match_team_type, match_type=match_type, offset=offset, reported=reported, season=season, season_number=season_number, team_name=team_name, tier=tier, tier_name=tier_name)
        print("The response of MatchesApi->matches_results_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_results_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date__gt** | **datetime**|  | [optional] 
 **date__lt** | **datetime**|  | [optional] 
 **day** | **int**| Match Day Equals | [optional] 
 **latest** | **bool**| Only the most recent match day already played (day and match type) with a reported score, among the matches the other filters select. | [optional] 
 **league** | **float**| Matches by League ID (Default: System Default League) | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **match_format** | **str**| Match Format Equals  * &#x60;GMS&#x60; - Game Series * &#x60;BO3&#x60; - Best of Three * &#x60;BO5&#x60; - Best of Five * &#x60;BO7&#x60; - Best of Seven | [optional] 
 **match_team_type** | **str**| * &#x60;HME&#x60; - Home * &#x60;AWY&#x60; - Away * &#x60;ALL&#x60; - All Games | [optional] 
 **match_type** | **str**| Match Type Equals (ANY: every type)  * &#x60;REG&#x60; - Regular Season * &#x60;PRE&#x60; - Pre-season * &#x60;PST&#x60; - Post-Season * &#x60;FNL&#x60; - Finals * &#x60;ANY&#x60; - Any | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **reported** | **bool**| Only matches with (true) or without (false) a reported score. | [optional] 
 **season** | **float**| Matches by Season ID (Default: the league&#39;s current season) | [optional] 
 **season_number** | **int**| Matches by Season Number | [optional] 
 **team_name** | **str**| Specific team name to search for. | [optional] 
 **tier** | **float**| Matches in Tier (Tier ID Equals) | [optional] 
 **tier_name** | **str**| Matches in Tier (Tier Name Equals, case-insensitive) | [optional] 

### Return type

[**PaginatedMatchResultListList**](PaginatedMatchResultListList.md)

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

# **matches_results_retrieve**
> MatchResults matches_results_retrieve(id)

Get results for a given match

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.match_results import MatchResults
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
    api_instance = rscapi.MatchesApi(api_client)
    id = 56 # int | A unique integer value identifying this match.

    try:
        api_response = await api_instance.matches_results_retrieve(id)
        print("The response of MatchesApi->matches_results_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_results_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this match. | 

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
**200** | Match results retrieved successfully |  -  |
**404** | Match results not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matches_retrieve**
> Match matches_retrieve(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.match import Match
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
    api_instance = rscapi.MatchesApi(api_client)
    id = 56 # int | A unique integer value identifying this match.

    try:
        api_response = await api_instance.matches_retrieve(id)
        print("The response of MatchesApi->matches_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this match. | 

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

# **matches_score_report_create**
> MatchResults matches_score_report_create(id, match_score_report_request)

Score report for initial match

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.match_results import MatchResults
from rscapi.models.match_score_report_request import MatchScoreReportRequest
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
    api_instance = rscapi.MatchesApi(api_client)
    id = 56 # int | A unique integer value identifying this match.
    match_score_report_request = rscapi.MatchScoreReportRequest() # MatchScoreReportRequest | 

    try:
        api_response = await api_instance.matches_score_report_create(id, match_score_report_request)
        print("The response of MatchesApi->matches_score_report_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_score_report_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this match. | 
 **match_score_report_request** | [**MatchScoreReportRequest**](MatchScoreReportRequest.md)|  | 

### Return type

[**MatchResults**](MatchResults.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matches_update**
> Match matches_update(id, match_update=match_update)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.match import Match
from rscapi.models.match_update import MatchUpdate
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
    api_instance = rscapi.MatchesApi(api_client)
    id = 56 # int | A unique integer value identifying this match.
    match_update = rscapi.MatchUpdate() # MatchUpdate |  (optional)

    try:
        api_response = await api_instance.matches_update(id, match_update=match_update)
        print("The response of MatchesApi->matches_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this match. | 
 **match_update** | [**MatchUpdate**](MatchUpdate.md)|  | [optional] 

### Return type

[**Match**](Match.md)

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


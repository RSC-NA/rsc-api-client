# rscapi.IntegrationsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrations_events_list**](IntegrationsApi.md#integrations_events_list) | **GET** /integrations/events/ | 
[**integrations_events_retrieve**](IntegrationsApi.md#integrations_events_retrieve) | **GET** /integrations/events/{id}/ | 


# **integrations_events_list**
> List[LeagueEventList] integrations_events_list(action=action, category=category, created_at__gte=created_at__gte, created_at__lte=created_at__lte, guild_id=guild_id, id__gte=id__gte, is_public=is_public, league=league)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_event_list import LeagueEventList
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
    api_instance = rscapi.IntegrationsApi(api_client)
    action = 'action_example' # str | Event action code. (optional)
    category = 'category_example' # str | Event category code. (optional)
    created_at__gte = '2013-10-20T19:20:30+01:00' # datetime | Events created at or after this datetime (ISO 8601). (optional)
    created_at__lte = '2013-10-20T19:20:30+01:00' # datetime | Events created at or before this datetime (ISO 8601). (optional)
    guild_id = 56 # int | Discord guild ID for league-scoped events. (optional)
    id__gte = 56 # int | Event ID greater than or equal to this value. (optional)
    is_public = True # bool | Filter events by public visibility. (optional)
    league = 56 # int | League ID. (optional)

    try:
        api_response = await api_instance.integrations_events_list(action=action, category=category, created_at__gte=created_at__gte, created_at__lte=created_at__lte, guild_id=guild_id, id__gte=id__gte, is_public=is_public, league=league)
        print("The response of IntegrationsApi->integrations_events_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->integrations_events_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Event action code. | [optional] 
 **category** | **str**| Event category code. | [optional] 
 **created_at__gte** | **datetime**| Events created at or after this datetime (ISO 8601). | [optional] 
 **created_at__lte** | **datetime**| Events created at or before this datetime (ISO 8601). | [optional] 
 **guild_id** | **int**| Discord guild ID for league-scoped events. | [optional] 
 **id__gte** | **int**| Event ID greater than or equal to this value. | [optional] 
 **is_public** | **bool**| Filter events by public visibility. | [optional] 
 **league** | **int**| League ID. | [optional] 

### Return type

[**List[LeagueEventList]**](LeagueEventList.md)

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

# **integrations_events_retrieve**
> LeagueEventDetail integrations_events_retrieve(id)

### Example

* Api Key Authentication (Api-Key):

```python
import rscapi
from rscapi.models.league_event_detail import LeagueEventDetail
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
    api_instance = rscapi.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this league event.

    try:
        api_response = await api_instance.integrations_events_retrieve(id)
        print("The response of IntegrationsApi->integrations_events_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->integrations_events_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this league event. | 

### Return type

[**LeagueEventDetail**](LeagueEventDetail.md)

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


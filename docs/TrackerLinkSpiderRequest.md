# TrackerLinkSpiderRequest

Identify one league player, by either key. Exactly one must be supplied -- sending both, or neither, is a 400.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discord_id** | **int** | The member&#39;s Discord snowflake. | [optional] 
**league_player_id** | **int** | Primary key of a LeaguePlayer row; its member is the one spidered. | [optional] 

## Example

```python
from rscapi.models.tracker_link_spider_request import TrackerLinkSpiderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerLinkSpiderRequest from a JSON string
tracker_link_spider_request_instance = TrackerLinkSpiderRequest.from_json(json)
# print the JSON string representation of the object
print(TrackerLinkSpiderRequest.to_json())

# convert the object into a dict
tracker_link_spider_request_dict = tracker_link_spider_request_instance.to_dict()
# create an instance of TrackerLinkSpiderRequest from a dict
tracker_link_spider_request_from_dict = TrackerLinkSpiderRequest.from_dict(tracker_link_spider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



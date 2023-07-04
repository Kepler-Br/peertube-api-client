# ServerStatsVideosRedundancyInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | **str** |  | [optional] 
**total_size** | **float** |  | [optional] 
**total_used** | **float** |  | [optional] 
**total_video_files** | **float** |  | [optional] 
**total_videos** | **float** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_stats_videos_redundancy_inner import ServerStatsVideosRedundancyInner

# TODO update the JSON string below
json = "{}"
# create an instance of ServerStatsVideosRedundancyInner from a JSON string
server_stats_videos_redundancy_inner_instance = ServerStatsVideosRedundancyInner.from_json(json)
# print the JSON string representation of the object
print ServerStatsVideosRedundancyInner.to_json()

# convert the object into a dict
server_stats_videos_redundancy_inner_dict = server_stats_videos_redundancy_inner_instance.to_dict()
# create an instance of ServerStatsVideosRedundancyInner from a dict
server_stats_videos_redundancy_inner_form_dict = server_stats_videos_redundancy_inner.from_dict(server_stats_videos_redundancy_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



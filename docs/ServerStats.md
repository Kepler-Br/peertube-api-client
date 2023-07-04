# ServerStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_users** | **float** |  | [optional] 
**total_daily_active_users** | **float** |  | [optional] 
**total_weekly_active_users** | **float** |  | [optional] 
**total_monthly_active_users** | **float** |  | [optional] 
**total_local_videos** | **float** |  | [optional] 
**total_local_video_views** | **float** | Total video views made on the instance | [optional] 
**total_local_video_comments** | **float** | Total comments made by local users | [optional] 
**total_local_video_files_size** | **float** |  | [optional] 
**total_videos** | **float** |  | [optional] 
**total_video_comments** | **float** |  | [optional] 
**total_local_video_channels** | **float** |  | [optional] 
**total_local_daily_active_video_channels** | **float** |  | [optional] 
**total_local_weekly_active_video_channels** | **float** |  | [optional] 
**total_local_monthly_active_video_channels** | **float** |  | [optional] 
**total_local_playlists** | **float** |  | [optional] 
**total_instance_followers** | **float** |  | [optional] 
**total_instance_following** | **float** |  | [optional] 
**videos_redundancy** | [**List[ServerStatsVideosRedundancyInner]**](ServerStatsVideosRedundancyInner.md) |  | [optional] 
**total_activity_pub_messages_processed** | **float** |  | [optional] 
**total_activity_pub_messages_successes** | **float** |  | [optional] 
**total_activity_pub_messages_errors** | **float** |  | [optional] 
**activity_pub_messages_processed_per_second** | **float** |  | [optional] 
**total_activity_pub_messages_waiting** | **float** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_stats import ServerStats

# TODO update the JSON string below
json = "{}"
# create an instance of ServerStats from a JSON string
server_stats_instance = ServerStats.from_json(json)
# print the JSON string representation of the object
print ServerStats.to_json()

# convert the object into a dict
server_stats_dict = server_stats_instance.to_dict()
# create an instance of ServerStats from a dict
server_stats_form_dict = server_stats.from_dict(server_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# VideoChannelSyncListDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**state** | [**VideoChannelSyncState**](VideoChannelSyncState.md) |  | [optional] 
**external_channel_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**last_sync_at** | **datetime** |  | [optional] 
**channel** | [**VideoChannel**](VideoChannel.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_channel_sync_list_data_inner import VideoChannelSyncListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of VideoChannelSyncListDataInner from a JSON string
video_channel_sync_list_data_inner_instance = VideoChannelSyncListDataInner.from_json(json)
# print the JSON string representation of the object
print VideoChannelSyncListDataInner.to_json()

# convert the object into a dict
video_channel_sync_list_data_inner_dict = video_channel_sync_list_data_inner_instance.to_dict()
# create an instance of VideoChannelSyncListDataInner from a dict
video_channel_sync_list_data_inner_form_dict = video_channel_sync_list_data_inner.from_dict(video_channel_sync_list_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



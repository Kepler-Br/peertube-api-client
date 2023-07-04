# VideoChannelSyncState


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_channel_sync_state import VideoChannelSyncState

# TODO update the JSON string below
json = "{}"
# create an instance of VideoChannelSyncState from a JSON string
video_channel_sync_state_instance = VideoChannelSyncState.from_json(json)
# print the JSON string representation of the object
print VideoChannelSyncState.to_json()

# convert the object into a dict
video_channel_sync_state_dict = video_channel_sync_state_instance.to_dict()
# create an instance of VideoChannelSyncState from a dict
video_channel_sync_state_form_dict = video_channel_sync_state.from_dict(video_channel_sync_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



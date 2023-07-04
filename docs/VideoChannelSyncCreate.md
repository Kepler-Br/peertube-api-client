# VideoChannelSyncCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_channel_url** | **str** |  | [optional] 
**video_channel_id** | **int** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_channel_sync_create import VideoChannelSyncCreate

# TODO update the JSON string below
json = "{}"
# create an instance of VideoChannelSyncCreate from a JSON string
video_channel_sync_create_instance = VideoChannelSyncCreate.from_json(json)
# print the JSON string representation of the object
print VideoChannelSyncCreate.to_json()

# convert the object into a dict
video_channel_sync_create_dict = video_channel_sync_create_instance.to_dict()
# create an instance of VideoChannelSyncCreate from a dict
video_channel_sync_create_form_dict = video_channel_sync_create.from_dict(video_channel_sync_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



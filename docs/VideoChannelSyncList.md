# VideoChannelSyncList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**data** | [**List[VideoChannelSyncListDataInner]**](VideoChannelSyncListDataInner.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_channel_sync_list import VideoChannelSyncList

# TODO update the JSON string below
json = "{}"
# create an instance of VideoChannelSyncList from a JSON string
video_channel_sync_list_instance = VideoChannelSyncList.from_json(json)
# print the JSON string representation of the object
print VideoChannelSyncList.to_json()

# convert the object into a dict
video_channel_sync_list_dict = video_channel_sync_list_instance.to_dict()
# create an instance of VideoChannelSyncList from a dict
video_channel_sync_list_form_dict = video_channel_sync_list.from_dict(video_channel_sync_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



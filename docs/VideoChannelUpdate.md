# VideoChannelUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **object** | Channel display name | [optional] 
**description** | **object** | Channel description | [optional] 
**support** | **object** | How to support/fund the channel | [optional] 
**bulk_videos_support_update** | **bool** | Update the support field for all videos of this channel | [optional] 

## Example

```python
from peertube_api_client.models.video_channel_update import VideoChannelUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of VideoChannelUpdate from a JSON string
video_channel_update_instance = VideoChannelUpdate.from_json(json)
# print the JSON string representation of the object
print VideoChannelUpdate.to_json()

# convert the object into a dict
video_channel_update_dict = video_channel_update_instance.to_dict()
# create an instance of VideoChannelUpdate from a dict
video_channel_update_form_dict = video_channel_update.from_dict(video_channel_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



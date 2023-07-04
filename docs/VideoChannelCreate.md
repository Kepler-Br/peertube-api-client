# VideoChannelCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **object** | Channel display name | 
**description** | **object** | Channel description | [optional] 
**support** | **object** | How to support/fund the channel | [optional] 
**name** | **str** | immutable name of the channel, used to interact with its actor | 

## Example

```python
from peertube_api_client.models.video_channel_create import VideoChannelCreate

# TODO update the JSON string below
json = "{}"
# create an instance of VideoChannelCreate from a JSON string
video_channel_create_instance = VideoChannelCreate.from_json(json)
# print the JSON string representation of the object
print VideoChannelCreate.to_json()

# convert the object into a dict
video_channel_create_dict = video_channel_create_instance.to_dict()
# create an instance of VideoChannelCreate from a dict
video_channel_create_form_dict = video_channel_create.from_dict(video_channel_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



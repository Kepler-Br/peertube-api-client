# VideoChannelEdit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **object** | Channel display name | [optional] 
**description** | **object** | Channel description | [optional] 
**support** | **object** | How to support/fund the channel | [optional] 

## Example

```python
from peertube_api_client.models.video_channel_edit import VideoChannelEdit

# TODO update the JSON string below
json = "{}"
# create an instance of VideoChannelEdit from a JSON string
video_channel_edit_instance = VideoChannelEdit.from_json(json)
# print the JSON string representation of the object
print VideoChannelEdit.to_json()

# convert the object into a dict
video_channel_edit_dict = video_channel_edit_instance.to_dict()
# create an instance of VideoChannelEdit from a dict
video_channel_edit_form_dict = video_channel_edit.from_dict(video_channel_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# VideoChannelList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**data** | [**List[VideoChannelListDataInner]**](VideoChannelListDataInner.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_channel_list import VideoChannelList

# TODO update the JSON string below
json = "{}"
# create an instance of VideoChannelList from a JSON string
video_channel_list_instance = VideoChannelList.from_json(json)
# print the JSON string representation of the object
print VideoChannelList.to_json()

# convert the object into a dict
video_channel_list_dict = video_channel_list_instance.to_dict()
# create an instance of VideoChannelList from a dict
video_channel_list_form_dict = video_channel_list.from_dict(video_channel_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



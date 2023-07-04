# VideoChannelSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**avatars** | [**List[ActorImage]**](ActorImage.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_channel_summary import VideoChannelSummary

# TODO update the JSON string below
json = "{}"
# create an instance of VideoChannelSummary from a JSON string
video_channel_summary_instance = VideoChannelSummary.from_json(json)
# print the JSON string representation of the object
print VideoChannelSummary.to_json()

# convert the object into a dict
video_channel_summary_dict = video_channel_summary_instance.to_dict()
# create an instance of VideoChannelSummary from a dict
video_channel_summary_form_dict = video_channel_summary.from_dict(video_channel_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



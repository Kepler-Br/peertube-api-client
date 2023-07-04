# LiveVideoSessionResponseReplayVideo

Video replay information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**uuid** | **str** |  | [optional] 
**short_uuid** | **str** | translation of a uuid v4 with a bigger alphabet to have a shorter uuid | [optional] 

## Example

```python
from peertube_api_client.models.live_video_session_response_replay_video import LiveVideoSessionResponseReplayVideo

# TODO update the JSON string below
json = "{}"
# create an instance of LiveVideoSessionResponseReplayVideo from a JSON string
live_video_session_response_replay_video_instance = LiveVideoSessionResponseReplayVideo.from_json(json)
# print the JSON string representation of the object
print LiveVideoSessionResponseReplayVideo.to_json()

# convert the object into a dict
live_video_session_response_replay_video_dict = live_video_session_response_replay_video_instance.to_dict()
# create an instance of LiveVideoSessionResponseReplayVideo from a dict
live_video_session_response_replay_video_form_dict = live_video_session_response_replay_video.from_dict(live_video_session_response_replay_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



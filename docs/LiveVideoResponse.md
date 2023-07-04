# LiveVideoResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rtmp_url** | **str** | Included in the response if an appropriate token is provided | [optional] 
**rtmps_url** | **str** | Included in the response if an appropriate token is provided | [optional] 
**stream_key** | **str** | RTMP stream key to use to stream into this live video. Included in the response if an appropriate token is provided | [optional] 
**save_replay** | **bool** |  | [optional] 
**replay_settings** | [**LiveVideoReplaySettings**](LiveVideoReplaySettings.md) |  | [optional] 
**permanent_live** | **bool** | User can stream multiple times in a permanent live | [optional] 
**latency_mode** | [**LiveVideoLatencyMode**](LiveVideoLatencyMode.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.live_video_response import LiveVideoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LiveVideoResponse from a JSON string
live_video_response_instance = LiveVideoResponse.from_json(json)
# print the JSON string representation of the object
print LiveVideoResponse.to_json()

# convert the object into a dict
live_video_response_dict = live_video_response_instance.to_dict()
# create an instance of LiveVideoResponse from a dict
live_video_response_form_dict = live_video_response.from_dict(live_video_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



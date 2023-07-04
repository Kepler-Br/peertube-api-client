# LiveVideoSessionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**start_date** | **datetime** | Start date of the live session | [optional] 
**end_date** | **datetime** | End date of the live session | [optional] 
**error** | **int** | Error type if an error occurred during the live session:   - &#x60;1&#x60;: Bad socket health (transcoding is too slow)   - &#x60;2&#x60;: Max duration exceeded   - &#x60;3&#x60;: Quota exceeded   - &#x60;4&#x60;: Quota FFmpeg error   - &#x60;5&#x60;: Video has been blacklisted during the live  | [optional] 
**replay_video** | [**LiveVideoSessionResponseReplayVideo**](LiveVideoSessionResponseReplayVideo.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.live_video_session_response import LiveVideoSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LiveVideoSessionResponse from a JSON string
live_video_session_response_instance = LiveVideoSessionResponse.from_json(json)
# print the JSON string representation of the object
print LiveVideoSessionResponse.to_json()

# convert the object into a dict
live_video_session_response_dict = live_video_session_response_instance.to_dict()
# create an instance of LiveVideoSessionResponse from a dict
live_video_session_response_form_dict = live_video_session_response.from_dict(live_video_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# LiveVideoUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**save_replay** | **bool** |  | [optional] 
**replay_settings** | [**LiveVideoReplaySettings**](LiveVideoReplaySettings.md) |  | [optional] 
**permanent_live** | **bool** | User can stream multiple times in a permanent live | [optional] 
**latency_mode** | [**LiveVideoLatencyMode**](LiveVideoLatencyMode.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.live_video_update import LiveVideoUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of LiveVideoUpdate from a JSON string
live_video_update_instance = LiveVideoUpdate.from_json(json)
# print the JSON string representation of the object
print LiveVideoUpdate.to_json()

# convert the object into a dict
live_video_update_dict = live_video_update_instance.to_dict()
# create an instance of LiveVideoUpdate from a dict
live_video_update_form_dict = live_video_update.from_dict(live_video_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



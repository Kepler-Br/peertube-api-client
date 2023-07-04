# LiveVideoReplaySettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privacy** | [**VideoPrivacySet**](VideoPrivacySet.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.live_video_replay_settings import LiveVideoReplaySettings

# TODO update the JSON string below
json = "{}"
# create an instance of LiveVideoReplaySettings from a JSON string
live_video_replay_settings_instance = LiveVideoReplaySettings.from_json(json)
# print the JSON string representation of the object
print LiveVideoReplaySettings.to_json()

# convert the object into a dict
live_video_replay_settings_dict = live_video_replay_settings_instance.to_dict()
# create an instance of LiveVideoReplaySettings from a dict
live_video_replay_settings_form_dict = live_video_replay_settings.from_dict(live_video_replay_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



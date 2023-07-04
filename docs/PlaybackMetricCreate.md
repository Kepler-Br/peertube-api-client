# PlaybackMetricCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player_mode** | **str** |  | 
**resolution** | **float** | Current player video resolution | [optional] 
**fps** | **float** | Current player video fps | [optional] 
**resolution_changes** | **float** | How many resolution changes occured since the last metric creation | 
**errors** | **float** | How many errors occured since the last metric creation | 
**downloaded_bytes_p2_p** | **float** | How many bytes were downloaded with P2P since the last metric creation | 
**downloaded_bytes_http** | **float** | How many bytes were downloaded with HTTP since the last metric creation | 
**uploaded_bytes_p2_p** | **float** | How many bytes were uploaded with P2P since the last metric creation | 
**video_id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](ApiV1VideosOwnershipIdAcceptPostIdParameter.md) |  | 

## Example

```python
from peertube_api_client.models.playback_metric_create import PlaybackMetricCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PlaybackMetricCreate from a JSON string
playback_metric_create_instance = PlaybackMetricCreate.from_json(json)
# print the JSON string representation of the object
print PlaybackMetricCreate.to_json()

# convert the object into a dict
playback_metric_create_dict = playback_metric_create_instance.to_dict()
# create an instance of PlaybackMetricCreate from a dict
playback_metric_create_form_dict = playback_metric_create.from_dict(playback_metric_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



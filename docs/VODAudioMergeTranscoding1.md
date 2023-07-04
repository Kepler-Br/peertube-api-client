# VODAudioMergeTranscoding1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**VODAudioMergeTranscoding1Input**](VODAudioMergeTranscoding1Input.md) |  | [optional] 
**output** | [**VODWebVideoTranscoding1Output**](VODWebVideoTranscoding1Output.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.vod_audio_merge_transcoding1 import VODAudioMergeTranscoding1

# TODO update the JSON string below
json = "{}"
# create an instance of VODAudioMergeTranscoding1 from a JSON string
vod_audio_merge_transcoding1_instance = VODAudioMergeTranscoding1.from_json(json)
# print the JSON string representation of the object
print VODAudioMergeTranscoding1.to_json()

# convert the object into a dict
vod_audio_merge_transcoding1_dict = vod_audio_merge_transcoding1_instance.to_dict()
# create an instance of VODAudioMergeTranscoding1 from a dict
vod_audio_merge_transcoding1_form_dict = vod_audio_merge_transcoding1.from_dict(vod_audio_merge_transcoding1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



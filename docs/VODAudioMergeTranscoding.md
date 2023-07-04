# VODAudioMergeTranscoding


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_file** | **bytearray** |  | [optional] 

## Example

```python
from peertube_api_client.models.vod_audio_merge_transcoding import VODAudioMergeTranscoding

# TODO update the JSON string below
json = "{}"
# create an instance of VODAudioMergeTranscoding from a JSON string
vod_audio_merge_transcoding_instance = VODAudioMergeTranscoding.from_json(json)
# print the JSON string representation of the object
print VODAudioMergeTranscoding.to_json()

# convert the object into a dict
vod_audio_merge_transcoding_dict = vod_audio_merge_transcoding_instance.to_dict()
# create an instance of VODAudioMergeTranscoding from a dict
vod_audio_merge_transcoding_form_dict = vod_audio_merge_transcoding.from_dict(vod_audio_merge_transcoding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



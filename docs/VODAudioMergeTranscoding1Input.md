# VODAudioMergeTranscoding1Input


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_file_url** | **str** |  | [optional] 
**preview_file_url** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.vod_audio_merge_transcoding1_input import VODAudioMergeTranscoding1Input

# TODO update the JSON string below
json = "{}"
# create an instance of VODAudioMergeTranscoding1Input from a JSON string
vod_audio_merge_transcoding1_input_instance = VODAudioMergeTranscoding1Input.from_json(json)
# print the JSON string representation of the object
print VODAudioMergeTranscoding1Input.to_json()

# convert the object into a dict
vod_audio_merge_transcoding1_input_dict = vod_audio_merge_transcoding1_input_instance.to_dict()
# create an instance of VODAudioMergeTranscoding1Input from a dict
vod_audio_merge_transcoding1_input_form_dict = vod_audio_merge_transcoding1_input.from_dict(vod_audio_merge_transcoding1_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



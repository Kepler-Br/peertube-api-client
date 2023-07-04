# VODWebVideoTranscoding


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_file** | **bytearray** |  | [optional] 

## Example

```python
from peertube_api_client.models.vod_web_video_transcoding import VODWebVideoTranscoding

# TODO update the JSON string below
json = "{}"
# create an instance of VODWebVideoTranscoding from a JSON string
vod_web_video_transcoding_instance = VODWebVideoTranscoding.from_json(json)
# print the JSON string representation of the object
print VODWebVideoTranscoding.to_json()

# convert the object into a dict
vod_web_video_transcoding_dict = vod_web_video_transcoding_instance.to_dict()
# create an instance of VODWebVideoTranscoding from a dict
vod_web_video_transcoding_form_dict = vod_web_video_transcoding.from_dict(vod_web_video_transcoding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



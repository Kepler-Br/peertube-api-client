# VODWebVideoTranscoding1Output


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution** | **float** |  | [optional] 
**fps** | **float** |  | [optional] 

## Example

```python
from peertube_api_client.models.vod_web_video_transcoding1_output import VODWebVideoTranscoding1Output

# TODO update the JSON string below
json = "{}"
# create an instance of VODWebVideoTranscoding1Output from a JSON string
vod_web_video_transcoding1_output_instance = VODWebVideoTranscoding1Output.from_json(json)
# print the JSON string representation of the object
print VODWebVideoTranscoding1Output.to_json()

# convert the object into a dict
vod_web_video_transcoding1_output_dict = vod_web_video_transcoding1_output_instance.to_dict()
# create an instance of VODWebVideoTranscoding1Output from a dict
vod_web_video_transcoding1_output_form_dict = vod_web_video_transcoding1_output.from_dict(vod_web_video_transcoding1_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



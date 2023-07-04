# ServerConfigCustomTranscoding

Settings pertaining to transcoding jobs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**allow_additional_extensions** | **bool** | Allow your users to upload .mkv, .mov, .avi, .wmv, .flv, .f4v, .3g2, .3gp, .mts, m2ts, .mxf, .nut videos | [optional] 
**allow_audio_files** | **bool** | If a user uploads an audio file, PeerTube will create a video by merging the preview file and the audio file | [optional] 
**threads** | **int** | Amount of threads used by ffmpeg for 1 transcoding job | [optional] 
**concurrency** | **float** | Amount of transcoding jobs to execute in parallel | [optional] 
**profile** | **str** | New profiles can be added by plugins ; available in core PeerTube: &#39;default&#39;.  | [optional] 
**resolutions** | [**ServerConfigCustomTranscodingResolutions**](ServerConfigCustomTranscodingResolutions.md) |  | [optional] 
**webtorrent** | [**ServerConfigCustomTranscodingWebtorrent**](ServerConfigCustomTranscodingWebtorrent.md) |  | [optional] 
**hls** | [**ServerConfigCustomTranscodingHls**](ServerConfigCustomTranscodingHls.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_custom_transcoding import ServerConfigCustomTranscoding

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigCustomTranscoding from a JSON string
server_config_custom_transcoding_instance = ServerConfigCustomTranscoding.from_json(json)
# print the JSON string representation of the object
print ServerConfigCustomTranscoding.to_json()

# convert the object into a dict
server_config_custom_transcoding_dict = server_config_custom_transcoding_instance.to_dict()
# create an instance of ServerConfigCustomTranscoding from a dict
server_config_custom_transcoding_form_dict = server_config_custom_transcoding.from_dict(server_config_custom_transcoding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



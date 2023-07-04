# VideoFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**magnet_uri** | **str** | magnet URI allowing to resolve the video via BitTorrent without a metainfo file | [optional] 
**resolution** | [**VideoResolutionConstant**](VideoResolutionConstant.md) |  | [optional] 
**size** | **int** | Video file size in bytes | [optional] 
**torrent_url** | **str** | Direct URL of the torrent file | [optional] 
**torrent_download_url** | **str** | URL endpoint that transfers the torrent file as an attachment (so that the browser opens a download dialog) | [optional] 
**file_url** | **str** | Direct URL of the video | [optional] 
**file_download_url** | **str** | URL endpoint that transfers the video file as an attachment (so that the browser opens a download dialog) | [optional] 
**fps** | **float** | Frames per second of the video file | [optional] 
**metadata_url** | **str** | URL dereferencing the output of ffprobe on the file | [optional] 

## Example

```python
from peertube_api_client.models.video_file import VideoFile

# TODO update the JSON string below
json = "{}"
# create an instance of VideoFile from a JSON string
video_file_instance = VideoFile.from_json(json)
# print the JSON string representation of the object
print VideoFile.to_json()

# convert the object into a dict
video_file_dict = video_file_instance.to_dict()
# create an instance of VideoFile from a dict
video_file_form_dict = video_file.from_dict(video_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



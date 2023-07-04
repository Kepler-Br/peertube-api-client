# PutVideoPlaylistVideoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_timestamp** | **int** | Start the video at this specific timestamp | [optional] 
**stop_timestamp** | **int** | Stop the video at this specific timestamp | [optional] 

## Example

```python
from peertube_api_client.models.put_video_playlist_video_request import PutVideoPlaylistVideoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutVideoPlaylistVideoRequest from a JSON string
put_video_playlist_video_request_instance = PutVideoPlaylistVideoRequest.from_json(json)
# print the JSON string representation of the object
print PutVideoPlaylistVideoRequest.to_json()

# convert the object into a dict
put_video_playlist_video_request_dict = put_video_playlist_video_request_instance.to_dict()
# create an instance of PutVideoPlaylistVideoRequest from a dict
put_video_playlist_video_request_form_dict = put_video_playlist_video_request.from_dict(put_video_playlist_video_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



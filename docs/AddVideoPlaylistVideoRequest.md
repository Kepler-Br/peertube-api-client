# AddVideoPlaylistVideoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_id** | [**AddVideoPlaylistVideoRequestVideoId**](AddVideoPlaylistVideoRequestVideoId.md) |  | 
**start_timestamp** | **int** | Start the video at this specific timestamp | [optional] 
**stop_timestamp** | **int** | Stop the video at this specific timestamp | [optional] 

## Example

```python
from peertube_api_client.models.add_video_playlist_video_request import AddVideoPlaylistVideoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddVideoPlaylistVideoRequest from a JSON string
add_video_playlist_video_request_instance = AddVideoPlaylistVideoRequest.from_json(json)
# print the JSON string representation of the object
print AddVideoPlaylistVideoRequest.to_json()

# convert the object into a dict
add_video_playlist_video_request_dict = add_video_playlist_video_request_instance.to_dict()
# create an instance of AddVideoPlaylistVideoRequest from a dict
add_video_playlist_video_request_form_dict = add_video_playlist_video_request.from_dict(add_video_playlist_video_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



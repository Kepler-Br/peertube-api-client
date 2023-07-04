# VideoStreamingPlaylists


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playlist_url** | **str** |  | [optional] 
**segments_sha256_url** | **str** |  | [optional] 
**files** | [**List[VideoFile]**](VideoFile.md) | Video files associated to this playlist.  The difference with the root &#x60;files&#x60; property is that these files are fragmented, so they can be used in this streaming playlist (HLS, etc.)  | [optional] 
**redundancies** | [**List[VideoStreamingPlaylistsHLSRedundanciesInner]**](VideoStreamingPlaylistsHLSRedundanciesInner.md) |  | [optional] 
**id** | **int** |  | [optional] 
**type** | **int** | Playlist type: - &#x60;1&#x60;: HLS  | [optional] 

## Example

```python
from peertube_api_client.models.video_streaming_playlists import VideoStreamingPlaylists

# TODO update the JSON string below
json = "{}"
# create an instance of VideoStreamingPlaylists from a JSON string
video_streaming_playlists_instance = VideoStreamingPlaylists.from_json(json)
# print the JSON string representation of the object
print VideoStreamingPlaylists.to_json()

# convert the object into a dict
video_streaming_playlists_dict = video_streaming_playlists_instance.to_dict()
# create an instance of VideoStreamingPlaylists from a dict
video_streaming_playlists_form_dict = video_streaming_playlists.from_dict(video_streaming_playlists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



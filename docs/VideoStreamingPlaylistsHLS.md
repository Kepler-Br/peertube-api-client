# VideoStreamingPlaylistsHLS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playlist_url** | **str** |  | [optional] 
**segments_sha256_url** | **str** |  | [optional] 
**files** | [**List[VideoFile]**](VideoFile.md) | Video files associated to this playlist.  The difference with the root &#x60;files&#x60; property is that these files are fragmented, so they can be used in this streaming playlist (HLS, etc.)  | [optional] 
**redundancies** | [**List[VideoStreamingPlaylistsHLSRedundanciesInner]**](VideoStreamingPlaylistsHLSRedundanciesInner.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_streaming_playlists_hls import VideoStreamingPlaylistsHLS

# TODO update the JSON string below
json = "{}"
# create an instance of VideoStreamingPlaylistsHLS from a JSON string
video_streaming_playlists_hls_instance = VideoStreamingPlaylistsHLS.from_json(json)
# print the JSON string representation of the object
print VideoStreamingPlaylistsHLS.to_json()

# convert the object into a dict
video_streaming_playlists_hls_dict = video_streaming_playlists_hls_instance.to_dict()
# create an instance of VideoStreamingPlaylistsHLS from a dict
video_streaming_playlists_hls_form_dict = video_streaming_playlists_hls.from_dict(video_streaming_playlists_hls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



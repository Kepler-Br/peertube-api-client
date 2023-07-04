# VideoPlaylist


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**uuid** | **str** |  | [optional] 
**short_uuid** | **str** | translation of a uuid v4 with a bigger alphabet to have a shorter uuid | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**is_local** | **bool** |  | [optional] 
**video_length** | **int** |  | [optional] 
**thumbnail_path** | **str** |  | [optional] 
**privacy** | [**VideoPlaylistPrivacyConstant**](VideoPlaylistPrivacyConstant.md) |  | [optional] 
**type** | [**VideoPlaylistTypeConstant**](VideoPlaylistTypeConstant.md) |  | [optional] 
**owner_account** | [**AccountSummary**](AccountSummary.md) |  | [optional] 
**video_channel** | [**VideoChannelSummary**](VideoChannelSummary.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_playlist import VideoPlaylist

# TODO update the JSON string below
json = "{}"
# create an instance of VideoPlaylist from a JSON string
video_playlist_instance = VideoPlaylist.from_json(json)
# print the JSON string representation of the object
print VideoPlaylist.to_json()

# convert the object into a dict
video_playlist_dict = video_playlist_instance.to_dict()
# create an instance of VideoPlaylist from a dict
video_playlist_form_dict = video_playlist.from_dict(video_playlist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



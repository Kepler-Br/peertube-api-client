# AddPlaylist200ResponseVideoPlaylist


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**uuid** | [**Uuid**](Uuid.md) |  | [optional] 
**short_uuid** | **str** | translation of a uuid v4 with a bigger alphabet to have a shorter uuid | [optional] 

## Example

```python
from peertube_api_client.models.add_playlist200_response_video_playlist import AddPlaylist200ResponseVideoPlaylist

# TODO update the JSON string below
json = "{}"
# create an instance of AddPlaylist200ResponseVideoPlaylist from a JSON string
add_playlist200_response_video_playlist_instance = AddPlaylist200ResponseVideoPlaylist.from_json(json)
# print the JSON string representation of the object
print AddPlaylist200ResponseVideoPlaylist.to_json()

# convert the object into a dict
add_playlist200_response_video_playlist_dict = add_playlist200_response_video_playlist_instance.to_dict()
# create an instance of AddPlaylist200ResponseVideoPlaylist from a dict
add_playlist200_response_video_playlist_form_dict = add_playlist200_response_video_playlist.from_dict(add_playlist200_response_video_playlist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



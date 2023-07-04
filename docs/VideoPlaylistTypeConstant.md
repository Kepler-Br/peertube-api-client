# VideoPlaylistTypeConstant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**VideoPlaylistTypeSet**](VideoPlaylistTypeSet.md) |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_playlist_type_constant import VideoPlaylistTypeConstant

# TODO update the JSON string below
json = "{}"
# create an instance of VideoPlaylistTypeConstant from a JSON string
video_playlist_type_constant_instance = VideoPlaylistTypeConstant.from_json(json)
# print the JSON string representation of the object
print VideoPlaylistTypeConstant.to_json()

# convert the object into a dict
video_playlist_type_constant_dict = video_playlist_type_constant_instance.to_dict()
# create an instance of VideoPlaylistTypeConstant from a dict
video_playlist_type_constant_form_dict = video_playlist_type_constant.from_dict(video_playlist_type_constant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



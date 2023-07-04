# VideoPlaylistPrivacyConstant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**VideoPlaylistPrivacySet**](VideoPlaylistPrivacySet.md) |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_playlist_privacy_constant import VideoPlaylistPrivacyConstant

# TODO update the JSON string below
json = "{}"
# create an instance of VideoPlaylistPrivacyConstant from a JSON string
video_playlist_privacy_constant_instance = VideoPlaylistPrivacyConstant.from_json(json)
# print the JSON string representation of the object
print VideoPlaylistPrivacyConstant.to_json()

# convert the object into a dict
video_playlist_privacy_constant_dict = video_playlist_privacy_constant_instance.to_dict()
# create an instance of VideoPlaylistPrivacyConstant from a dict
video_playlist_privacy_constant_form_dict = video_playlist_privacy_constant.from_dict(video_playlist_privacy_constant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



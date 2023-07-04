# AddVideoPlaylistVideo200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_playlist_element** | [**AddVideoPlaylistVideo200ResponseVideoPlaylistElement**](AddVideoPlaylistVideo200ResponseVideoPlaylistElement.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.add_video_playlist_video200_response import AddVideoPlaylistVideo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddVideoPlaylistVideo200Response from a JSON string
add_video_playlist_video200_response_instance = AddVideoPlaylistVideo200Response.from_json(json)
# print the JSON string representation of the object
print AddVideoPlaylistVideo200Response.to_json()

# convert the object into a dict
add_video_playlist_video200_response_dict = add_video_playlist_video200_response_instance.to_dict()
# create an instance of AddVideoPlaylistVideo200Response from a dict
add_video_playlist_video200_response_form_dict = add_video_playlist_video200_response.from_dict(add_video_playlist_video200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



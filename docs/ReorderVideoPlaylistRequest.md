# ReorderVideoPlaylistRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_position** | **int** | Start position of the element to reorder | 
**insert_after_position** | **int** | New position for the block to reorder, to add the block before the first element | 
**reorder_length** | **int** | How many element from &#x60;startPosition&#x60; to reorder | [optional] 

## Example

```python
from peertube_api_client.models.reorder_video_playlist_request import ReorderVideoPlaylistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderVideoPlaylistRequest from a JSON string
reorder_video_playlist_request_instance = ReorderVideoPlaylistRequest.from_json(json)
# print the JSON string representation of the object
print ReorderVideoPlaylistRequest.to_json()

# convert the object into a dict
reorder_video_playlist_request_dict = reorder_video_playlist_request_instance.to_dict()
# create an instance of ReorderVideoPlaylistRequest from a dict
reorder_video_playlist_request_form_dict = reorder_video_playlist_request.from_dict(reorder_video_playlist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



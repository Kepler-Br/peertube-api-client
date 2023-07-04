# AddPlaylist200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_playlist** | [**AddPlaylist200ResponseVideoPlaylist**](AddPlaylist200ResponseVideoPlaylist.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.add_playlist200_response import AddPlaylist200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddPlaylist200Response from a JSON string
add_playlist200_response_instance = AddPlaylist200Response.from_json(json)
# print the JSON string representation of the object
print AddPlaylist200Response.to_json()

# convert the object into a dict
add_playlist200_response_dict = add_playlist200_response_instance.to_dict()
# create an instance of AddPlaylist200Response from a dict
add_playlist200_response_form_dict = add_playlist200_response.from_dict(add_playlist200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



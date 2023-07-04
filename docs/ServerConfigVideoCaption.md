# ServerConfigVideoCaption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | [**ServerConfigVideoCaptionFile**](ServerConfigVideoCaptionFile.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_video_caption import ServerConfigVideoCaption

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigVideoCaption from a JSON string
server_config_video_caption_instance = ServerConfigVideoCaption.from_json(json)
# print the JSON string representation of the object
print ServerConfigVideoCaption.to_json()

# convert the object into a dict
server_config_video_caption_dict = server_config_video_caption_instance.to_dict()
# create an instance of ServerConfigVideoCaption from a dict
server_config_video_caption_form_dict = server_config_video_caption.from_dict(server_config_video_caption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



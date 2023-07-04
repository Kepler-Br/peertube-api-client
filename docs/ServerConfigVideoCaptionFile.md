# ServerConfigVideoCaptionFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | [**ServerConfigAvatarFileSize**](ServerConfigAvatarFileSize.md) |  | [optional] 
**extensions** | **List[str]** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_video_caption_file import ServerConfigVideoCaptionFile

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigVideoCaptionFile from a JSON string
server_config_video_caption_file_instance = ServerConfigVideoCaptionFile.from_json(json)
# print the JSON string representation of the object
print ServerConfigVideoCaptionFile.to_json()

# convert the object into a dict
server_config_video_caption_file_dict = server_config_video_caption_file_instance.to_dict()
# create an instance of ServerConfigVideoCaptionFile from a dict
server_config_video_caption_file_form_dict = server_config_video_caption_file.from_dict(server_config_video_caption_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



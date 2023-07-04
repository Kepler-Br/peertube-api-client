# ServerConfigVideoImage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extensions** | **List[str]** |  | [optional] 
**size** | [**ServerConfigAvatarFileSize**](ServerConfigAvatarFileSize.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_video_image import ServerConfigVideoImage

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigVideoImage from a JSON string
server_config_video_image_instance = ServerConfigVideoImage.from_json(json)
# print the JSON string representation of the object
print ServerConfigVideoImage.to_json()

# convert the object into a dict
server_config_video_image_dict = server_config_video_image_instance.to_dict()
# create an instance of ServerConfigVideoImage from a dict
server_config_video_image_form_dict = server_config_video_image.from_dict(server_config_video_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



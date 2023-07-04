# ServerConfigAvatarFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | [**ServerConfigAvatarFileSize**](ServerConfigAvatarFileSize.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_avatar_file import ServerConfigAvatarFile

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigAvatarFile from a JSON string
server_config_avatar_file_instance = ServerConfigAvatarFile.from_json(json)
# print the JSON string representation of the object
print ServerConfigAvatarFile.to_json()

# convert the object into a dict
server_config_avatar_file_dict = server_config_avatar_file_instance.to_dict()
# create an instance of ServerConfigAvatarFile from a dict
server_config_avatar_file_form_dict = server_config_avatar_file.from_dict(server_config_avatar_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



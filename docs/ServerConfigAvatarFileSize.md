# ServerConfigAvatarFileSize


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | **int** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_avatar_file_size import ServerConfigAvatarFileSize

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigAvatarFileSize from a JSON string
server_config_avatar_file_size_instance = ServerConfigAvatarFileSize.from_json(json)
# print the JSON string representation of the object
print ServerConfigAvatarFileSize.to_json()

# convert the object into a dict
server_config_avatar_file_size_dict = server_config_avatar_file_size_instance.to_dict()
# create an instance of ServerConfigAvatarFileSize from a dict
server_config_avatar_file_size_form_dict = server_config_avatar_file_size.from_dict(server_config_avatar_file_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



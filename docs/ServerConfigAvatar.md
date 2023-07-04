# ServerConfigAvatar


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | [**ServerConfigAvatarFile**](ServerConfigAvatarFile.md) |  | [optional] 
**extensions** | **List[str]** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_avatar import ServerConfigAvatar

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigAvatar from a JSON string
server_config_avatar_instance = ServerConfigAvatar.from_json(json)
# print the JSON string representation of the object
print ServerConfigAvatar.to_json()

# convert the object into a dict
server_config_avatar_dict = server_config_avatar_instance.to_dict()
# create an instance of ServerConfigAvatar from a dict
server_config_avatar_form_dict = server_config_avatar.from_dict(server_config_avatar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



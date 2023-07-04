# ServerConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**ServerConfigInstance**](ServerConfigInstance.md) |  | [optional] 
**search** | [**ServerConfigSearch**](ServerConfigSearch.md) |  | [optional] 
**plugin** | [**ServerConfigPlugin**](ServerConfigPlugin.md) |  | [optional] 
**theme** | [**ServerConfigPlugin**](ServerConfigPlugin.md) |  | [optional] 
**email** | [**ServerConfigEmail**](ServerConfigEmail.md) |  | [optional] 
**contact_form** | [**ServerConfigEmail**](ServerConfigEmail.md) |  | [optional] 
**server_version** | **str** |  | [optional] 
**server_commit** | **str** |  | [optional] 
**signup** | [**ServerConfigSignup**](ServerConfigSignup.md) |  | [optional] 
**transcoding** | [**ServerConfigTranscoding**](ServerConfigTranscoding.md) |  | [optional] 
**var_import** | [**ServerConfigImport**](ServerConfigImport.md) |  | [optional] 
**auto_blacklist** | [**ServerConfigAutoBlacklist**](ServerConfigAutoBlacklist.md) |  | [optional] 
**avatar** | [**ServerConfigAvatar**](ServerConfigAvatar.md) |  | [optional] 
**video** | [**ServerConfigVideo**](ServerConfigVideo.md) |  | [optional] 
**video_caption** | [**ServerConfigVideoCaption**](ServerConfigVideoCaption.md) |  | [optional] 
**user** | [**ServerConfigUser**](ServerConfigUser.md) |  | [optional] 
**trending** | [**ServerConfigTrending**](ServerConfigTrending.md) |  | [optional] 
**tracker** | [**ServerConfigEmail**](ServerConfigEmail.md) |  | [optional] 
**followings** | [**ServerConfigFollowings**](ServerConfigFollowings.md) |  | [optional] 
**homepage** | [**ServerConfigEmail**](ServerConfigEmail.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config import ServerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfig from a JSON string
server_config_instance = ServerConfig.from_json(json)
# print the JSON string representation of the object
print ServerConfig.to_json()

# convert the object into a dict
server_config_dict = server_config_instance.to_dict()
# create an instance of ServerConfig from a dict
server_config_form_dict = server_config.from_dict(server_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



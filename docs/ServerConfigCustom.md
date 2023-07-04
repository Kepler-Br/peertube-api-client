# ServerConfigCustom


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**ServerConfigCustomInstance**](ServerConfigCustomInstance.md) |  | [optional] 
**theme** | [**ServerConfigCustomTheme**](ServerConfigCustomTheme.md) |  | [optional] 
**services** | [**ServerConfigCustomServices**](ServerConfigCustomServices.md) |  | [optional] 
**cache** | [**ServerConfigCustomCache**](ServerConfigCustomCache.md) |  | [optional] 
**signup** | [**ServerConfigCustomSignup**](ServerConfigCustomSignup.md) |  | [optional] 
**admin** | [**ServerConfigCustomAdmin**](ServerConfigCustomAdmin.md) |  | [optional] 
**contact_form** | [**ServerConfigEmail**](ServerConfigEmail.md) |  | [optional] 
**user** | [**ServerConfigCustomUser**](ServerConfigCustomUser.md) |  | [optional] 
**transcoding** | [**ServerConfigCustomTranscoding**](ServerConfigCustomTranscoding.md) |  | [optional] 
**var_import** | [**ServerConfigCustomImport**](ServerConfigCustomImport.md) |  | [optional] 
**auto_blacklist** | [**ServerConfigAutoBlacklist**](ServerConfigAutoBlacklist.md) |  | [optional] 
**followers** | [**ServerConfigCustomFollowers**](ServerConfigCustomFollowers.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_custom import ServerConfigCustom

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigCustom from a JSON string
server_config_custom_instance = ServerConfigCustom.from_json(json)
# print the JSON string representation of the object
print ServerConfigCustom.to_json()

# convert the object into a dict
server_config_custom_dict = server_config_custom_instance.to_dict()
# create an instance of ServerConfigCustom from a dict
server_config_custom_form_dict = server_config_custom.from_dict(server_config_custom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ServerConfigPlugin


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registered** | **List[str]** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_plugin import ServerConfigPlugin

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigPlugin from a JSON string
server_config_plugin_instance = ServerConfigPlugin.from_json(json)
# print the JSON string representation of the object
print ServerConfigPlugin.to_json()

# convert the object into a dict
server_config_plugin_dict = server_config_plugin_instance.to_dict()
# create an instance of ServerConfigPlugin from a dict
server_config_plugin_form_dict = server_config_plugin.from_dict(server_config_plugin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



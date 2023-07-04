# UninstallPluginRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**npm_name** | **str** | name of the plugin/theme in its package.json | 

## Example

```python
from peertube_api_client.models.uninstall_plugin_request import UninstallPluginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UninstallPluginRequest from a JSON string
uninstall_plugin_request_instance = UninstallPluginRequest.from_json(json)
# print the JSON string representation of the object
print UninstallPluginRequest.to_json()

# convert the object into a dict
uninstall_plugin_request_dict = uninstall_plugin_request_instance.to_dict()
# create an instance of UninstallPluginRequest from a dict
uninstall_plugin_request_form_dict = uninstall_plugin_request.from_dict(uninstall_plugin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



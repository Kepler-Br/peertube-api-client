# ServerConfigCustomAdmin


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_custom_admin import ServerConfigCustomAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigCustomAdmin from a JSON string
server_config_custom_admin_instance = ServerConfigCustomAdmin.from_json(json)
# print the JSON string representation of the object
print ServerConfigCustomAdmin.to_json()

# convert the object into a dict
server_config_custom_admin_dict = server_config_custom_admin_instance.to_dict()
# create an instance of ServerConfigCustomAdmin from a dict
server_config_custom_admin_form_dict = server_config_custom_admin.from_dict(server_config_custom_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



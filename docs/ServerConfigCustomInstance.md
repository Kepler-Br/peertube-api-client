# ServerConfigCustomInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**terms** | **str** |  | [optional] 
**default_client_route** | **str** |  | [optional] 
**is_nsfw** | **bool** |  | [optional] 
**default_nsfw_policy** | **str** |  | [optional] 
**customizations** | [**ServerConfigInstanceCustomizations**](ServerConfigInstanceCustomizations.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_custom_instance import ServerConfigCustomInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigCustomInstance from a JSON string
server_config_custom_instance_instance = ServerConfigCustomInstance.from_json(json)
# print the JSON string representation of the object
print ServerConfigCustomInstance.to_json()

# convert the object into a dict
server_config_custom_instance_dict = server_config_custom_instance_instance.to_dict()
# create an instance of ServerConfigCustomInstance from a dict
server_config_custom_instance_form_dict = server_config_custom_instance.from_dict(server_config_custom_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



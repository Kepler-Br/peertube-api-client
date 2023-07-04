# ServerConfigInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**default_client_route** | **str** |  | [optional] 
**is_nsfw** | **bool** |  | [optional] 
**default_nsfw_policy** | **str** |  | [optional] 
**customizations** | [**ServerConfigInstanceCustomizations**](ServerConfigInstanceCustomizations.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_instance import ServerConfigInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigInstance from a JSON string
server_config_instance_instance = ServerConfigInstance.from_json(json)
# print the JSON string representation of the object
print ServerConfigInstance.to_json()

# convert the object into a dict
server_config_instance_dict = server_config_instance_instance.to_dict()
# create an instance of ServerConfigInstance from a dict
server_config_instance_form_dict = server_config_instance.from_dict(server_config_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



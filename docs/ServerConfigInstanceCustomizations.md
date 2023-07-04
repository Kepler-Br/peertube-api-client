# ServerConfigInstanceCustomizations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**javascript** | **str** |  | [optional] 
**css** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_instance_customizations import ServerConfigInstanceCustomizations

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigInstanceCustomizations from a JSON string
server_config_instance_customizations_instance = ServerConfigInstanceCustomizations.from_json(json)
# print the JSON string representation of the object
print ServerConfigInstanceCustomizations.to_json()

# convert the object into a dict
server_config_instance_customizations_dict = server_config_instance_customizations_instance.to_dict()
# create an instance of ServerConfigInstanceCustomizations from a dict
server_config_instance_customizations_form_dict = server_config_instance_customizations.from_dict(server_config_instance_customizations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



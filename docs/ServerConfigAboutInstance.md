# ServerConfigAboutInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**terms** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_about_instance import ServerConfigAboutInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigAboutInstance from a JSON string
server_config_about_instance_instance = ServerConfigAboutInstance.from_json(json)
# print the JSON string representation of the object
print ServerConfigAboutInstance.to_json()

# convert the object into a dict
server_config_about_instance_dict = server_config_about_instance_instance.to_dict()
# create an instance of ServerConfigAboutInstance from a dict
server_config_about_instance_form_dict = server_config_about_instance.from_dict(server_config_about_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



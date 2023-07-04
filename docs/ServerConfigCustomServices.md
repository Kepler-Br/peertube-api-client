# ServerConfigCustomServices


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**twitter** | [**ServerConfigCustomServicesTwitter**](ServerConfigCustomServicesTwitter.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_custom_services import ServerConfigCustomServices

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigCustomServices from a JSON string
server_config_custom_services_instance = ServerConfigCustomServices.from_json(json)
# print the JSON string representation of the object
print ServerConfigCustomServices.to_json()

# convert the object into a dict
server_config_custom_services_dict = server_config_custom_services_instance.to_dict()
# create an instance of ServerConfigCustomServices from a dict
server_config_custom_services_form_dict = server_config_custom_services.from_dict(server_config_custom_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



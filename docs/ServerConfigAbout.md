# ServerConfigAbout


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**ServerConfigAboutInstance**](ServerConfigAboutInstance.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_about import ServerConfigAbout

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigAbout from a JSON string
server_config_about_instance = ServerConfigAbout.from_json(json)
# print the JSON string representation of the object
print ServerConfigAbout.to_json()

# convert the object into a dict
server_config_about_dict = server_config_about_instance.to_dict()
# create an instance of ServerConfigAbout from a dict
server_config_about_form_dict = server_config_about.from_dict(server_config_about_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



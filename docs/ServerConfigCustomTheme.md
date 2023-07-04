# ServerConfigCustomTheme


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_custom_theme import ServerConfigCustomTheme

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigCustomTheme from a JSON string
server_config_custom_theme_instance = ServerConfigCustomTheme.from_json(json)
# print the JSON string representation of the object
print ServerConfigCustomTheme.to_json()

# convert the object into a dict
server_config_custom_theme_dict = server_config_custom_theme_instance.to_dict()
# create an instance of ServerConfigCustomTheme from a dict
server_config_custom_theme_form_dict = server_config_custom_theme.from_dict(server_config_custom_theme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



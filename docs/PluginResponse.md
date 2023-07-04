# PluginResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**data** | [**List[Plugin]**](Plugin.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.plugin_response import PluginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PluginResponse from a JSON string
plugin_response_instance = PluginResponse.from_json(json)
# print the JSON string representation of the object
print PluginResponse.to_json()

# convert the object into a dict
plugin_response_dict = plugin_response_instance.to_dict()
# create an instance of PluginResponse from a dict
plugin_response_form_dict = plugin_response.from_dict(plugin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



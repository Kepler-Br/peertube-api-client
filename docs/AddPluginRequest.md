# AddPluginRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**npm_name** | **str** |  | 
**path** | **str** |  | 

## Example

```python
from peertube_api_client.models.add_plugin_request import AddPluginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddPluginRequest from a JSON string
add_plugin_request_instance = AddPluginRequest.from_json(json)
# print the JSON string representation of the object
print AddPluginRequest.to_json()

# convert the object into a dict
add_plugin_request_dict = add_plugin_request_instance.to_dict()
# create an instance of AddPluginRequest from a dict
add_plugin_request_form_dict = add_plugin_request.from_dict(add_plugin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



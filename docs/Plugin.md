# Plugin


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **int** | - &#x60;1&#x60;: PLUGIN - &#x60;2&#x60;: THEME  | [optional] 
**latest_version** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**uninstalled** | **bool** |  | [optional] 
**peertube_engine** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**homepage** | **str** |  | [optional] 
**settings** | **Dict[str, object]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from peertube_api_client.models.plugin import Plugin

# TODO update the JSON string below
json = "{}"
# create an instance of Plugin from a JSON string
plugin_instance = Plugin.from_json(json)
# print the JSON string representation of the object
print Plugin.to_json()

# convert the object into a dict
plugin_dict = plugin_instance.to_dict()
# create an instance of Plugin from a dict
plugin_form_dict = plugin.from_dict(plugin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



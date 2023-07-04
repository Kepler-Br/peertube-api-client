# ServerConfigCustomCache


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previews** | [**ServerConfigCustomCachePreviews**](ServerConfigCustomCachePreviews.md) |  | [optional] 
**captions** | [**ServerConfigCustomCachePreviews**](ServerConfigCustomCachePreviews.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_custom_cache import ServerConfigCustomCache

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigCustomCache from a JSON string
server_config_custom_cache_instance = ServerConfigCustomCache.from_json(json)
# print the JSON string representation of the object
print ServerConfigCustomCache.to_json()

# convert the object into a dict
server_config_custom_cache_dict = server_config_custom_cache_instance.to_dict()
# create an instance of ServerConfigCustomCache from a dict
server_config_custom_cache_form_dict = server_config_custom_cache.from_dict(server_config_custom_cache_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



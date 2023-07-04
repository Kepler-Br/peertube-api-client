# ServerConfigSearchRemoteUri


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **bool** |  | [optional] 
**anonymous** | **bool** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_search_remote_uri import ServerConfigSearchRemoteUri

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigSearchRemoteUri from a JSON string
server_config_search_remote_uri_instance = ServerConfigSearchRemoteUri.from_json(json)
# print the JSON string representation of the object
print ServerConfigSearchRemoteUri.to_json()

# convert the object into a dict
server_config_search_remote_uri_dict = server_config_search_remote_uri_instance.to_dict()
# create an instance of ServerConfigSearchRemoteUri from a dict
server_config_search_remote_uri_form_dict = server_config_search_remote_uri.from_dict(server_config_search_remote_uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ServerConfigSearch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_uri** | [**ServerConfigSearchRemoteUri**](ServerConfigSearchRemoteUri.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_search import ServerConfigSearch

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigSearch from a JSON string
server_config_search_instance = ServerConfigSearch.from_json(json)
# print the JSON string representation of the object
print ServerConfigSearch.to_json()

# convert the object into a dict
server_config_search_dict = server_config_search_instance.to_dict()
# create an instance of ServerConfigSearch from a dict
server_config_search_form_dict = server_config_search.from_dict(server_config_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



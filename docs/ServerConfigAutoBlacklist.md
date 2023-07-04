# ServerConfigAutoBlacklist


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**videos** | [**ServerConfigAutoBlacklistVideos**](ServerConfigAutoBlacklistVideos.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_auto_blacklist import ServerConfigAutoBlacklist

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigAutoBlacklist from a JSON string
server_config_auto_blacklist_instance = ServerConfigAutoBlacklist.from_json(json)
# print the JSON string representation of the object
print ServerConfigAutoBlacklist.to_json()

# convert the object into a dict
server_config_auto_blacklist_dict = server_config_auto_blacklist_instance.to_dict()
# create an instance of ServerConfigAutoBlacklist from a dict
server_config_auto_blacklist_form_dict = server_config_auto_blacklist.from_dict(server_config_auto_blacklist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



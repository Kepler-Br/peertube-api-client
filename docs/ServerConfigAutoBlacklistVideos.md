# ServerConfigAutoBlacklistVideos


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**of_users** | [**ServerConfigEmail**](ServerConfigEmail.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_auto_blacklist_videos import ServerConfigAutoBlacklistVideos

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigAutoBlacklistVideos from a JSON string
server_config_auto_blacklist_videos_instance = ServerConfigAutoBlacklistVideos.from_json(json)
# print the JSON string representation of the object
print ServerConfigAutoBlacklistVideos.to_json()

# convert the object into a dict
server_config_auto_blacklist_videos_dict = server_config_auto_blacklist_videos_instance.to_dict()
# create an instance of ServerConfigAutoBlacklistVideos from a dict
server_config_auto_blacklist_videos_form_dict = server_config_auto_blacklist_videos.from_dict(server_config_auto_blacklist_videos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



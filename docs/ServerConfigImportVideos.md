# ServerConfigImportVideos


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http** | [**ServerConfigEmail**](ServerConfigEmail.md) |  | [optional] 
**torrent** | [**ServerConfigEmail**](ServerConfigEmail.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_import_videos import ServerConfigImportVideos

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigImportVideos from a JSON string
server_config_import_videos_instance = ServerConfigImportVideos.from_json(json)
# print the JSON string representation of the object
print ServerConfigImportVideos.to_json()

# convert the object into a dict
server_config_import_videos_dict = server_config_import_videos_instance.to_dict()
# create an instance of ServerConfigImportVideos from a dict
server_config_import_videos_form_dict = server_config_import_videos.from_dict(server_config_import_videos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



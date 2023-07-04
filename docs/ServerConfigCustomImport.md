# ServerConfigCustomImport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**videos** | [**ServerConfigImportVideos**](ServerConfigImportVideos.md) |  | [optional] 
**video_channel_synchronization** | [**ServerConfigEmail**](ServerConfigEmail.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_custom_import import ServerConfigCustomImport

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigCustomImport from a JSON string
server_config_custom_import_instance = ServerConfigCustomImport.from_json(json)
# print the JSON string representation of the object
print ServerConfigCustomImport.to_json()

# convert the object into a dict
server_config_custom_import_dict = server_config_custom_import_instance.to_dict()
# create an instance of ServerConfigCustomImport from a dict
server_config_custom_import_form_dict = server_config_custom_import.from_dict(server_config_custom_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



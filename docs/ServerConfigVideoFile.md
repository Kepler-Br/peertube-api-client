# ServerConfigVideoFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extensions** | **List[str]** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_video_file import ServerConfigVideoFile

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigVideoFile from a JSON string
server_config_video_file_instance = ServerConfigVideoFile.from_json(json)
# print the JSON string representation of the object
print ServerConfigVideoFile.to_json()

# convert the object into a dict
server_config_video_file_dict = server_config_video_file_instance.to_dict()
# create an instance of ServerConfigVideoFile from a dict
server_config_video_file_form_dict = server_config_video_file.from_dict(server_config_video_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



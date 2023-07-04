# ServerConfigVideo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**ServerConfigVideoImage**](ServerConfigVideoImage.md) |  | [optional] 
**file** | [**ServerConfigVideoFile**](ServerConfigVideoFile.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_video import ServerConfigVideo

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigVideo from a JSON string
server_config_video_instance = ServerConfigVideo.from_json(json)
# print the JSON string representation of the object
print ServerConfigVideo.to_json()

# convert the object into a dict
server_config_video_dict = server_config_video_instance.to_dict()
# create an instance of ServerConfigVideo from a dict
server_config_video_form_dict = server_config_video.from_dict(server_config_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



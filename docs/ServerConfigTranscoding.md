# ServerConfigTranscoding


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hls** | [**ServerConfigEmail**](ServerConfigEmail.md) |  | [optional] 
**webtorrent** | [**ServerConfigEmail**](ServerConfigEmail.md) |  | [optional] 
**enabled_resolutions** | **List[int]** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_transcoding import ServerConfigTranscoding

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigTranscoding from a JSON string
server_config_transcoding_instance = ServerConfigTranscoding.from_json(json)
# print the JSON string representation of the object
print ServerConfigTranscoding.to_json()

# convert the object into a dict
server_config_transcoding_dict = server_config_transcoding_instance.to_dict()
# create an instance of ServerConfigTranscoding from a dict
server_config_transcoding_form_dict = server_config_transcoding.from_dict(server_config_transcoding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



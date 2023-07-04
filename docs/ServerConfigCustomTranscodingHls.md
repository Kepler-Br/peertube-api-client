# ServerConfigCustomTranscodingHls

HLS-specific settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_custom_transcoding_hls import ServerConfigCustomTranscodingHls

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigCustomTranscodingHls from a JSON string
server_config_custom_transcoding_hls_instance = ServerConfigCustomTranscodingHls.from_json(json)
# print the JSON string representation of the object
print ServerConfigCustomTranscodingHls.to_json()

# convert the object into a dict
server_config_custom_transcoding_hls_dict = server_config_custom_transcoding_hls_instance.to_dict()
# create an instance of ServerConfigCustomTranscodingHls from a dict
server_config_custom_transcoding_hls_form_dict = server_config_custom_transcoding_hls.from_dict(server_config_custom_transcoding_hls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



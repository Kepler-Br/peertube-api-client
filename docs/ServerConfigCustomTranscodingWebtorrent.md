# ServerConfigCustomTranscodingWebtorrent

WebTorrent-specific settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_custom_transcoding_webtorrent import ServerConfigCustomTranscodingWebtorrent

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigCustomTranscodingWebtorrent from a JSON string
server_config_custom_transcoding_webtorrent_instance = ServerConfigCustomTranscodingWebtorrent.from_json(json)
# print the JSON string representation of the object
print ServerConfigCustomTranscodingWebtorrent.to_json()

# convert the object into a dict
server_config_custom_transcoding_webtorrent_dict = server_config_custom_transcoding_webtorrent_instance.to_dict()
# create an instance of ServerConfigCustomTranscodingWebtorrent from a dict
server_config_custom_transcoding_webtorrent_form_dict = server_config_custom_transcoding_webtorrent.from_dict(server_config_custom_transcoding_webtorrent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



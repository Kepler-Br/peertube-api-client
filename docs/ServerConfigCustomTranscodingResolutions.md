# ServerConfigCustomTranscodingResolutions

Resolutions to transcode _new videos_ to

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_0p** | **bool** |  | [optional] 
**var_144p** | **bool** |  | [optional] 
**var_240p** | **bool** |  | [optional] 
**var_360p** | **bool** |  | [optional] 
**var_480p** | **bool** |  | [optional] 
**var_720p** | **bool** |  | [optional] 
**var_1080p** | **bool** |  | [optional] 
**var_1440p** | **bool** |  | [optional] 
**var_2160p** | **bool** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_custom_transcoding_resolutions import ServerConfigCustomTranscodingResolutions

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigCustomTranscodingResolutions from a JSON string
server_config_custom_transcoding_resolutions_instance = ServerConfigCustomTranscodingResolutions.from_json(json)
# print the JSON string representation of the object
print ServerConfigCustomTranscodingResolutions.to_json()

# convert the object into a dict
server_config_custom_transcoding_resolutions_dict = server_config_custom_transcoding_resolutions_instance.to_dict()
# create an instance of ServerConfigCustomTranscodingResolutions from a dict
server_config_custom_transcoding_resolutions_form_dict = server_config_custom_transcoding_resolutions.from_dict(server_config_custom_transcoding_resolutions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



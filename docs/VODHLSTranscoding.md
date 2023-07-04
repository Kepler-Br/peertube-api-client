# VODHLSTranscoding


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_file** | **bytearray** |  | [optional] 
**resolution_playlist_file** | **bytearray** |  | [optional] 

## Example

```python
from peertube_api_client.models.vodhls_transcoding import VODHLSTranscoding

# TODO update the JSON string below
json = "{}"
# create an instance of VODHLSTranscoding from a JSON string
vodhls_transcoding_instance = VODHLSTranscoding.from_json(json)
# print the JSON string representation of the object
print VODHLSTranscoding.to_json()

# convert the object into a dict
vodhls_transcoding_dict = vodhls_transcoding_instance.to_dict()
# create an instance of VODHLSTranscoding from a dict
vodhls_transcoding_form_dict = vodhls_transcoding.from_dict(vodhls_transcoding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



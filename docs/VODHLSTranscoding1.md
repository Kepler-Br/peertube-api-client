# VODHLSTranscoding1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**VODWebVideoTranscoding1Input**](VODWebVideoTranscoding1Input.md) |  | [optional] 
**output** | [**VODWebVideoTranscoding1Output**](VODWebVideoTranscoding1Output.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.vodhls_transcoding1 import VODHLSTranscoding1

# TODO update the JSON string below
json = "{}"
# create an instance of VODHLSTranscoding1 from a JSON string
vodhls_transcoding1_instance = VODHLSTranscoding1.from_json(json)
# print the JSON string representation of the object
print VODHLSTranscoding1.to_json()

# convert the object into a dict
vodhls_transcoding1_dict = vodhls_transcoding1_instance.to_dict()
# create an instance of VODHLSTranscoding1 from a dict
vodhls_transcoding1_form_dict = vodhls_transcoding1.from_dict(vodhls_transcoding1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



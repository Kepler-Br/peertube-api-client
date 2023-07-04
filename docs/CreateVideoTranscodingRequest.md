# CreateVideoTranscodingRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transcoding_type** | **str** |  | 

## Example

```python
from peertube_api_client.models.create_video_transcoding_request import CreateVideoTranscodingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVideoTranscodingRequest from a JSON string
create_video_transcoding_request_instance = CreateVideoTranscodingRequest.from_json(json)
# print the JSON string representation of the object
print CreateVideoTranscodingRequest.to_json()

# convert the object into a dict
create_video_transcoding_request_dict = create_video_transcoding_request_instance.to_dict()
# create an instance of CreateVideoTranscodingRequest from a dict
create_video_transcoding_request_form_dict = create_video_transcoding_request.from_dict(create_video_transcoding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



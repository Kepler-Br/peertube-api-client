# VideoUploadResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video** | [**VideoUploadResponseVideo**](VideoUploadResponseVideo.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_upload_response import VideoUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VideoUploadResponse from a JSON string
video_upload_response_instance = VideoUploadResponse.from_json(json)
# print the JSON string representation of the object
print VideoUploadResponse.to_json()

# convert the object into a dict
video_upload_response_dict = video_upload_response_instance.to_dict()
# create an instance of VideoUploadResponse from a dict
video_upload_response_form_dict = video_upload_response.from_dict(video_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



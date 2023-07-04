# VideoUploadResponseVideo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**uuid** | **str** |  | [optional] 
**short_uuid** | **str** | translation of a uuid v4 with a bigger alphabet to have a shorter uuid | [optional] 

## Example

```python
from peertube_api_client.models.video_upload_response_video import VideoUploadResponseVideo

# TODO update the JSON string below
json = "{}"
# create an instance of VideoUploadResponseVideo from a JSON string
video_upload_response_video_instance = VideoUploadResponseVideo.from_json(json)
# print the JSON string representation of the object
print VideoUploadResponseVideo.to_json()

# convert the object into a dict
video_upload_response_video_dict = video_upload_response_video_instance.to_dict()
# create an instance of VideoUploadResponseVideo from a dict
video_upload_response_video_form_dict = video_upload_response_video.from_dict(video_upload_response_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



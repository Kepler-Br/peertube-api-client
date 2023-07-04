# VideoUploadRequestResumable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Video name | 
**channel_id** | **int** | Channel id that will contain this video | 
**privacy** | [**VideoPrivacySet**](VideoPrivacySet.md) |  | [optional] 
**category** | **int** | category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
**licence** | **int** | licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
**language** | **str** | language id of the video (see [/videos/languages](#operation/getLanguages)) | [optional] 
**description** | **str** | Video description | [optional] 
**wait_transcoding** | **bool** | Whether or not we wait transcoding before publish the video | [optional] 
**support** | **str** | A text tell the audience how to support the video creator | [optional] 
**nsfw** | **bool** | Whether or not this video contains sensitive content | [optional] 
**tags** | **List[str]** | Video tags (maximum 5 tags each between 2 and 30 characters) | [optional] 
**comments_enabled** | **bool** | Enable or disable comments for this video | [optional] 
**download_enabled** | **bool** | Enable or disable downloading for this video | [optional] 
**originally_published_at** | **datetime** | Date when the content was originally published | [optional] 
**schedule_update** | [**VideoScheduledUpdate**](VideoScheduledUpdate.md) |  | [optional] 
**thumbnailfile** | **bytearray** | Video thumbnail file | [optional] 
**previewfile** | **bytearray** | Video preview file | [optional] 
**filename** | **str** | Video filename including extension | 

## Example

```python
from peertube_api_client.models.video_upload_request_resumable import VideoUploadRequestResumable

# TODO update the JSON string below
json = "{}"
# create an instance of VideoUploadRequestResumable from a JSON string
video_upload_request_resumable_instance = VideoUploadRequestResumable.from_json(json)
# print the JSON string representation of the object
print VideoUploadRequestResumable.to_json()

# convert the object into a dict
video_upload_request_resumable_dict = video_upload_request_resumable_instance.to_dict()
# create an instance of VideoUploadRequestResumable from a dict
video_upload_request_resumable_form_dict = video_upload_request_resumable.from_dict(video_upload_request_resumable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



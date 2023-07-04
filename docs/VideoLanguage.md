# VideoLanguage

main language used in the video

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | language id of the video (see [/videos/languages](#operation/getLanguages)) | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_language import VideoLanguage

# TODO update the JSON string below
json = "{}"
# create an instance of VideoLanguage from a JSON string
video_language_instance = VideoLanguage.from_json(json)
# print the JSON string representation of the object
print VideoLanguage.to_json()

# convert the object into a dict
video_language_dict = video_language_instance.to_dict()
# create an instance of VideoLanguage from a dict
video_language_form_dict = video_language.from_dict(video_language_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



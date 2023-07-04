# VideoConstantStringLanguage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | language id of the video (see [/videos/languages](#operation/getLanguages)) | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_constant_string_language import VideoConstantStringLanguage

# TODO update the JSON string below
json = "{}"
# create an instance of VideoConstantStringLanguage from a JSON string
video_constant_string_language_instance = VideoConstantStringLanguage.from_json(json)
# print the JSON string representation of the object
print VideoConstantStringLanguage.to_json()

# convert the object into a dict
video_constant_string_language_dict = video_constant_string_language_instance.to_dict()
# create an instance of VideoConstantStringLanguage from a dict
video_constant_string_language_form_dict = video_constant_string_language.from_dict(video_constant_string_language_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# VideoResolutionConstant

resolutions and their labels for the video

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Video resolution (&#x60;0&#x60;, &#x60;240&#x60;, &#x60;360&#x60;, &#x60;720&#x60;, &#x60;1080&#x60;, &#x60;1440&#x60; or &#x60;2160&#x60;)  &#x60;0&#x60; is used as a special value for stillimage videos dedicated to audio, a.k.a. audio-only videos.  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_resolution_constant import VideoResolutionConstant

# TODO update the JSON string below
json = "{}"
# create an instance of VideoResolutionConstant from a JSON string
video_resolution_constant_instance = VideoResolutionConstant.from_json(json)
# print the JSON string representation of the object
print VideoResolutionConstant.to_json()

# convert the object into a dict
video_resolution_constant_dict = video_resolution_constant_instance.to_dict()
# create an instance of VideoResolutionConstant from a dict
video_resolution_constant_form_dict = video_resolution_constant.from_dict(video_resolution_constant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



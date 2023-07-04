# VideoCaption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | [**VideoConstantStringLanguage**](VideoConstantStringLanguage.md) |  | [optional] 
**caption_path** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_caption import VideoCaption

# TODO update the JSON string below
json = "{}"
# create an instance of VideoCaption from a JSON string
video_caption_instance = VideoCaption.from_json(json)
# print the JSON string representation of the object
print VideoCaption.to_json()

# convert the object into a dict
video_caption_dict = video_caption_instance.to_dict()
# create an instance of VideoCaption from a dict
video_caption_form_dict = video_caption.from_dict(video_caption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



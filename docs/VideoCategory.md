# VideoCategory

category in which the video is classified

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_category import VideoCategory

# TODO update the JSON string below
json = "{}"
# create an instance of VideoCategory from a JSON string
video_category_instance = VideoCategory.from_json(json)
# print the JSON string representation of the object
print VideoCategory.to_json()

# convert the object into a dict
video_category_dict = video_category_instance.to_dict()
# create an instance of VideoCategory from a dict
video_category_form_dict = video_category.from_dict(video_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



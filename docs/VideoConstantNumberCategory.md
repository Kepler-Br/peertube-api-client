# VideoConstantNumberCategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_constant_number_category import VideoConstantNumberCategory

# TODO update the JSON string below
json = "{}"
# create an instance of VideoConstantNumberCategory from a JSON string
video_constant_number_category_instance = VideoConstantNumberCategory.from_json(json)
# print the JSON string representation of the object
print VideoConstantNumberCategory.to_json()

# convert the object into a dict
video_constant_number_category_dict = video_constant_number_category_instance.to_dict()
# create an instance of VideoConstantNumberCategory from a dict
video_constant_number_category_form_dict = video_constant_number_category.from_dict(video_constant_number_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



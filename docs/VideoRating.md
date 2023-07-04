# VideoRating


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video** | [**Video**](Video.md) |  | 
**rating** | **str** | Rating of the video | 

## Example

```python
from peertube_api_client.models.video_rating import VideoRating

# TODO update the JSON string below
json = "{}"
# create an instance of VideoRating from a JSON string
video_rating_instance = VideoRating.from_json(json)
# print the JSON string representation of the object
print VideoRating.to_json()

# convert the object into a dict
video_rating_dict = video_rating_instance.to_dict()
# create an instance of VideoRating from a dict
video_rating_form_dict = video_rating.from_dict(video_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



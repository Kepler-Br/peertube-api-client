# GetMeVideoRating


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**rating** | **str** | Rating of the video | 

## Example

```python
from peertube_api_client.models.get_me_video_rating import GetMeVideoRating

# TODO update the JSON string below
json = "{}"
# create an instance of GetMeVideoRating from a JSON string
get_me_video_rating_instance = GetMeVideoRating.from_json(json)
# print the JSON string representation of the object
print GetMeVideoRating.to_json()

# convert the object into a dict
get_me_video_rating_dict = get_me_video_rating_instance.to_dict()
# create an instance of GetMeVideoRating from a dict
get_me_video_rating_form_dict = get_me_video_rating.from_dict(get_me_video_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



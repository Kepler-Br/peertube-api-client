# UserViewingVideo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_time** | **int** | timestamp within the video, in seconds | 
**view_event** | **str** | Event since last viewing call:  * &#x60;seek&#x60; - If the user seeked the video  | [optional] 

## Example

```python
from peertube_api_client.models.user_viewing_video import UserViewingVideo

# TODO update the JSON string below
json = "{}"
# create an instance of UserViewingVideo from a JSON string
user_viewing_video_instance = UserViewingVideo.from_json(json)
# print the JSON string representation of the object
print UserViewingVideo.to_json()

# convert the object into a dict
user_viewing_video_dict = user_viewing_video_instance.to_dict()
# create an instance of UserViewingVideo from a dict
user_viewing_video_form_dict = user_viewing_video.from_dict(user_viewing_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



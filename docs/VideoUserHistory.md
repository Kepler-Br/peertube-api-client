# VideoUserHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_time** | **int** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_user_history import VideoUserHistory

# TODO update the JSON string below
json = "{}"
# create an instance of VideoUserHistory from a JSON string
video_user_history_instance = VideoUserHistory.from_json(json)
# print the JSON string representation of the object
print VideoUserHistory.to_json()

# convert the object into a dict
video_user_history_dict = video_user_history_instance.to_dict()
# create an instance of VideoUserHistory from a dict
video_user_history_form_dict = video_user_history.from_dict(video_user_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



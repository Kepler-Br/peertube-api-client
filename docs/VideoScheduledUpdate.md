# VideoScheduledUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privacy** | [**VideoPrivacySet**](VideoPrivacySet.md) |  | [optional] 
**update_at** | **date** | When to update the video | 

## Example

```python
from peertube_api_client.models.video_scheduled_update import VideoScheduledUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of VideoScheduledUpdate from a JSON string
video_scheduled_update_instance = VideoScheduledUpdate.from_json(json)
# print the JSON string representation of the object
print VideoScheduledUpdate.to_json()

# convert the object into a dict
video_scheduled_update_dict = video_scheduled_update_instance.to_dict()
# create an instance of VideoScheduledUpdate from a dict
video_scheduled_update_form_dict = video_scheduled_update.from_dict(video_scheduled_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# NotificationVideoAbuse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**video** | [**NotificationVideoAbuseVideo**](NotificationVideoAbuseVideo.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.notification_video_abuse import NotificationVideoAbuse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationVideoAbuse from a JSON string
notification_video_abuse_instance = NotificationVideoAbuse.from_json(json)
# print the JSON string representation of the object
print NotificationVideoAbuse.to_json()

# convert the object into a dict
notification_video_abuse_dict = notification_video_abuse_instance.to_dict()
# create an instance of NotificationVideoAbuse from a dict
notification_video_abuse_form_dict = notification_video_abuse.from_dict(notification_video_abuse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



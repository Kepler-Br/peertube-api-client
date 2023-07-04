# NotificationVideoAbuseVideo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**uuid** | [**Uuid**](Uuid.md) |  | [optional] 
**name** | [**Name**](Name.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.notification_video_abuse_video import NotificationVideoAbuseVideo

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationVideoAbuseVideo from a JSON string
notification_video_abuse_video_instance = NotificationVideoAbuseVideo.from_json(json)
# print the JSON string representation of the object
print NotificationVideoAbuseVideo.to_json()

# convert the object into a dict
notification_video_abuse_video_dict = notification_video_abuse_video_instance.to_dict()
# create an instance of NotificationVideoAbuseVideo from a dict
notification_video_abuse_video_form_dict = notification_video_abuse_video.from_dict(notification_video_abuse_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



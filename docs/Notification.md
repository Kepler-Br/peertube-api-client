# Notification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **int** | Notification type, following the &#x60;UserNotificationType&#x60; enum: - &#x60;1&#x60; NEW_VIDEO_FROM_SUBSCRIPTION - &#x60;2&#x60; NEW_COMMENT_ON_MY_VIDEO - &#x60;3&#x60; NEW_ABUSE_FOR_MODERATORS - &#x60;4&#x60; BLACKLIST_ON_MY_VIDEO - &#x60;5&#x60; UNBLACKLIST_ON_MY_VIDEO - &#x60;6&#x60; MY_VIDEO_PUBLISHED - &#x60;7&#x60; MY_VIDEO_IMPORT_SUCCESS - &#x60;8&#x60; MY_VIDEO_IMPORT_ERROR - &#x60;9&#x60; NEW_USER_REGISTRATION - &#x60;10&#x60; NEW_FOLLOW - &#x60;11&#x60; COMMENT_MENTION - &#x60;12&#x60; VIDEO_AUTO_BLACKLIST_FOR_MODERATORS - &#x60;13&#x60; NEW_INSTANCE_FOLLOWER - &#x60;14&#x60; AUTO_INSTANCE_FOLLOWING - &#x60;15&#x60; ABUSE_STATE_CHANGE - &#x60;16&#x60; ABUSE_NEW_MESSAGE - &#x60;17&#x60; NEW_PLUGIN_VERSION - &#x60;18&#x60; NEW_PEERTUBE_VERSION  | [optional] 
**read** | **bool** |  | [optional] 
**video** | [**NotificationVideo**](NotificationVideo.md) |  | [optional] 
**video_import** | [**NotificationVideoImport**](NotificationVideoImport.md) |  | [optional] 
**comment** | [**NotificationComment**](NotificationComment.md) |  | [optional] 
**video_abuse** | [**NotificationVideoAbuse**](NotificationVideoAbuse.md) |  | [optional] 
**video_blacklist** | [**NotificationVideoAbuse**](NotificationVideoAbuse.md) |  | [optional] 
**account** | [**ActorInfo**](ActorInfo.md) |  | [optional] 
**actor_follow** | [**NotificationActorFollow**](NotificationActorFollow.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from peertube_api_client.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print Notification.to_json()

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_form_dict = notification.from_dict(notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



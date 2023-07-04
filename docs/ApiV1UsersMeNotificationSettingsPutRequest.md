# ApiV1UsersMeNotificationSettingsPutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_video_from_subscription** | **int** | Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL  | [optional] 
**new_comment_on_my_video** | **int** | Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL  | [optional] 
**abuse_as_moderator** | **int** | Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL  | [optional] 
**video_auto_blacklist_as_moderator** | **int** | Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL  | [optional] 
**blacklist_on_my_video** | **int** | Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL  | [optional] 
**my_video_published** | **int** | Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL  | [optional] 
**my_video_import_finished** | **int** | Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL  | [optional] 
**new_follow** | **int** | Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL  | [optional] 
**new_user_registration** | **int** | Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL  | [optional] 
**comment_mention** | **int** | Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL  | [optional] 
**new_instance_follower** | **int** | Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL  | [optional] 
**auto_instance_following** | **int** | Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL  | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_users_me_notification_settings_put_request import ApiV1UsersMeNotificationSettingsPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1UsersMeNotificationSettingsPutRequest from a JSON string
api_v1_users_me_notification_settings_put_request_instance = ApiV1UsersMeNotificationSettingsPutRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1UsersMeNotificationSettingsPutRequest.to_json()

# convert the object into a dict
api_v1_users_me_notification_settings_put_request_dict = api_v1_users_me_notification_settings_put_request_instance.to_dict()
# create an instance of ApiV1UsersMeNotificationSettingsPutRequest from a dict
api_v1_users_me_notification_settings_put_request_form_dict = api_v1_users_me_notification_settings_put_request.from_dict(api_v1_users_me_notification_settings_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



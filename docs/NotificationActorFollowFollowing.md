# NotificationActorFollowFollowing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**host** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.notification_actor_follow_following import NotificationActorFollowFollowing

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationActorFollowFollowing from a JSON string
notification_actor_follow_following_instance = NotificationActorFollowFollowing.from_json(json)
# print the JSON string representation of the object
print NotificationActorFollowFollowing.to_json()

# convert the object into a dict
notification_actor_follow_following_dict = notification_actor_follow_following_instance.to_dict()
# create an instance of NotificationActorFollowFollowing from a dict
notification_actor_follow_following_form_dict = notification_actor_follow_following.from_dict(notification_actor_follow_following_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



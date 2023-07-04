# NotificationActorFollow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**follower** | [**ActorInfo**](ActorInfo.md) |  | [optional] 
**state** | **str** |  | [optional] 
**following** | [**NotificationActorFollowFollowing**](NotificationActorFollowFollowing.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.notification_actor_follow import NotificationActorFollow

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationActorFollow from a JSON string
notification_actor_follow_instance = NotificationActorFollow.from_json(json)
# print the JSON string representation of the object
print NotificationActorFollow.to_json()

# convert the object into a dict
notification_actor_follow_dict = notification_actor_follow_instance.to_dict()
# create an instance of NotificationActorFollow from a dict
notification_actor_follow_form_dict = notification_actor_follow.from_dict(notification_actor_follow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



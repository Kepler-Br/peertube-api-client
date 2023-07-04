# NotificationComment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**thread_id** | **int** |  | [optional] 
**video** | [**VideoInfo**](VideoInfo.md) |  | [optional] 
**account** | [**ActorInfo**](ActorInfo.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.notification_comment import NotificationComment

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationComment from a JSON string
notification_comment_instance = NotificationComment.from_json(json)
# print the JSON string representation of the object
print NotificationComment.to_json()

# convert the object into a dict
notification_comment_dict = notification_comment_instance.to_dict()
# create an instance of NotificationComment from a dict
notification_comment_form_dict = notification_comment.from_dict(notification_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



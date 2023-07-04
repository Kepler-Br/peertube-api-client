# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**Account**](Account.md) |  | [optional] 
**auto_play_next_video** | **bool** | Automatically start playing the upcoming video after the currently playing video | [optional] 
**auto_play_next_video_playlist** | **bool** | Automatically start playing the video on the playlist after the currently playing video | [optional] 
**auto_play_video** | **bool** | Automatically start playing the video on the watch page | [optional] 
**blocked** | **bool** |  | [optional] 
**blocked_reason** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**email** | **str** | The user email | [optional] 
**email_verified** | **bool** | Has the user confirmed their email address? | [optional] 
**id** | **int** |  | [optional] [readonly] 
**plugin_auth** | **str** | Auth plugin to use to authenticate the user | [optional] 
**last_login_date** | **datetime** |  | [optional] 
**no_instance_config_warning_modal** | **bool** |  | [optional] 
**no_account_setup_warning_modal** | **bool** |  | [optional] 
**no_welcome_modal** | **bool** |  | [optional] 
**nsfw_policy** | [**NSFWPolicy**](NSFWPolicy.md) |  | [optional] 
**role** | [**UserRole**](UserRole.md) |  | [optional] 
**theme** | **str** | Theme enabled by this user | [optional] 
**username** | **str** | immutable name of the user, used to find or mention its actor | [optional] 
**video_channels** | [**List[VideoChannel]**](VideoChannel.md) |  | [optional] 
**video_quota** | **int** | The user video quota in bytes | [optional] 
**video_quota_daily** | **int** | The user daily video quota in bytes | [optional] 
**p2p_enabled** | **bool** | Enable P2P in the player | [optional] 

## Example

```python
from peertube_api_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



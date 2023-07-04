# GetUser200Response


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
**videos_count** | **int** | Count of videos published | [optional] 
**abuses_count** | **int** | Count of reports/abuses of which the user is a target | [optional] 
**abuses_accepted_count** | **int** | Count of reports/abuses created by the user and accepted/acted upon by the moderation team | [optional] 
**abuses_created_count** | **int** | Count of reports/abuses created by the user | [optional] 
**video_comments_count** | **int** | Count of comments published | [optional] 

## Example

```python
from peertube_api_client.models.get_user200_response import GetUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUser200Response from a JSON string
get_user200_response_instance = GetUser200Response.from_json(json)
# print the JSON string representation of the object
print GetUser200Response.to_json()

# convert the object into a dict
get_user200_response_dict = get_user200_response_instance.to_dict()
# create an instance of GetUser200Response from a dict
get_user200_response_form_dict = get_user200_response.from_dict(get_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



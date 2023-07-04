# UpdateUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**Email**](Email.md) |  | [optional] 
**email_verified** | **bool** | Set the email as verified | [optional] 
**video_quota** | **int** | The updated video quota of the user in bytes | [optional] 
**video_quota_daily** | **int** | The updated daily video quota of the user in bytes | [optional] 
**plugin_auth** | **str** | The auth plugin to use to authenticate the user | [optional] 
**role** | [**UserRole**](UserRole.md) |  | [optional] 
**admin_flags** | [**UserAdminFlags**](UserAdminFlags.md) |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.update_user import UpdateUser

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUser from a JSON string
update_user_instance = UpdateUser.from_json(json)
# print the JSON string representation of the object
print UpdateUser.to_json()

# convert the object into a dict
update_user_dict = update_user_instance.to_dict()
# create an instance of UpdateUser from a dict
update_user_form_dict = update_user.from_dict(update_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



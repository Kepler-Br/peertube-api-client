# AddUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | immutable name of the user, used to find or mention its actor | 
**password** | **str** |  | 
**email** | **str** | The user email | 
**video_quota** | **int** | The user video quota in bytes | [optional] 
**video_quota_daily** | **int** | The user daily video quota in bytes | [optional] 
**channel_name** | **str** | immutable name of the channel, used to interact with its actor | [optional] 
**role** | **int** | TODO: SHOULD BE A REF TO #/components/schemas/UserRole, BUT DUE TO openapi-generator BUG I INLINED IT. The user role (Admin &#x3D; &#x60;0&#x60;, Moderator &#x3D; &#x60;1&#x60;, User &#x3D; &#x60;2&#x60;) | 
**admin_flags** | [**UserAdminFlags**](UserAdminFlags.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.add_user import AddUser

# TODO update the JSON string below
json = "{}"
# create an instance of AddUser from a JSON string
add_user_instance = AddUser.from_json(json)
# print the JSON string representation of the object
print AddUser.to_json()

# convert the object into a dict
add_user_dict = add_user_instance.to_dict()
# create an instance of AddUser from a dict
add_user_form_dict = add_user.from_dict(add_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ServerConfigCustomUser

Settings that apply to new users, if registration is enabled

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_quota** | **int** |  | [optional] 
**video_quota_daily** | **int** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_custom_user import ServerConfigCustomUser

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigCustomUser from a JSON string
server_config_custom_user_instance = ServerConfigCustomUser.from_json(json)
# print the JSON string representation of the object
print ServerConfigCustomUser.to_json()

# convert the object into a dict
server_config_custom_user_dict = server_config_custom_user_instance.to_dict()
# create an instance of ServerConfigCustomUser from a dict
server_config_custom_user_form_dict = server_config_custom_user.from_dict(server_config_custom_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



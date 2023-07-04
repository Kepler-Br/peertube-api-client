# ServerConfigUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_quota** | **int** |  | [optional] 
**video_quota_daily** | **int** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_user import ServerConfigUser

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigUser from a JSON string
server_config_user_instance = ServerConfigUser.from_json(json)
# print the JSON string representation of the object
print ServerConfigUser.to_json()

# convert the object into a dict
server_config_user_dict = server_config_user_instance.to_dict()
# create an instance of ServerConfigUser from a dict
server_config_user_form_dict = server_config_user.from_dict(server_config_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



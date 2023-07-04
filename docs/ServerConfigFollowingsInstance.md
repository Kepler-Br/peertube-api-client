# ServerConfigFollowingsInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_follow_index** | [**ServerConfigFollowingsInstanceAutoFollowIndex**](ServerConfigFollowingsInstanceAutoFollowIndex.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_followings_instance import ServerConfigFollowingsInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigFollowingsInstance from a JSON string
server_config_followings_instance_instance = ServerConfigFollowingsInstance.from_json(json)
# print the JSON string representation of the object
print ServerConfigFollowingsInstance.to_json()

# convert the object into a dict
server_config_followings_instance_dict = server_config_followings_instance_instance.to_dict()
# create an instance of ServerConfigFollowingsInstance from a dict
server_config_followings_instance_form_dict = server_config_followings_instance.from_dict(server_config_followings_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ServerConfigFollowings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**ServerConfigFollowingsInstance**](ServerConfigFollowingsInstance.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_followings import ServerConfigFollowings

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigFollowings from a JSON string
server_config_followings_instance = ServerConfigFollowings.from_json(json)
# print the JSON string representation of the object
print ServerConfigFollowings.to_json()

# convert the object into a dict
server_config_followings_dict = server_config_followings_instance.to_dict()
# create an instance of ServerConfigFollowings from a dict
server_config_followings_form_dict = server_config_followings.from_dict(server_config_followings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



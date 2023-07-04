# ServerConfigCustomFollowers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**ServerConfigCustomFollowersInstance**](ServerConfigCustomFollowersInstance.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_custom_followers import ServerConfigCustomFollowers

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigCustomFollowers from a JSON string
server_config_custom_followers_instance = ServerConfigCustomFollowers.from_json(json)
# print the JSON string representation of the object
print ServerConfigCustomFollowers.to_json()

# convert the object into a dict
server_config_custom_followers_dict = server_config_custom_followers_instance.to_dict()
# create an instance of ServerConfigCustomFollowers from a dict
server_config_custom_followers_form_dict = server_config_custom_followers.from_dict(server_config_custom_followers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ServerConfigCustomFollowersInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**manual_approval** | **bool** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_custom_followers_instance import ServerConfigCustomFollowersInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigCustomFollowersInstance from a JSON string
server_config_custom_followers_instance_instance = ServerConfigCustomFollowersInstance.from_json(json)
# print the JSON string representation of the object
print ServerConfigCustomFollowersInstance.to_json()

# convert the object into a dict
server_config_custom_followers_instance_dict = server_config_custom_followers_instance_instance.to_dict()
# create an instance of ServerConfigCustomFollowersInstance from a dict
server_config_custom_followers_instance_form_dict = server_config_custom_followers_instance.from_dict(server_config_custom_followers_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



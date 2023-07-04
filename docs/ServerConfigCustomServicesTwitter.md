# ServerConfigCustomServicesTwitter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**whitelisted** | **bool** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_custom_services_twitter import ServerConfigCustomServicesTwitter

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigCustomServicesTwitter from a JSON string
server_config_custom_services_twitter_instance = ServerConfigCustomServicesTwitter.from_json(json)
# print the JSON string representation of the object
print ServerConfigCustomServicesTwitter.to_json()

# convert the object into a dict
server_config_custom_services_twitter_dict = server_config_custom_services_twitter_instance.to_dict()
# create an instance of ServerConfigCustomServicesTwitter from a dict
server_config_custom_services_twitter_form_dict = server_config_custom_services_twitter.from_dict(server_config_custom_services_twitter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



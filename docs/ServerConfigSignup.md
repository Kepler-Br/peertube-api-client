# ServerConfigSignup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **bool** |  | [optional] 
**allowed_for_current_ip** | **bool** |  | [optional] 
**requires_email_verification** | **bool** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_signup import ServerConfigSignup

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigSignup from a JSON string
server_config_signup_instance = ServerConfigSignup.from_json(json)
# print the JSON string representation of the object
print ServerConfigSignup.to_json()

# convert the object into a dict
server_config_signup_dict = server_config_signup_instance.to_dict()
# create an instance of ServerConfigSignup from a dict
server_config_signup_form_dict = server_config_signup.from_dict(server_config_signup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



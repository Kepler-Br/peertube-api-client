# ServerConfigEmail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_email import ServerConfigEmail

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigEmail from a JSON string
server_config_email_instance = ServerConfigEmail.from_json(json)
# print the JSON string representation of the object
print ServerConfigEmail.to_json()

# convert the object into a dict
server_config_email_dict = server_config_email_instance.to_dict()
# create an instance of ServerConfigEmail from a dict
server_config_email_form_dict = server_config_email.from_dict(server_config_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



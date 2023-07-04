# OAuthClient


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.o_auth_client import OAuthClient

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthClient from a JSON string
o_auth_client_instance = OAuthClient.from_json(json)
# print the JSON string representation of the object
print OAuthClient.to_json()

# convert the object into a dict
o_auth_client_dict = o_auth_client_instance.to_dict()
# create an instance of OAuthClient from a dict
o_auth_client_form_dict = o_auth_client.from_dict(o_auth_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



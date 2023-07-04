# GetOAuthToken200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_type** | **str** |  | [optional] 
**access_token** | **str** | valid for 1 day | [optional] 
**refresh_token** | **str** | valid for 2 weeks | [optional] 
**expires_in** | **int** |  | [optional] 
**refresh_token_expires_in** | **int** |  | [optional] 

## Example

```python
from peertube_api_client.models.get_o_auth_token200_response import GetOAuthToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOAuthToken200Response from a JSON string
get_o_auth_token200_response_instance = GetOAuthToken200Response.from_json(json)
# print the JSON string representation of the object
print GetOAuthToken200Response.to_json()

# convert the object into a dict
get_o_auth_token200_response_dict = get_o_auth_token200_response_instance.to_dict()
# create an instance of GetOAuthToken200Response from a dict
get_o_auth_token200_response_form_dict = get_o_auth_token200_response.from_dict(get_o_auth_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



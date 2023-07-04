# VerifyUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_string** | **str** |  | 
**is_pending_email** | **bool** |  | [optional] 

## Example

```python
from peertube_api_client.models.verify_user_request import VerifyUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyUserRequest from a JSON string
verify_user_request_instance = VerifyUserRequest.from_json(json)
# print the JSON string representation of the object
print VerifyUserRequest.to_json()

# convert the object into a dict
verify_user_request_dict = verify_user_request_instance.to_dict()
# create an instance of VerifyUserRequest from a dict
verify_user_request_form_dict = verify_user_request.from_dict(verify_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



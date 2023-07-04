# ResendEmailToVerifyUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email | 

## Example

```python
from peertube_api_client.models.resend_email_to_verify_user_request import ResendEmailToVerifyUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResendEmailToVerifyUserRequest from a JSON string
resend_email_to_verify_user_request_instance = ResendEmailToVerifyUserRequest.from_json(json)
# print the JSON string representation of the object
print ResendEmailToVerifyUserRequest.to_json()

# convert the object into a dict
resend_email_to_verify_user_request_dict = resend_email_to_verify_user_request_instance.to_dict()
# create an instance of ResendEmailToVerifyUserRequest from a dict
resend_email_to_verify_user_request_form_dict = resend_email_to_verify_user_request.from_dict(resend_email_to_verify_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



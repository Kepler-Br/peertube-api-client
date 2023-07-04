# ResendEmailToVerifyRegistrationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Registration email | 

## Example

```python
from peertube_api_client.models.resend_email_to_verify_registration_request import ResendEmailToVerifyRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResendEmailToVerifyRegistrationRequest from a JSON string
resend_email_to_verify_registration_request_instance = ResendEmailToVerifyRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print ResendEmailToVerifyRegistrationRequest.to_json()

# convert the object into a dict
resend_email_to_verify_registration_request_dict = resend_email_to_verify_registration_request_instance.to_dict()
# create an instance of ResendEmailToVerifyRegistrationRequest from a dict
resend_email_to_verify_registration_request_form_dict = resend_email_to_verify_registration_request.from_dict(resend_email_to_verify_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



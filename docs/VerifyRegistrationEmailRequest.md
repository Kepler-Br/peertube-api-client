# VerifyRegistrationEmailRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_string** | **str** |  | 

## Example

```python
from peertube_api_client.models.verify_registration_email_request import VerifyRegistrationEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyRegistrationEmailRequest from a JSON string
verify_registration_email_request_instance = VerifyRegistrationEmailRequest.from_json(json)
# print the JSON string representation of the object
print VerifyRegistrationEmailRequest.to_json()

# convert the object into a dict
verify_registration_email_request_dict = verify_registration_email_request_instance.to_dict()
# create an instance of VerifyRegistrationEmailRequest from a dict
verify_registration_email_request_form_dict = verify_registration_email_request.from_dict(verify_registration_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



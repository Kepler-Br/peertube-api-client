# RequestTwoFactorResponseOtpRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_token** | **str** | The token to send to confirm this request | [optional] 
**secret** | **str** | The OTP secret | [optional] 
**uri** | **str** | The OTP URI | [optional] 

## Example

```python
from peertube_api_client.models.request_two_factor_response_otp_request import RequestTwoFactorResponseOtpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestTwoFactorResponseOtpRequest from a JSON string
request_two_factor_response_otp_request_instance = RequestTwoFactorResponseOtpRequest.from_json(json)
# print the JSON string representation of the object
print RequestTwoFactorResponseOtpRequest.to_json()

# convert the object into a dict
request_two_factor_response_otp_request_dict = request_two_factor_response_otp_request_instance.to_dict()
# create an instance of RequestTwoFactorResponseOtpRequest from a dict
request_two_factor_response_otp_request_form_dict = request_two_factor_response_otp_request.from_dict(request_two_factor_response_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



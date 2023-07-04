# RequestTwoFactorResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp_request** | [**RequestTwoFactorResponseOtpRequest**](RequestTwoFactorResponseOtpRequest.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.request_two_factor_response import RequestTwoFactorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestTwoFactorResponse from a JSON string
request_two_factor_response_instance = RequestTwoFactorResponse.from_json(json)
# print the JSON string representation of the object
print RequestTwoFactorResponse.to_json()

# convert the object into a dict
request_two_factor_response_dict = request_two_factor_response_instance.to_dict()
# create an instance of RequestTwoFactorResponse from a dict
request_two_factor_response_form_dict = request_two_factor_response.from_dict(request_two_factor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



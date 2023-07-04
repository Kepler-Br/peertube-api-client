# RequestTwoFactorRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** | Password of the currently authenticated user | [optional] 

## Example

```python
from peertube_api_client.models.request_two_factor_request import RequestTwoFactorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestTwoFactorRequest from a JSON string
request_two_factor_request_instance = RequestTwoFactorRequest.from_json(json)
# print the JSON string representation of the object
print RequestTwoFactorRequest.to_json()

# convert the object into a dict
request_two_factor_request_dict = request_two_factor_request_instance.to_dict()
# create an instance of RequestTwoFactorRequest from a dict
request_two_factor_request_form_dict = request_two_factor_request.from_dict(request_two_factor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



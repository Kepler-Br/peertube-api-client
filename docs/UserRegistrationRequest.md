# UserRegistrationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | immutable name of the user, used to find or mention its actor | 
**password** | **str** |  | 
**email** | **str** | email of the user, used for login or service communications | 
**display_name** | **str** | editable name of the user, displayed in its representations | [optional] 
**channel** | [**RegisterUserChannel**](RegisterUserChannel.md) |  | [optional] 
**registration_reason** | **str** | reason for the user to register on the instance | 

## Example

```python
from peertube_api_client.models.user_registration_request import UserRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserRegistrationRequest from a JSON string
user_registration_request_instance = UserRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print UserRegistrationRequest.to_json()

# convert the object into a dict
user_registration_request_dict = user_registration_request_instance.to_dict()
# create an instance of UserRegistrationRequest from a dict
user_registration_request_form_dict = user_registration_request.from_dict(user_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



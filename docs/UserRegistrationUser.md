# UserRegistrationUser

If the registration has been accepted, this is a partial user object created by the registration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 

## Example

```python
from peertube_api_client.models.user_registration_user import UserRegistrationUser

# TODO update the JSON string below
json = "{}"
# create an instance of UserRegistrationUser from a JSON string
user_registration_user_instance = UserRegistrationUser.from_json(json)
# print the JSON string representation of the object
print UserRegistrationUser.to_json()

# convert the object into a dict
user_registration_user_dict = user_registration_user_instance.to_dict()
# create an instance of UserRegistrationUser from a dict
user_registration_user_form_dict = user_registration_user.from_dict(user_registration_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UserRegistration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**state** | [**UserRegistrationState**](UserRegistrationState.md) |  | [optional] 
**registration_reason** | **str** |  | [optional] 
**moderation_response** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**email_verified** | **bool** |  | [optional] 
**account_display_name** | **str** |  | [optional] 
**channel_handle** | **str** |  | [optional] 
**channel_display_name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user** | [**UserRegistrationUser**](UserRegistrationUser.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.user_registration import UserRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of UserRegistration from a JSON string
user_registration_instance = UserRegistration.from_json(json)
# print the JSON string representation of the object
print UserRegistration.to_json()

# convert the object into a dict
user_registration_dict = user_registration_instance.to_dict()
# create an instance of UserRegistration from a dict
user_registration_form_dict = user_registration.from_dict(user_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



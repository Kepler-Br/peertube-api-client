# UserRegistrationState


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The registration state (Pending &#x3D; &#x60;1&#x60;, Rejected &#x3D; &#x60;2&#x60;, Accepted &#x3D; &#x60;3&#x60;) | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.user_registration_state import UserRegistrationState

# TODO update the JSON string below
json = "{}"
# create an instance of UserRegistrationState from a JSON string
user_registration_state_instance = UserRegistrationState.from_json(json)
# print the JSON string representation of the object
print UserRegistrationState.to_json()

# convert the object into a dict
user_registration_state_dict = user_registration_state_instance.to_dict()
# create an instance of UserRegistrationState from a dict
user_registration_state_form_dict = user_registration_state.from_dict(user_registration_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



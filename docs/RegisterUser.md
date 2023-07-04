# RegisterUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | immutable name of the user, used to find or mention its actor | 
**password** | **str** |  | 
**email** | **str** | email of the user, used for login or service communications | 
**display_name** | **str** | editable name of the user, displayed in its representations | [optional] 
**channel** | [**RegisterUserChannel**](RegisterUserChannel.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.register_user import RegisterUser

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterUser from a JSON string
register_user_instance = RegisterUser.from_json(json)
# print the JSON string representation of the object
print RegisterUser.to_json()

# convert the object into a dict
register_user_dict = register_user_instance.to_dict()
# create an instance of RegisterUser from a dict
register_user_form_dict = register_user.from_dict(register_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



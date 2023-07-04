# AddUserResponseUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**account** | [**ApiV1AbusesPost200ResponseAbuse**](ApiV1AbusesPost200ResponseAbuse.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.add_user_response_user import AddUserResponseUser

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserResponseUser from a JSON string
add_user_response_user_instance = AddUserResponseUser.from_json(json)
# print the JSON string representation of the object
print AddUserResponseUser.to_json()

# convert the object into a dict
add_user_response_user_dict = add_user_response_user_instance.to_dict()
# create an instance of AddUserResponseUser from a dict
add_user_response_user_form_dict = add_user_response_user.from_dict(add_user_response_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RegisterUserChannel

channel base information used to create the first channel of the user

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | immutable name of the channel, used to interact with its actor | [optional] 
**display_name** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.register_user_channel import RegisterUserChannel

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterUserChannel from a JSON string
register_user_channel_instance = RegisterUserChannel.from_json(json)
# print the JSON string representation of the object
print RegisterUserChannel.to_json()

# convert the object into a dict
register_user_channel_dict = register_user_channel_instance.to_dict()
# create an instance of RegisterUserChannel from a dict
register_user_channel_form_dict = register_user_channel.from_dict(register_user_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



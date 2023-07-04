# ApiV1UsersMeAvatarPickPost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatars** | [**List[ActorImage]**](ActorImage.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_users_me_avatar_pick_post200_response import ApiV1UsersMeAvatarPickPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1UsersMeAvatarPickPost200Response from a JSON string
api_v1_users_me_avatar_pick_post200_response_instance = ApiV1UsersMeAvatarPickPost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1UsersMeAvatarPickPost200Response.to_json()

# convert the object into a dict
api_v1_users_me_avatar_pick_post200_response_dict = api_v1_users_me_avatar_pick_post200_response_instance.to_dict()
# create an instance of ApiV1UsersMeAvatarPickPost200Response from a dict
api_v1_users_me_avatar_pick_post200_response_form_dict = api_v1_users_me_avatar_pick_post200_response.from_dict(api_v1_users_me_avatar_pick_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



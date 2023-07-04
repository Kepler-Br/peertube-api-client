# ApiV1UsersMeSubscriptionsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | uri of the video channels to subscribe to | 

## Example

```python
from peertube_api_client.models.api_v1_users_me_subscriptions_post_request import ApiV1UsersMeSubscriptionsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1UsersMeSubscriptionsPostRequest from a JSON string
api_v1_users_me_subscriptions_post_request_instance = ApiV1UsersMeSubscriptionsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1UsersMeSubscriptionsPostRequest.to_json()

# convert the object into a dict
api_v1_users_me_subscriptions_post_request_dict = api_v1_users_me_subscriptions_post_request_instance.to_dict()
# create an instance of ApiV1UsersMeSubscriptionsPostRequest from a dict
api_v1_users_me_subscriptions_post_request_form_dict = api_v1_users_me_subscriptions_post_request.from_dict(api_v1_users_me_subscriptions_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



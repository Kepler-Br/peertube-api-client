# UserRegistrationAcceptOrReject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**moderation_response** | **str** | Moderation response to send to the user | 
**prevent_email_delivery** | **bool** | Set it to true if you don&#39;t want PeerTube to send an email to the user | [optional] 

## Example

```python
from peertube_api_client.models.user_registration_accept_or_reject import UserRegistrationAcceptOrReject

# TODO update the JSON string below
json = "{}"
# create an instance of UserRegistrationAcceptOrReject from a JSON string
user_registration_accept_or_reject_instance = UserRegistrationAcceptOrReject.from_json(json)
# print the JSON string representation of the object
print UserRegistrationAcceptOrReject.to_json()

# convert the object into a dict
user_registration_accept_or_reject_dict = user_registration_accept_or_reject_instance.to_dict()
# create an instance of UserRegistrationAcceptOrReject from a dict
user_registration_accept_or_reject_form_dict = user_registration_accept_or_reject.from_dict(user_registration_accept_or_reject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



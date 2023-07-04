# ApiV1UsersMeVideoQuotaUsedGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_quota_used** | **float** | The user video quota used so far in bytes | [optional] 
**video_quota_used_daily** | **float** | The user video quota used today in bytes | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_users_me_video_quota_used_get200_response import ApiV1UsersMeVideoQuotaUsedGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1UsersMeVideoQuotaUsedGet200Response from a JSON string
api_v1_users_me_video_quota_used_get200_response_instance = ApiV1UsersMeVideoQuotaUsedGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1UsersMeVideoQuotaUsedGet200Response.to_json()

# convert the object into a dict
api_v1_users_me_video_quota_used_get200_response_dict = api_v1_users_me_video_quota_used_get200_response_instance.to_dict()
# create an instance of ApiV1UsersMeVideoQuotaUsedGet200Response from a dict
api_v1_users_me_video_quota_used_get200_response_form_dict = api_v1_users_me_video_quota_used_get200_response.from_dict(api_v1_users_me_video_quota_used_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



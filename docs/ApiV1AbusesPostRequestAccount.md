# ApiV1AbusesPostRequestAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Account id to report | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_abuses_post_request_account import ApiV1AbusesPostRequestAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AbusesPostRequestAccount from a JSON string
api_v1_abuses_post_request_account_instance = ApiV1AbusesPostRequestAccount.from_json(json)
# print the JSON string representation of the object
print ApiV1AbusesPostRequestAccount.to_json()

# convert the object into a dict
api_v1_abuses_post_request_account_dict = api_v1_abuses_post_request_account_instance.to_dict()
# create an instance of ApiV1AbusesPostRequestAccount from a dict
api_v1_abuses_post_request_account_form_dict = api_v1_abuses_post_request_account.from_dict(api_v1_abuses_post_request_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



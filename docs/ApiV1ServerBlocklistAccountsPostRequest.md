# ApiV1ServerBlocklistAccountsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** | account to block, in the form &#x60;username@domain&#x60; | 

## Example

```python
from peertube_api_client.models.api_v1_server_blocklist_accounts_post_request import ApiV1ServerBlocklistAccountsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ServerBlocklistAccountsPostRequest from a JSON string
api_v1_server_blocklist_accounts_post_request_instance = ApiV1ServerBlocklistAccountsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1ServerBlocklistAccountsPostRequest.to_json()

# convert the object into a dict
api_v1_server_blocklist_accounts_post_request_dict = api_v1_server_blocklist_accounts_post_request_instance.to_dict()
# create an instance of ApiV1ServerBlocklistAccountsPostRequest from a dict
api_v1_server_blocklist_accounts_post_request_form_dict = api_v1_server_blocklist_accounts_post_request.from_dict(api_v1_server_blocklist_accounts_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



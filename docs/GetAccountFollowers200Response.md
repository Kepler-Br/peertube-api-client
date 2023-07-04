# GetAccountFollowers200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**data** | [**List[Follow]**](Follow.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.get_account_followers200_response import GetAccountFollowers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountFollowers200Response from a JSON string
get_account_followers200_response_instance = GetAccountFollowers200Response.from_json(json)
# print the JSON string representation of the object
print GetAccountFollowers200Response.to_json()

# convert the object into a dict
get_account_followers200_response_dict = get_account_followers200_response_instance.to_dict()
# create an instance of GetAccountFollowers200Response from a dict
get_account_followers200_response_form_dict = get_account_followers200_response.from_dict(get_account_followers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



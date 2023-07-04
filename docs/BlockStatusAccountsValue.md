# BlockStatusAccountsValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked_by_server** | **bool** |  | [optional] 
**blocked_by_user** | **bool** |  | [optional] 

## Example

```python
from peertube_api_client.models.block_status_accounts_value import BlockStatusAccountsValue

# TODO update the JSON string below
json = "{}"
# create an instance of BlockStatusAccountsValue from a JSON string
block_status_accounts_value_instance = BlockStatusAccountsValue.from_json(json)
# print the JSON string representation of the object
print BlockStatusAccountsValue.to_json()

# convert the object into a dict
block_status_accounts_value_dict = block_status_accounts_value_instance.to_dict()
# create an instance of BlockStatusAccountsValue from a dict
block_status_accounts_value_form_dict = block_status_accounts_value.from_dict(block_status_accounts_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



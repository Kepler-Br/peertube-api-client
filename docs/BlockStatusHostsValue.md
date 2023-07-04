# BlockStatusHostsValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked_by_server** | **bool** |  | [optional] 
**blocked_by_user** | **bool** |  | [optional] 

## Example

```python
from peertube_api_client.models.block_status_hosts_value import BlockStatusHostsValue

# TODO update the JSON string below
json = "{}"
# create an instance of BlockStatusHostsValue from a JSON string
block_status_hosts_value_instance = BlockStatusHostsValue.from_json(json)
# print the JSON string representation of the object
print BlockStatusHostsValue.to_json()

# convert the object into a dict
block_status_hosts_value_dict = block_status_hosts_value_instance.to_dict()
# create an instance of BlockStatusHostsValue from a dict
block_status_hosts_value_form_dict = block_status_hosts_value.from_dict(block_status_hosts_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



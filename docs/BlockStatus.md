# BlockStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**Dict[str, BlockStatusAccountsValue]**](BlockStatusAccountsValue.md) |  | [optional] 
**hosts** | [**Dict[str, BlockStatusHostsValue]**](BlockStatusHostsValue.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.block_status import BlockStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BlockStatus from a JSON string
block_status_instance = BlockStatus.from_json(json)
# print the JSON string representation of the object
print BlockStatus.to_json()

# convert the object into a dict
block_status_dict = block_status_instance.to_dict()
# create an instance of BlockStatus from a dict
block_status_form_dict = block_status.from_dict(block_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



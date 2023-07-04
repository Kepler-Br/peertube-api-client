# AbuseStateConstant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**AbuseStateSet**](AbuseStateSet.md) |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.abuse_state_constant import AbuseStateConstant

# TODO update the JSON string below
json = "{}"
# create an instance of AbuseStateConstant from a JSON string
abuse_state_constant_instance = AbuseStateConstant.from_json(json)
# print the JSON string representation of the object
print AbuseStateConstant.to_json()

# convert the object into a dict
abuse_state_constant_dict = abuse_state_constant_instance.to_dict()
# create an instance of AbuseStateConstant from a dict
abuse_state_constant_form_dict = abuse_state_constant.from_dict(abuse_state_constant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AbuseMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**by_moderator** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**account** | [**AccountSummary**](AccountSummary.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.abuse_message import AbuseMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AbuseMessage from a JSON string
abuse_message_instance = AbuseMessage.from_json(json)
# print the JSON string representation of the object
print AbuseMessage.to_json()

# convert the object into a dict
abuse_message_dict = abuse_message_instance.to_dict()
# create an instance of AbuseMessage from a dict
abuse_message_form_dict = abuse_message.from_dict(abuse_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



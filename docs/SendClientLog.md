# SendClientLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**url** | **str** | URL of the current user page | 
**level** | **str** |  | 
**stack_trace** | **str** | Stack trace of the error if there is one | [optional] 
**user_agent** | **str** | User agent of the web browser that sends the message | [optional] 
**meta** | **str** | Additional information regarding this log | [optional] 

## Example

```python
from peertube_api_client.models.send_client_log import SendClientLog

# TODO update the JSON string below
json = "{}"
# create an instance of SendClientLog from a JSON string
send_client_log_instance = SendClientLog.from_json(json)
# print the JSON string representation of the object
print SendClientLog.to_json()

# convert the object into a dict
send_client_log_dict = send_client_log_instance.to_dict()
# create an instance of SendClientLog from a dict
send_client_log_form_dict = send_client_log.from_dict(send_client_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



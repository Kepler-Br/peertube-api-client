# ApiV1ServerRedundancyHostPutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redundancy_allowed** | **bool** | allow mirroring of the host&#39;s local videos | 

## Example

```python
from peertube_api_client.models.api_v1_server_redundancy_host_put_request import ApiV1ServerRedundancyHostPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ServerRedundancyHostPutRequest from a JSON string
api_v1_server_redundancy_host_put_request_instance = ApiV1ServerRedundancyHostPutRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1ServerRedundancyHostPutRequest.to_json()

# convert the object into a dict
api_v1_server_redundancy_host_put_request_dict = api_v1_server_redundancy_host_put_request_instance.to_dict()
# create an instance of ApiV1ServerRedundancyHostPutRequest from a dict
api_v1_server_redundancy_host_put_request_form_dict = api_v1_server_redundancy_host_put_request.from_dict(api_v1_server_redundancy_host_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



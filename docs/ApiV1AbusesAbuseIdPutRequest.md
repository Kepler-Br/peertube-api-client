# ApiV1AbusesAbuseIdPutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**AbuseStateSet**](AbuseStateSet.md) |  | [optional] 
**moderation_comment** | **str** | Update the report comment visible only to the moderation team | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_abuses_abuse_id_put_request import ApiV1AbusesAbuseIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AbusesAbuseIdPutRequest from a JSON string
api_v1_abuses_abuse_id_put_request_instance = ApiV1AbusesAbuseIdPutRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AbusesAbuseIdPutRequest.to_json()

# convert the object into a dict
api_v1_abuses_abuse_id_put_request_dict = api_v1_abuses_abuse_id_put_request_instance.to_dict()
# create an instance of ApiV1AbusesAbuseIdPutRequest from a dict
api_v1_abuses_abuse_id_put_request_form_dict = api_v1_abuses_abuse_id_put_request.from_dict(api_v1_abuses_abuse_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



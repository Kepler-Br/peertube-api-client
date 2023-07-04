# ApiV1AbusesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Reason why the user reports this video | 
**predefined_reasons** | **List[str]** | Reason categories that help triage reports | [optional] 
**video** | [**ApiV1AbusesPostRequestVideo**](ApiV1AbusesPostRequestVideo.md) |  | [optional] 
**comment** | [**ApiV1AbusesPostRequestComment**](ApiV1AbusesPostRequestComment.md) |  | [optional] 
**account** | [**ApiV1AbusesPostRequestAccount**](ApiV1AbusesPostRequestAccount.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_abuses_post_request import ApiV1AbusesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AbusesPostRequest from a JSON string
api_v1_abuses_post_request_instance = ApiV1AbusesPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AbusesPostRequest.to_json()

# convert the object into a dict
api_v1_abuses_post_request_dict = api_v1_abuses_post_request_instance.to_dict()
# create an instance of ApiV1AbusesPostRequest from a dict
api_v1_abuses_post_request_form_dict = api_v1_abuses_post_request.from_dict(api_v1_abuses_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1RunnersJobsRequestPost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_jobs** | [**List[ApiV1RunnersJobsRequestPost200ResponseAvailableJobsInner]**](ApiV1RunnersJobsRequestPost200ResponseAvailableJobsInner.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_runners_jobs_request_post200_response import ApiV1RunnersJobsRequestPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1RunnersJobsRequestPost200Response from a JSON string
api_v1_runners_jobs_request_post200_response_instance = ApiV1RunnersJobsRequestPost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1RunnersJobsRequestPost200Response.to_json()

# convert the object into a dict
api_v1_runners_jobs_request_post200_response_dict = api_v1_runners_jobs_request_post200_response_instance.to_dict()
# create an instance of ApiV1RunnersJobsRequestPost200Response from a dict
api_v1_runners_jobs_request_post200_response_form_dict = api_v1_runners_jobs_request_post200_response.from_dict(api_v1_runners_jobs_request_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



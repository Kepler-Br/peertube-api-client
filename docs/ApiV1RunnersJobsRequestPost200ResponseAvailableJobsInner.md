# ApiV1RunnersJobsRequestPost200ResponseAvailableJobsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**type** | [**RunnerJobType**](RunnerJobType.md) |  | [optional] 
**payload** | [**RunnerJobPayload**](RunnerJobPayload.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_runners_jobs_request_post200_response_available_jobs_inner import ApiV1RunnersJobsRequestPost200ResponseAvailableJobsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1RunnersJobsRequestPost200ResponseAvailableJobsInner from a JSON string
api_v1_runners_jobs_request_post200_response_available_jobs_inner_instance = ApiV1RunnersJobsRequestPost200ResponseAvailableJobsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1RunnersJobsRequestPost200ResponseAvailableJobsInner.to_json()

# convert the object into a dict
api_v1_runners_jobs_request_post200_response_available_jobs_inner_dict = api_v1_runners_jobs_request_post200_response_available_jobs_inner_instance.to_dict()
# create an instance of ApiV1RunnersJobsRequestPost200ResponseAvailableJobsInner from a dict
api_v1_runners_jobs_request_post200_response_available_jobs_inner_form_dict = api_v1_runners_jobs_request_post200_response_available_jobs_inner.from_dict(api_v1_runners_jobs_request_post200_response_available_jobs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



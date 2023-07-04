# ApiV1RunnersJobsJobUUIDSuccessPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runner_token** | **str** |  | 
**job_token** | **str** |  | 
**payload** | [**ApiV1RunnersJobsJobUUIDSuccessPostRequestPayload**](ApiV1RunnersJobsJobUUIDSuccessPostRequestPayload.md) |  | 

## Example

```python
from peertube_api_client.models.api_v1_runners_jobs_job_uuid_success_post_request import ApiV1RunnersJobsJobUUIDSuccessPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1RunnersJobsJobUUIDSuccessPostRequest from a JSON string
api_v1_runners_jobs_job_uuid_success_post_request_instance = ApiV1RunnersJobsJobUUIDSuccessPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1RunnersJobsJobUUIDSuccessPostRequest.to_json()

# convert the object into a dict
api_v1_runners_jobs_job_uuid_success_post_request_dict = api_v1_runners_jobs_job_uuid_success_post_request_instance.to_dict()
# create an instance of ApiV1RunnersJobsJobUUIDSuccessPostRequest from a dict
api_v1_runners_jobs_job_uuid_success_post_request_form_dict = api_v1_runners_jobs_job_uuid_success_post_request.from_dict(api_v1_runners_jobs_job_uuid_success_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



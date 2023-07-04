# ApiV1RunnersJobsJobUUIDUpdatePostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runner_token** | **str** |  | 
**job_token** | **str** |  | 
**progress** | **int** | Update job progression percentage (optional) | [optional] 
**payload** | [**ApiV1RunnersJobsJobUUIDUpdatePostRequestPayload**](ApiV1RunnersJobsJobUUIDUpdatePostRequestPayload.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_runners_jobs_job_uuid_update_post_request import ApiV1RunnersJobsJobUUIDUpdatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1RunnersJobsJobUUIDUpdatePostRequest from a JSON string
api_v1_runners_jobs_job_uuid_update_post_request_instance = ApiV1RunnersJobsJobUUIDUpdatePostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1RunnersJobsJobUUIDUpdatePostRequest.to_json()

# convert the object into a dict
api_v1_runners_jobs_job_uuid_update_post_request_dict = api_v1_runners_jobs_job_uuid_update_post_request_instance.to_dict()
# create an instance of ApiV1RunnersJobsJobUUIDUpdatePostRequest from a dict
api_v1_runners_jobs_job_uuid_update_post_request_form_dict = api_v1_runners_jobs_job_uuid_update_post_request.from_dict(api_v1_runners_jobs_job_uuid_update_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



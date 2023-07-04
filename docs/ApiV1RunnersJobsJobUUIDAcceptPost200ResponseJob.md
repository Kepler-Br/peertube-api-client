# ApiV1RunnersJobsJobUUIDAcceptPost200ResponseJob


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**type** | [**RunnerJobType**](RunnerJobType.md) |  | [optional] 
**state** | [**RunnerJobStateConstant**](RunnerJobStateConstant.md) |  | [optional] 
**payload** | [**RunnerJobPayload**](RunnerJobPayload.md) |  | [optional] 
**failures** | **int** | Number of times a remote runner failed to process this job. After too many failures, the job in \&quot;error\&quot; state | [optional] 
**error** | **str** | Error message if the job is errored | [optional] 
**progress** | **int** | Percentage progress | [optional] 
**priority** | **int** | Job priority (less has more priority) | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**parent** | [**RunnerJobParent**](RunnerJobParent.md) |  | [optional] 
**runner** | [**RunnerJobRunner**](RunnerJobRunner.md) |  | [optional] 
**job_token** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_runners_jobs_job_uuid_accept_post200_response_job import ApiV1RunnersJobsJobUUIDAcceptPost200ResponseJob

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1RunnersJobsJobUUIDAcceptPost200ResponseJob from a JSON string
api_v1_runners_jobs_job_uuid_accept_post200_response_job_instance = ApiV1RunnersJobsJobUUIDAcceptPost200ResponseJob.from_json(json)
# print the JSON string representation of the object
print ApiV1RunnersJobsJobUUIDAcceptPost200ResponseJob.to_json()

# convert the object into a dict
api_v1_runners_jobs_job_uuid_accept_post200_response_job_dict = api_v1_runners_jobs_job_uuid_accept_post200_response_job_instance.to_dict()
# create an instance of ApiV1RunnersJobsJobUUIDAcceptPost200ResponseJob from a dict
api_v1_runners_jobs_job_uuid_accept_post200_response_job_form_dict = api_v1_runners_jobs_job_uuid_accept_post200_response_job.from_dict(api_v1_runners_jobs_job_uuid_accept_post200_response_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



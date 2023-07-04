# RunnerJobAdmin


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
**private_payload** | **object** |  | [optional] 

## Example

```python
from peertube_api_client.models.runner_job_admin import RunnerJobAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerJobAdmin from a JSON string
runner_job_admin_instance = RunnerJobAdmin.from_json(json)
# print the JSON string representation of the object
print RunnerJobAdmin.to_json()

# convert the object into a dict
runner_job_admin_dict = runner_job_admin_instance.to_dict()
# create an instance of RunnerJobAdmin from a dict
runner_job_admin_form_dict = runner_job_admin.from_dict(runner_job_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



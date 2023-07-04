# RunnerJobRunner

If job is associated to a runner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.runner_job_runner import RunnerJobRunner

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerJobRunner from a JSON string
runner_job_runner_instance = RunnerJobRunner.from_json(json)
# print the JSON string representation of the object
print RunnerJobRunner.to_json()

# convert the object into a dict
runner_job_runner_dict = runner_job_runner_instance.to_dict()
# create an instance of RunnerJobRunner from a dict
runner_job_runner_form_dict = runner_job_runner.from_dict(runner_job_runner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



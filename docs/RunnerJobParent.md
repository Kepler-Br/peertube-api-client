# RunnerJobParent

If job has a parent job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RunnerJobType**](RunnerJobType.md) |  | [optional] 
**state** | [**RunnerJobStateConstant**](RunnerJobStateConstant.md) |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.runner_job_parent import RunnerJobParent

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerJobParent from a JSON string
runner_job_parent_instance = RunnerJobParent.from_json(json)
# print the JSON string representation of the object
print RunnerJobParent.to_json()

# convert the object into a dict
runner_job_parent_dict = runner_job_parent_instance.to_dict()
# create an instance of RunnerJobParent from a dict
runner_job_parent_form_dict = runner_job_parent.from_dict(runner_job_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



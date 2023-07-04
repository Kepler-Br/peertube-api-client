# RunnerJobStateConstant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**RunnerJobState**](RunnerJobState.md) |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.runner_job_state_constant import RunnerJobStateConstant

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerJobStateConstant from a JSON string
runner_job_state_constant_instance = RunnerJobStateConstant.from_json(json)
# print the JSON string representation of the object
print RunnerJobStateConstant.to_json()

# convert the object into a dict
runner_job_state_constant_dict = runner_job_state_constant_instance.to_dict()
# create an instance of RunnerJobStateConstant from a dict
runner_job_state_constant_form_dict = runner_job_state_constant.from_dict(runner_job_state_constant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



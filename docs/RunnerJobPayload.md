# RunnerJobPayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**VODAudioMergeTranscoding1Input**](VODAudioMergeTranscoding1Input.md) |  | [optional] 
**output** | [**VODWebVideoTranscoding1Output**](VODWebVideoTranscoding1Output.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.runner_job_payload import RunnerJobPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerJobPayload from a JSON string
runner_job_payload_instance = RunnerJobPayload.from_json(json)
# print the JSON string representation of the object
print RunnerJobPayload.to_json()

# convert the object into a dict
runner_job_payload_dict = runner_job_payload_instance.to_dict()
# create an instance of RunnerJobPayload from a dict
runner_job_payload_form_dict = runner_job_payload.from_dict(runner_job_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



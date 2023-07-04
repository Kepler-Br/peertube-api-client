# Runner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**last_contact** | **datetime** |  | [optional] 

## Example

```python
from peertube_api_client.models.runner import Runner

# TODO update the JSON string below
json = "{}"
# create an instance of Runner from a JSON string
runner_instance = Runner.from_json(json)
# print the JSON string representation of the object
print Runner.to_json()

# convert the object into a dict
runner_dict = runner_instance.to_dict()
# create an instance of Runner from a dict
runner_form_dict = runner.from_dict(runner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



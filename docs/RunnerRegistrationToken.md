# RunnerRegistrationToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**registration_token** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**registered_runners_count** | **int** |  | [optional] 

## Example

```python
from peertube_api_client.models.runner_registration_token import RunnerRegistrationToken

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerRegistrationToken from a JSON string
runner_registration_token_instance = RunnerRegistrationToken.from_json(json)
# print the JSON string representation of the object
print RunnerRegistrationToken.to_json()

# convert the object into a dict
runner_registration_token_dict = runner_registration_token_instance.to_dict()
# create an instance of RunnerRegistrationToken from a dict
runner_registration_token_form_dict = runner_registration_token.from_dict(runner_registration_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



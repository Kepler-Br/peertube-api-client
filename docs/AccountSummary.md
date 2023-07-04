# AccountSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**avatars** | [**List[ActorImage]**](ActorImage.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.account_summary import AccountSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSummary from a JSON string
account_summary_instance = AccountSummary.from_json(json)
# print the JSON string representation of the object
print AccountSummary.to_json()

# convert the object into a dict
account_summary_dict = account_summary_instance.to_dict()
# create an instance of AccountSummary from a dict
account_summary_form_dict = account_summary.from_dict(account_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



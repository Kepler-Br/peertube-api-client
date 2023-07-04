# Account


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**name** | **str** | immutable name of the user, used to find or mention its actor | [optional] 
**host** | **str** | server on which the actor is resident | [optional] 
**host_redundancy_allowed** | **bool** | whether this actor&#39;s host allows redundancy of its videos | [optional] 
**following_count** | **int** | number of actors subscribed to by this actor, as seen by this instance | [optional] 
**followers_count** | **int** | number of followers of this actor, as seen by this instance | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user_id** | **int** |  | [optional] 
**display_name** | **str** | editable name of the account, displayed in its representations | [optional] 
**description** | **str** | text or bio displayed on the account&#39;s profile | [optional] 

## Example

```python
from peertube_api_client.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print Account.to_json()

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_form_dict = account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



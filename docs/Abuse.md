# Abuse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**reason** | **str** |  | [optional] 
**predefined_reasons** | **List[str]** |  | [optional] 
**reporter_account** | [**Account**](Account.md) |  | [optional] 
**state** | [**AbuseStateConstant**](AbuseStateConstant.md) |  | [optional] 
**moderation_comment** | **str** |  | [optional] 
**video** | [**VideoInfo**](VideoInfo.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from peertube_api_client.models.abuse import Abuse

# TODO update the JSON string below
json = "{}"
# create an instance of Abuse from a JSON string
abuse_instance = Abuse.from_json(json)
# print the JSON string representation of the object
print Abuse.to_json()

# convert the object into a dict
abuse_dict = abuse_instance.to_dict()
# create an instance of Abuse from a dict
abuse_form_dict = abuse.from_dict(abuse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UpdateMe


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**current_password** | **str** |  | [optional] 
**email** | [**Email**](Email.md) |  | [optional] 
**display_name** | **str** | new name of the user in its representations | [optional] 
**display_nsfw** | **str** | new NSFW display policy | [optional] 
**p2p_enabled** | **bool** | whether to enable P2P in the player or not | [optional] 
**auto_play_video** | **bool** | new preference regarding playing videos automatically | [optional] 
**auto_play_next_video** | **bool** | new preference regarding playing following videos automatically | [optional] 
**auto_play_next_video_playlist** | **bool** | new preference regarding playing following playlist videos automatically | [optional] 
**videos_history_enabled** | **bool** | whether to keep track of watched history or not | [optional] 
**video_languages** | **List[str]** | list of languages to filter videos down to | [optional] 
**theme** | **str** |  | [optional] 
**no_instance_config_warning_modal** | **bool** |  | [optional] 
**no_account_setup_warning_modal** | **bool** |  | [optional] 
**no_welcome_modal** | **bool** |  | [optional] 

## Example

```python
from peertube_api_client.models.update_me import UpdateMe

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMe from a JSON string
update_me_instance = UpdateMe.from_json(json)
# print the JSON string representation of the object
print UpdateMe.to_json()

# convert the object into a dict
update_me_dict = update_me_instance.to_dict()
# create an instance of UpdateMe from a dict
update_me_form_dict = update_me.from_dict(update_me_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



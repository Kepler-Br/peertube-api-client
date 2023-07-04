# VideoChannelListDataInner


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
**display_name** | **str** | editable name of the channel, displayed in its representations | [optional] 
**description** | **str** |  | [optional] 
**support** | **str** | text shown by default on all videos of this channel, to tell the audience how to support it | [optional] 
**is_local** | **bool** |  | [optional] [readonly] 
**banners** | [**List[ActorImage]**](ActorImage.md) |  | [optional] 
**owner_account** | [**VideoChannelAllOfOwnerAccount**](VideoChannelAllOfOwnerAccount.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_channel_list_data_inner import VideoChannelListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of VideoChannelListDataInner from a JSON string
video_channel_list_data_inner_instance = VideoChannelListDataInner.from_json(json)
# print the JSON string representation of the object
print VideoChannelListDataInner.to_json()

# convert the object into a dict
video_channel_list_data_inner_dict = video_channel_list_data_inner_instance.to_dict()
# create an instance of VideoChannelListDataInner from a dict
video_channel_list_data_inner_form_dict = video_channel_list_data_inner.from_dict(video_channel_list_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



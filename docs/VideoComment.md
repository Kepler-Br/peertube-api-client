# VideoComment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**text** | **str** | Text of the comment | [optional] 
**thread_id** | **int** |  | [optional] 
**in_reply_to_comment_id** | **int** |  | [optional] 
**video_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**is_deleted** | **bool** |  | [optional] [default to False]
**total_replies_from_video_author** | **int** |  | [optional] 
**total_replies** | **int** |  | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_comment import VideoComment

# TODO update the JSON string below
json = "{}"
# create an instance of VideoComment from a JSON string
video_comment_instance = VideoComment.from_json(json)
# print the JSON string representation of the object
print VideoComment.to_json()

# convert the object into a dict
video_comment_dict = video_comment_instance.to_dict()
# create an instance of VideoComment from a dict
video_comment_form_dict = video_comment.from_dict(video_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



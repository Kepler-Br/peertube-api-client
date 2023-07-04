# VideoCommentThreadTree


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**VideoComment**](VideoComment.md) |  | [optional] 
**children** | [**List[VideoCommentThreadTree]**](VideoCommentThreadTree.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_comment_thread_tree import VideoCommentThreadTree

# TODO update the JSON string below
json = "{}"
# create an instance of VideoCommentThreadTree from a JSON string
video_comment_thread_tree_instance = VideoCommentThreadTree.from_json(json)
# print the JSON string representation of the object
print VideoCommentThreadTree.to_json()

# convert the object into a dict
video_comment_thread_tree_dict = video_comment_thread_tree_instance.to_dict()
# create an instance of VideoCommentThreadTree from a dict
video_comment_thread_tree_form_dict = video_comment_thread_tree.from_dict(video_comment_thread_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



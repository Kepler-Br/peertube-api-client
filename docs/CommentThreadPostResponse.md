# CommentThreadPostResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**VideoComment**](VideoComment.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.comment_thread_post_response import CommentThreadPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommentThreadPostResponse from a JSON string
comment_thread_post_response_instance = CommentThreadPostResponse.from_json(json)
# print the JSON string representation of the object
print CommentThreadPostResponse.to_json()

# convert the object into a dict
comment_thread_post_response_dict = comment_thread_post_response_instance.to_dict()
# create an instance of CommentThreadPostResponse from a dict
comment_thread_post_response_form_dict = comment_thread_post_response.from_dict(comment_thread_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



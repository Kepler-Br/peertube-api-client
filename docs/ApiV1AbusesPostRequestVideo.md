# ApiV1AbusesPostRequestVideo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**start_at** | **int** | Timestamp in the video that marks the beginning of the report | [optional] 
**end_at** | **int** | Timestamp in the video that marks the ending of the report | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_abuses_post_request_video import ApiV1AbusesPostRequestVideo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AbusesPostRequestVideo from a JSON string
api_v1_abuses_post_request_video_instance = ApiV1AbusesPostRequestVideo.from_json(json)
# print the JSON string representation of the object
print ApiV1AbusesPostRequestVideo.to_json()

# convert the object into a dict
api_v1_abuses_post_request_video_dict = api_v1_abuses_post_request_video_instance.to_dict()
# create an instance of ApiV1AbusesPostRequestVideo from a dict
api_v1_abuses_post_request_video_form_dict = api_v1_abuses_post_request_video.from_dict(api_v1_abuses_post_request_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



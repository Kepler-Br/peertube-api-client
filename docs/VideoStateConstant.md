# VideoStateConstant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The video state: - &#x60;1&#x60;: Published - &#x60;2&#x60;: To transcode - &#x60;3&#x60;: To import - &#x60;4&#x60;: Waiting for live stream - &#x60;5&#x60;: Live ended - &#x60;6&#x60;: To move to an external storage (object storage...) - &#x60;7&#x60;: Transcoding failed - &#x60;8&#x60;: Moving to an external storage failed - &#x60;9&#x60;: To edit using studio edition feature  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_state_constant import VideoStateConstant

# TODO update the JSON string below
json = "{}"
# create an instance of VideoStateConstant from a JSON string
video_state_constant_instance = VideoStateConstant.from_json(json)
# print the JSON string representation of the object
print VideoStateConstant.to_json()

# convert the object into a dict
video_state_constant_dict = video_state_constant_instance.to_dict()
# create an instance of VideoStateConstant from a dict
video_state_constant_form_dict = video_state_constant.from_dict(video_state_constant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



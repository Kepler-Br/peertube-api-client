# Video


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**uuid** | **str** |  | [optional] 
**short_uuid** | **str** | translation of a uuid v4 with a bigger alphabet to have a shorter uuid | [optional] 
**is_live** | **bool** |  | [optional] 
**created_at** | **datetime** | time at which the video object was first drafted | [optional] 
**published_at** | **datetime** | time at which the video was marked as ready for playback (with restrictions depending on &#x60;privacy&#x60;). Usually set after a &#x60;state&#x60; evolution. | [optional] 
**updated_at** | **datetime** | last time the video&#39;s metadata was modified | [optional] 
**originally_published_at** | **datetime** | used to represent a date of first publication, prior to the practical publication date of &#x60;publishedAt&#x60; | [optional] 
**category** | [**VideoCategory**](VideoCategory.md) |  | [optional] 
**licence** | [**VideoLicence**](VideoLicence.md) |  | [optional] 
**language** | [**VideoLanguage**](VideoLanguage.md) |  | [optional] 
**privacy** | [**VideoPrivacy**](VideoPrivacy.md) |  | [optional] 
**description** | **str** | truncated description of the video, written in Markdown. Resolve &#x60;descriptionPath&#x60; to get the full description of maximum &#x60;10000&#x60; characters.  | [optional] 
**duration** | **int** | duration of the video in seconds | [optional] 
**is_local** | **bool** |  | [optional] 
**name** | **str** | title of the video | [optional] 
**thumbnail_path** | **str** |  | [optional] 
**preview_path** | **str** |  | [optional] 
**embed_path** | **str** |  | [optional] 
**views** | **int** |  | [optional] 
**likes** | **int** |  | [optional] 
**dislikes** | **int** |  | [optional] 
**nsfw** | **bool** |  | [optional] 
**wait_transcoding** | **bool** |  | [optional] 
**state** | [**VideoState**](VideoState.md) |  | [optional] 
**scheduled_update** | [**VideoScheduledUpdate**](VideoScheduledUpdate.md) |  | [optional] 
**blacklisted** | **bool** |  | [optional] 
**blacklisted_reason** | **str** |  | [optional] 
**account** | [**AccountSummary**](AccountSummary.md) |  | [optional] 
**channel** | [**VideoChannelSummary**](VideoChannelSummary.md) |  | [optional] 
**user_history** | [**VideoUserHistory**](VideoUserHistory.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video import Video

# TODO update the JSON string below
json = "{}"
# create an instance of Video from a JSON string
video_instance = Video.from_json(json)
# print the JSON string representation of the object
print Video.to_json()

# convert the object into a dict
video_dict = video_instance.to_dict()
# create an instance of Video from a dict
video_form_dict = video.from_dict(video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



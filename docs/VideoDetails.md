# VideoDetails


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
**account** | [**Account**](Account.md) |  | [optional] 
**channel** | [**VideoChannel**](VideoChannel.md) |  | [optional] 
**user_history** | [**VideoUserHistory**](VideoUserHistory.md) |  | [optional] 
**viewers** | **int** | If the video is a live, you have the amount of current viewers | [optional] 
**description_path** | **str** | path at which to get the full description of maximum &#x60;10000&#x60; characters | [optional] 
**support** | **str** | A text tell the audience how to support the video creator | [optional] 
**tags** | **List[str]** |  | [optional] 
**comments_enabled** | **bool** |  | [optional] 
**download_enabled** | **bool** |  | [optional] 
**tracker_urls** | **List[str]** |  | [optional] 
**files** | [**List[VideoFile]**](VideoFile.md) | WebTorrent/raw video files. If WebTorrent is disabled on the server:  - field will be empty - video files will be found in &#x60;streamingPlaylists[].files&#x60; field  | [optional] 
**streaming_playlists** | [**List[VideoStreamingPlaylists]**](VideoStreamingPlaylists.md) | HLS playlists/manifest files. If HLS is disabled on the server:  - field will be empty - video files will be found in &#x60;files&#x60; field  | [optional] 

## Example

```python
from peertube_api_client.models.video_details import VideoDetails

# TODO update the JSON string below
json = "{}"
# create an instance of VideoDetails from a JSON string
video_details_instance = VideoDetails.from_json(json)
# print the JSON string representation of the object
print VideoDetails.to_json()

# convert the object into a dict
video_details_dict = video_details_instance.to_dict()
# create an instance of VideoDetails from a dict
video_details_form_dict = video_details.from_dict(video_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



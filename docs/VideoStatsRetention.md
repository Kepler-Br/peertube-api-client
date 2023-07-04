# VideoStatsRetention


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VideoStatsRetentionDataInner]**](VideoStatsRetentionDataInner.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_stats_retention import VideoStatsRetention

# TODO update the JSON string below
json = "{}"
# create an instance of VideoStatsRetention from a JSON string
video_stats_retention_instance = VideoStatsRetention.from_json(json)
# print the JSON string representation of the object
print VideoStatsRetention.to_json()

# convert the object into a dict
video_stats_retention_dict = video_stats_retention_instance.to_dict()
# create an instance of VideoStatsRetention from a dict
video_stats_retention_form_dict = video_stats_retention.from_dict(video_stats_retention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



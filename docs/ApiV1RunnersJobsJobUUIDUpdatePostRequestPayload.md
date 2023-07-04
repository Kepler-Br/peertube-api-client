# ApiV1RunnersJobsJobUUIDUpdatePostRequestPayload

Provide live transcoding chunks update

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**master_playlist_file** | **bytearray** |  | [optional] 
**resolution_playlist_file** | **bytearray** |  | [optional] 
**resolution_playlist_filename** | **str** |  | [optional] 
**video_chunk_file** | **bytearray** |  | [optional] 
**video_chunk_filename** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_runners_jobs_job_uuid_update_post_request_payload import ApiV1RunnersJobsJobUUIDUpdatePostRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1RunnersJobsJobUUIDUpdatePostRequestPayload from a JSON string
api_v1_runners_jobs_job_uuid_update_post_request_payload_instance = ApiV1RunnersJobsJobUUIDUpdatePostRequestPayload.from_json(json)
# print the JSON string representation of the object
print ApiV1RunnersJobsJobUUIDUpdatePostRequestPayload.to_json()

# convert the object into a dict
api_v1_runners_jobs_job_uuid_update_post_request_payload_dict = api_v1_runners_jobs_job_uuid_update_post_request_payload_instance.to_dict()
# create an instance of ApiV1RunnersJobsJobUUIDUpdatePostRequestPayload from a dict
api_v1_runners_jobs_job_uuid_update_post_request_payload_form_dict = api_v1_runners_jobs_job_uuid_update_post_request_payload.from_dict(api_v1_runners_jobs_job_uuid_update_post_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



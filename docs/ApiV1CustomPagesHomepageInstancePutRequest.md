# ApiV1CustomPagesHomepageInstancePutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | content of the homepage, that will be injected in the client | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_custom_pages_homepage_instance_put_request import ApiV1CustomPagesHomepageInstancePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CustomPagesHomepageInstancePutRequest from a JSON string
api_v1_custom_pages_homepage_instance_put_request_instance = ApiV1CustomPagesHomepageInstancePutRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1CustomPagesHomepageInstancePutRequest.to_json()

# convert the object into a dict
api_v1_custom_pages_homepage_instance_put_request_dict = api_v1_custom_pages_homepage_instance_put_request_instance.to_dict()
# create an instance of ApiV1CustomPagesHomepageInstancePutRequest from a dict
api_v1_custom_pages_homepage_instance_put_request_form_dict = api_v1_custom_pages_homepage_instance_put_request.from_dict(api_v1_custom_pages_homepage_instance_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



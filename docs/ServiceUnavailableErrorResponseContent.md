# ServiceUnavailableErrorResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data** | **object** | Empty object for operations that don&#39;t return data | 

## Example

```python
from ha_sdk_python.models.service_unavailable_error_response_content import ServiceUnavailableErrorResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUnavailableErrorResponseContent from a JSON string
service_unavailable_error_response_content_instance = ServiceUnavailableErrorResponseContent.from_json(json)
# print the JSON string representation of the object
print(ServiceUnavailableErrorResponseContent.to_json())

# convert the object into a dict
service_unavailable_error_response_content_dict = service_unavailable_error_response_content_instance.to_dict()
# create an instance of ServiceUnavailableErrorResponseContent from a dict
service_unavailable_error_response_content_from_dict = ServiceUnavailableErrorResponseContent.from_dict(service_unavailable_error_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



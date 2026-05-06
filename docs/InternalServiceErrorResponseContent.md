# InternalServiceErrorResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data** | **object** | Empty object for operations that don&#39;t return data | 

## Example

```python
from hostafrica_sdk_python.models.internal_service_error_response_content import InternalServiceErrorResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of InternalServiceErrorResponseContent from a JSON string
internal_service_error_response_content_instance = InternalServiceErrorResponseContent.from_json(json)
# print the JSON string representation of the object
print(InternalServiceErrorResponseContent.to_json())

# convert the object into a dict
internal_service_error_response_content_dict = internal_service_error_response_content_instance.to_dict()
# create an instance of InternalServiceErrorResponseContent from a dict
internal_service_error_response_content_from_dict = InternalServiceErrorResponseContent.from_dict(internal_service_error_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



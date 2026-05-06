# TooManyRequestsErrorResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data** | **object** | Empty object for operations that don&#39;t return data | 

## Example

```python
from hostafrica_sdk_python.models.too_many_requests_error_response_content import TooManyRequestsErrorResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of TooManyRequestsErrorResponseContent from a JSON string
too_many_requests_error_response_content_instance = TooManyRequestsErrorResponseContent.from_json(json)
# print the JSON string representation of the object
print(TooManyRequestsErrorResponseContent.to_json())

# convert the object into a dict
too_many_requests_error_response_content_dict = too_many_requests_error_response_content_instance.to_dict()
# create an instance of TooManyRequestsErrorResponseContent from a dict
too_many_requests_error_response_content_from_dict = TooManyRequestsErrorResponseContent.from_dict(too_many_requests_error_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



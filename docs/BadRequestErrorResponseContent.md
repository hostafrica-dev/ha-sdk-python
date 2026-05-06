# BadRequestErrorResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data** | **object** | Empty object for operations that don&#39;t return data | 

## Example

```python
from hostafrica_sdk_python.models.bad_request_error_response_content import BadRequestErrorResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestErrorResponseContent from a JSON string
bad_request_error_response_content_instance = BadRequestErrorResponseContent.from_json(json)
# print the JSON string representation of the object
print(BadRequestErrorResponseContent.to_json())

# convert the object into a dict
bad_request_error_response_content_dict = bad_request_error_response_content_instance.to_dict()
# create an instance of BadRequestErrorResponseContent from a dict
bad_request_error_response_content_from_dict = BadRequestErrorResponseContent.from_dict(bad_request_error_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



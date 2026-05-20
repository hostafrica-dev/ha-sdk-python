# ForbiddenErrorResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data** | **object** | Empty object for operations that don&#39;t return data | 

## Example

```python
from ha_sdk_python.models.forbidden_error_response_content import ForbiddenErrorResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ForbiddenErrorResponseContent from a JSON string
forbidden_error_response_content_instance = ForbiddenErrorResponseContent.from_json(json)
# print the JSON string representation of the object
print(ForbiddenErrorResponseContent.to_json())

# convert the object into a dict
forbidden_error_response_content_dict = forbidden_error_response_content_instance.to_dict()
# create an instance of ForbiddenErrorResponseContent from a dict
forbidden_error_response_content_from_dict = ForbiddenErrorResponseContent.from_dict(forbidden_error_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



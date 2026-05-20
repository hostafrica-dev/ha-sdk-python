# UnauthorizedErrorResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data** | **object** | Empty object for operations that don&#39;t return data | 

## Example

```python
from ha_sdk_python.models.unauthorized_error_response_content import UnauthorizedErrorResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of UnauthorizedErrorResponseContent from a JSON string
unauthorized_error_response_content_instance = UnauthorizedErrorResponseContent.from_json(json)
# print the JSON string representation of the object
print(UnauthorizedErrorResponseContent.to_json())

# convert the object into a dict
unauthorized_error_response_content_dict = unauthorized_error_response_content_instance.to_dict()
# create an instance of UnauthorizedErrorResponseContent from a dict
unauthorized_error_response_content_from_dict = UnauthorizedErrorResponseContent.from_dict(unauthorized_error_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



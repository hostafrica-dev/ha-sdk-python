# ValidationErrorResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data** | **object** | Empty object for operations that don&#39;t return data | 

## Example

```python
from hostafrica_sdk_python.models.validation_error_response_content import ValidationErrorResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorResponseContent from a JSON string
validation_error_response_content_instance = ValidationErrorResponseContent.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorResponseContent.to_json())

# convert the object into a dict
validation_error_response_content_dict = validation_error_response_content_instance.to_dict()
# create an instance of ValidationErrorResponseContent from a dict
validation_error_response_content_from_dict = ValidationErrorResponseContent.from_dict(validation_error_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



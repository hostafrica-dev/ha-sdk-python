# ResourceNotFoundErrorResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data** | **object** | Empty object for operations that don&#39;t return data | 

## Example

```python
from hostafrica_sdk_python.models.resource_not_found_error_response_content import ResourceNotFoundErrorResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceNotFoundErrorResponseContent from a JSON string
resource_not_found_error_response_content_instance = ResourceNotFoundErrorResponseContent.from_json(json)
# print the JSON string representation of the object
print(ResourceNotFoundErrorResponseContent.to_json())

# convert the object into a dict
resource_not_found_error_response_content_dict = resource_not_found_error_response_content_instance.to_dict()
# create an instance of ResourceNotFoundErrorResponseContent from a dict
resource_not_found_error_response_content_from_dict = ResourceNotFoundErrorResponseContent.from_dict(resource_not_found_error_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



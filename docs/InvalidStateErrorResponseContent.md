# InvalidStateErrorResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data** | **object** | Empty object for operations that don&#39;t return data | 

## Example

```python
from hostafrica_sdk_python.models.invalid_state_error_response_content import InvalidStateErrorResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidStateErrorResponseContent from a JSON string
invalid_state_error_response_content_instance = InvalidStateErrorResponseContent.from_json(json)
# print the JSON string representation of the object
print(InvalidStateErrorResponseContent.to_json())

# convert the object into a dict
invalid_state_error_response_content_dict = invalid_state_error_response_content_instance.to_dict()
# create an instance of InvalidStateErrorResponseContent from a dict
invalid_state_error_response_content_from_dict = InvalidStateErrorResponseContent.from_dict(invalid_state_error_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



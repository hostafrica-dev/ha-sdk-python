# InternalServiceError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data** | **object** | Empty object for operations that don&#39;t return data | 

## Example

```python
from hostafrica_sdk_python.models.internal_service_error import InternalServiceError

# TODO update the JSON string below
json = "{}"
# create an instance of InternalServiceError from a JSON string
internal_service_error_instance = InternalServiceError.from_json(json)
# print the JSON string representation of the object
print(InternalServiceError.to_json())

# convert the object into a dict
internal_service_error_dict = internal_service_error_instance.to_dict()
# create an instance of InternalServiceError from a dict
internal_service_error_from_dict = InternalServiceError.from_dict(internal_service_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



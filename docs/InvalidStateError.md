# InvalidStateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data** | **object** | Empty object for operations that don&#39;t return data | 

## Example

```python
from hostafrica_sdk_python.models.invalid_state_error import InvalidStateError

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidStateError from a JSON string
invalid_state_error_instance = InvalidStateError.from_json(json)
# print the JSON string representation of the object
print(InvalidStateError.to_json())

# convert the object into a dict
invalid_state_error_dict = invalid_state_error_instance.to_dict()
# create an instance of InvalidStateError from a dict
invalid_state_error_from_dict = InvalidStateError.from_dict(invalid_state_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



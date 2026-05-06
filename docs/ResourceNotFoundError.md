# ResourceNotFoundError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data** | **object** | Empty object for operations that don&#39;t return data | 

## Example

```python
from hostafrica_sdk_python.models.resource_not_found_error import ResourceNotFoundError

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceNotFoundError from a JSON string
resource_not_found_error_instance = ResourceNotFoundError.from_json(json)
# print the JSON string representation of the object
print(ResourceNotFoundError.to_json())

# convert the object into a dict
resource_not_found_error_dict = resource_not_found_error_instance.to_dict()
# create an instance of ResourceNotFoundError from a dict
resource_not_found_error_from_dict = ResourceNotFoundError.from_dict(resource_not_found_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



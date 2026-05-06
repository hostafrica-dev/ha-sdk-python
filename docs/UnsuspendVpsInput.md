# UnsuspendVpsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.unsuspend_vps_input import UnsuspendVpsInput

# TODO update the JSON string below
json = "{}"
# create an instance of UnsuspendVpsInput from a JSON string
unsuspend_vps_input_instance = UnsuspendVpsInput.from_json(json)
# print the JSON string representation of the object
print(UnsuspendVpsInput.to_json())

# convert the object into a dict
unsuspend_vps_input_dict = unsuspend_vps_input_instance.to_dict()
# create an instance of UnsuspendVpsInput from a dict
unsuspend_vps_input_from_dict = UnsuspendVpsInput.from_dict(unsuspend_vps_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



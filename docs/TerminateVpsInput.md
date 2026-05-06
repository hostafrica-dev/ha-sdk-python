# TerminateVpsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.terminate_vps_input import TerminateVpsInput

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateVpsInput from a JSON string
terminate_vps_input_instance = TerminateVpsInput.from_json(json)
# print the JSON string representation of the object
print(TerminateVpsInput.to_json())

# convert the object into a dict
terminate_vps_input_dict = terminate_vps_input_instance.to_dict()
# create an instance of TerminateVpsInput from a dict
terminate_vps_input_from_dict = TerminateVpsInput.from_dict(terminate_vps_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



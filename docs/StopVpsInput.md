# StopVpsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.stop_vps_input import StopVpsInput

# TODO update the JSON string below
json = "{}"
# create an instance of StopVpsInput from a JSON string
stop_vps_input_instance = StopVpsInput.from_json(json)
# print the JSON string representation of the object
print(StopVpsInput.to_json())

# convert the object into a dict
stop_vps_input_dict = stop_vps_input_instance.to_dict()
# create an instance of StopVpsInput from a dict
stop_vps_input_from_dict = StopVpsInput.from_dict(stop_vps_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



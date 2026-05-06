# ShutdownVpsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.shutdown_vps_input import ShutdownVpsInput

# TODO update the JSON string below
json = "{}"
# create an instance of ShutdownVpsInput from a JSON string
shutdown_vps_input_instance = ShutdownVpsInput.from_json(json)
# print the JSON string representation of the object
print(ShutdownVpsInput.to_json())

# convert the object into a dict
shutdown_vps_input_dict = shutdown_vps_input_instance.to_dict()
# create an instance of ShutdownVpsInput from a dict
shutdown_vps_input_from_dict = ShutdownVpsInput.from_dict(shutdown_vps_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# StartVpsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.start_vps_input import StartVpsInput

# TODO update the JSON string below
json = "{}"
# create an instance of StartVpsInput from a JSON string
start_vps_input_instance = StartVpsInput.from_json(json)
# print the JSON string representation of the object
print(StartVpsInput.to_json())

# convert the object into a dict
start_vps_input_dict = start_vps_input_instance.to_dict()
# create an instance of StartVpsInput from a dict
start_vps_input_from_dict = StartVpsInput.from_dict(start_vps_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



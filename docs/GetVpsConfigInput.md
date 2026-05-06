# GetVpsConfigInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.get_vps_config_input import GetVpsConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of GetVpsConfigInput from a JSON string
get_vps_config_input_instance = GetVpsConfigInput.from_json(json)
# print the JSON string representation of the object
print(GetVpsConfigInput.to_json())

# convert the object into a dict
get_vps_config_input_dict = get_vps_config_input_instance.to_dict()
# create an instance of GetVpsConfigInput from a dict
get_vps_config_input_from_dict = GetVpsConfigInput.from_dict(get_vps_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



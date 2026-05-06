# GetVpsConfigOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsConfigResponseData**](VpsConfigResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.get_vps_config_output import GetVpsConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetVpsConfigOutput from a JSON string
get_vps_config_output_instance = GetVpsConfigOutput.from_json(json)
# print the JSON string representation of the object
print(GetVpsConfigOutput.to_json())

# convert the object into a dict
get_vps_config_output_dict = get_vps_config_output_instance.to_dict()
# create an instance of GetVpsConfigOutput from a dict
get_vps_config_output_from_dict = GetVpsConfigOutput.from_dict(get_vps_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



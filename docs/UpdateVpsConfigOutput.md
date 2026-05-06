# UpdateVpsConfigOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.update_vps_config_output import UpdateVpsConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVpsConfigOutput from a JSON string
update_vps_config_output_instance = UpdateVpsConfigOutput.from_json(json)
# print the JSON string representation of the object
print(UpdateVpsConfigOutput.to_json())

# convert the object into a dict
update_vps_config_output_dict = update_vps_config_output_instance.to_dict()
# create an instance of UpdateVpsConfigOutput from a dict
update_vps_config_output_from_dict = UpdateVpsConfigOutput.from_dict(update_vps_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



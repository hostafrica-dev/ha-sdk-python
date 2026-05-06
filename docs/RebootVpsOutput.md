# RebootVpsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.reboot_vps_output import RebootVpsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RebootVpsOutput from a JSON string
reboot_vps_output_instance = RebootVpsOutput.from_json(json)
# print the JSON string representation of the object
print(RebootVpsOutput.to_json())

# convert the object into a dict
reboot_vps_output_dict = reboot_vps_output_instance.to_dict()
# create an instance of RebootVpsOutput from a dict
reboot_vps_output_from_dict = RebootVpsOutput.from_dict(reboot_vps_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



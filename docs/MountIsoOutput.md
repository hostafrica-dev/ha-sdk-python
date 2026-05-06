# MountIsoOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.mount_iso_output import MountIsoOutput

# TODO update the JSON string below
json = "{}"
# create an instance of MountIsoOutput from a JSON string
mount_iso_output_instance = MountIsoOutput.from_json(json)
# print the JSON string representation of the object
print(MountIsoOutput.to_json())

# convert the object into a dict
mount_iso_output_dict = mount_iso_output_instance.to_dict()
# create an instance of MountIsoOutput from a dict
mount_iso_output_from_dict = MountIsoOutput.from_dict(mount_iso_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



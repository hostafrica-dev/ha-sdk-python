# MountIsoResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.mount_iso_response_content import MountIsoResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of MountIsoResponseContent from a JSON string
mount_iso_response_content_instance = MountIsoResponseContent.from_json(json)
# print the JSON string representation of the object
print(MountIsoResponseContent.to_json())

# convert the object into a dict
mount_iso_response_content_dict = mount_iso_response_content_instance.to_dict()
# create an instance of MountIsoResponseContent from a dict
mount_iso_response_content_from_dict = MountIsoResponseContent.from_dict(mount_iso_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



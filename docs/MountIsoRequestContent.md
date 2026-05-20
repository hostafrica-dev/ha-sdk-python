# MountIsoRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**iso** | **str** | Name of the ISO image to mount | 
**format_master_disk** | **bool** | Whether to format the master disk before mounting the ISO | [optional] 

## Example

```python
from ha_sdk_python.models.mount_iso_request_content import MountIsoRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of MountIsoRequestContent from a JSON string
mount_iso_request_content_instance = MountIsoRequestContent.from_json(json)
# print the JSON string representation of the object
print(MountIsoRequestContent.to_json())

# convert the object into a dict
mount_iso_request_content_dict = mount_iso_request_content_instance.to_dict()
# create an instance of MountIsoRequestContent from a dict
mount_iso_request_content_from_dict = MountIsoRequestContent.from_dict(mount_iso_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# OsImage

Storage/OS image information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage** | **str** | Storage name | 
**enabled** | **int** | Whether the storage is enabled | 
**shared** | **int** | Whether the storage is shared | 
**used_fraction** | **float** | Fraction of storage used (0.0 to 1.0) | 
**type** | **str** | Storage type (e.g., dir, lvm) | 
**content** | **str** | Content types available in this storage | 
**total** | **int** | Total storage capacity in bytes | 
**active** | **int** | Whether the storage is active | 
**used** | **int** | Used storage in bytes | 
**avail** | **int** | Available storage in bytes | 

## Example

```python
from hostafrica_sdk_python.models.os_image import OsImage

# TODO update the JSON string below
json = "{}"
# create an instance of OsImage from a JSON string
os_image_instance = OsImage.from_json(json)
# print the JSON string representation of the object
print(OsImage.to_json())

# convert the object into a dict
os_image_dict = os_image_instance.to_dict()
# create an instance of OsImage from a dict
os_image_from_dict = OsImage.from_dict(os_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



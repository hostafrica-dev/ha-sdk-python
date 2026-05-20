# ServiceBackupsResponseData

Response data for service backups operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**backups** | [**List[BackupItem]**](BackupItem.md) | List of backups for the service | 
**quota_total** | **float** | Total backup quota (null if unlimited) | [optional] 
**quota_used** | **float** | Used backup quota | 
**quota_unit** | **str** | Unit for quota measurements (e.g., GiB) | 
**available_compress_methods** | [**List[CompressionMethod]**](CompressionMethod.md) | Available compression methods for creating backups | 
**available_modes** | [**List[BackupMode]**](BackupMode.md) | Available backup modes | 
**backup_is_creating** | **bool** | Whether a backup is currently being created | 
**backup_creation** | [**BackupCreationInfo**](BackupCreationInfo.md) |  | [optional] 

## Example

```python
from ha_sdk_python.models.service_backups_response_data import ServiceBackupsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceBackupsResponseData from a JSON string
service_backups_response_data_instance = ServiceBackupsResponseData.from_json(json)
# print the JSON string representation of the object
print(ServiceBackupsResponseData.to_json())

# convert the object into a dict
service_backups_response_data_dict = service_backups_response_data_instance.to_dict()
# create an instance of ServiceBackupsResponseData from a dict
service_backups_response_data_from_dict = ServiceBackupsResponseData.from_dict(service_backups_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



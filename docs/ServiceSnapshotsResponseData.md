# ServiceSnapshotsResponseData

Response data for service snapshots operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**snapshots** | [**List[SnapshotItem]**](SnapshotItem.md) | List of snapshots | [optional] 
**max_snapshots** | **int** | Maximum number of snapshots allowed | [optional] 
**snapshots_count** | **int** | Number of snapshots currently stored | [optional] 

## Example

```python
from ha_sdk_python.models.service_snapshots_response_data import ServiceSnapshotsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSnapshotsResponseData from a JSON string
service_snapshots_response_data_instance = ServiceSnapshotsResponseData.from_json(json)
# print the JSON string representation of the object
print(ServiceSnapshotsResponseData.to_json())

# convert the object into a dict
service_snapshots_response_data_dict = service_snapshots_response_data_instance.to_dict()
# create an instance of ServiceSnapshotsResponseData from a dict
service_snapshots_response_data_from_dict = ServiceSnapshotsResponseData.from_dict(service_snapshots_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



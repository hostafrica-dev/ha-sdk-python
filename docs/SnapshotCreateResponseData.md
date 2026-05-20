# SnapshotCreateResponseData

Response data for snapshot creation operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**task_id** | **int** | Task ID for the snapshot creation | [optional] 

## Example

```python
from ha_sdk_python.models.snapshot_create_response_data import SnapshotCreateResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotCreateResponseData from a JSON string
snapshot_create_response_data_instance = SnapshotCreateResponseData.from_json(json)
# print the JSON string representation of the object
print(SnapshotCreateResponseData.to_json())

# convert the object into a dict
snapshot_create_response_data_dict = snapshot_create_response_data_instance.to_dict()
# create an instance of SnapshotCreateResponseData from a dict
snapshot_create_response_data_from_dict = SnapshotCreateResponseData.from_dict(snapshot_create_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



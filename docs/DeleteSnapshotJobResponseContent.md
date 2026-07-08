# DeleteSnapshotJobResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**SnapshotJobDeleteResponseData**](SnapshotJobDeleteResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.delete_snapshot_job_response_content import DeleteSnapshotJobResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSnapshotJobResponseContent from a JSON string
delete_snapshot_job_response_content_instance = DeleteSnapshotJobResponseContent.from_json(json)
# print the JSON string representation of the object
print(DeleteSnapshotJobResponseContent.to_json())

# convert the object into a dict
delete_snapshot_job_response_content_dict = delete_snapshot_job_response_content_instance.to_dict()
# create an instance of DeleteSnapshotJobResponseContent from a dict
delete_snapshot_job_response_content_from_dict = DeleteSnapshotJobResponseContent.from_dict(delete_snapshot_job_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DeleteSnapshotJobRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**job_id** | **str** | Snapshot job ID to delete | 

## Example

```python
from ha_sdk_python.models.delete_snapshot_job_request_content import DeleteSnapshotJobRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSnapshotJobRequestContent from a JSON string
delete_snapshot_job_request_content_instance = DeleteSnapshotJobRequestContent.from_json(json)
# print the JSON string representation of the object
print(DeleteSnapshotJobRequestContent.to_json())

# convert the object into a dict
delete_snapshot_job_request_content_dict = delete_snapshot_job_request_content_instance.to_dict()
# create an instance of DeleteSnapshotJobRequestContent from a dict
delete_snapshot_job_request_content_from_dict = DeleteSnapshotJobRequestContent.from_dict(delete_snapshot_job_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



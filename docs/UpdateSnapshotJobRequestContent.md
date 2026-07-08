# UpdateSnapshotJobRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**job_id** | **str** | Snapshot job ID to update | 
**name** | **str** | New name for the snapshot job | [optional] 
**description** | **str** | New description for the snapshot job | [optional] 
**vmstate** | **bool** | Whether to include VM state in the snapshot | [optional] 
**period** | [**SnapshotJobPeriod**](SnapshotJobPeriod.md) |  | [optional] 
**run_every** | **int** | For hourly jobs: run every N hours (e.g. 6 &#x3D; every 6 hours) | [optional] 
**days** | [**List[DayOfWeek]**](DayOfWeek.md) | For daily jobs: days of week when the job should run | [optional] 
**start_time** | **str** | For daily jobs: start time in HH:MM format (e.g. &#39;02:30&#39;) | [optional] 

## Example

```python
from ha_sdk_python.models.update_snapshot_job_request_content import UpdateSnapshotJobRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSnapshotJobRequestContent from a JSON string
update_snapshot_job_request_content_instance = UpdateSnapshotJobRequestContent.from_json(json)
# print the JSON string representation of the object
print(UpdateSnapshotJobRequestContent.to_json())

# convert the object into a dict
update_snapshot_job_request_content_dict = update_snapshot_job_request_content_instance.to_dict()
# create an instance of UpdateSnapshotJobRequestContent from a dict
update_snapshot_job_request_content_from_dict = UpdateSnapshotJobRequestContent.from_dict(update_snapshot_job_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



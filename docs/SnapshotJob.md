# SnapshotJob

Individual snapshot job item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Snapshot job ID | 
**hosting_id** | **int** | Hosting account ID | [optional] 
**vm_id** | **int** | VM ID (null if not yet assigned) | [optional] 
**name** | **str** | Name of the snapshot job | 
**description** | **str** | Description of the snapshot job | [optional] 
**vmstate** | **bool** | Whether VM state is included in the snapshot | [optional] 
**period** | [**SnapshotJobPeriod**](SnapshotJobPeriod.md) |  | 
**run_every** | **int** | For hourly jobs: run every N hours | [optional] 
**days** | [**List[DayOfWeek]**](DayOfWeek.md) | For daily jobs: days of week | [optional] 
**start_time** | **str** | For daily jobs: start time in HH:MM format | [optional] 

## Example

```python
from ha_sdk_python.models.snapshot_job import SnapshotJob

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotJob from a JSON string
snapshot_job_instance = SnapshotJob.from_json(json)
# print the JSON string representation of the object
print(SnapshotJob.to_json())

# convert the object into a dict
snapshot_job_dict = snapshot_job_instance.to_dict()
# create an instance of SnapshotJob from a dict
snapshot_job_from_dict = SnapshotJob.from_dict(snapshot_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SnapshotJobLimits

Limits and quota information for snapshot jobs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_jobs** | **int** | Maximum number of snapshot jobs allowed | 
**job_count** | **int** | Current number of snapshot jobs | 
**can_add_more** | **bool** | Whether more jobs can be added | 

## Example

```python
from ha_sdk_python.models.snapshot_job_limits import SnapshotJobLimits

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotJobLimits from a JSON string
snapshot_job_limits_instance = SnapshotJobLimits.from_json(json)
# print the JSON string representation of the object
print(SnapshotJobLimits.to_json())

# convert the object into a dict
snapshot_job_limits_dict = snapshot_job_limits_instance.to_dict()
# create an instance of SnapshotJobLimits from a dict
snapshot_job_limits_from_dict = SnapshotJobLimits.from_dict(snapshot_job_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



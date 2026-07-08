# SnapshotJobListResponseData

Response data for snapshot job list operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**jobs** | [**List[SnapshotJob]**](SnapshotJob.md) | List of snapshot jobs | 
**limits** | [**SnapshotJobLimits**](SnapshotJobLimits.md) |  | 
**allowed_periods** | **List[str]** | Allowed schedule periods for snapshot jobs | [optional] 

## Example

```python
from ha_sdk_python.models.snapshot_job_list_response_data import SnapshotJobListResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotJobListResponseData from a JSON string
snapshot_job_list_response_data_instance = SnapshotJobListResponseData.from_json(json)
# print the JSON string representation of the object
print(SnapshotJobListResponseData.to_json())

# convert the object into a dict
snapshot_job_list_response_data_dict = snapshot_job_list_response_data_instance.to_dict()
# create an instance of SnapshotJobListResponseData from a dict
snapshot_job_list_response_data_from_dict = SnapshotJobListResponseData.from_dict(snapshot_job_list_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



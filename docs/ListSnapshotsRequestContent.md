# ListSnapshotsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.list_snapshots_request_content import ListSnapshotsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListSnapshotsRequestContent from a JSON string
list_snapshots_request_content_instance = ListSnapshotsRequestContent.from_json(json)
# print the JSON string representation of the object
print(ListSnapshotsRequestContent.to_json())

# convert the object into a dict
list_snapshots_request_content_dict = list_snapshots_request_content_instance.to_dict()
# create an instance of ListSnapshotsRequestContent from a dict
list_snapshots_request_content_from_dict = ListSnapshotsRequestContent.from_dict(list_snapshots_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



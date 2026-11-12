# DeleteDnssecRecordResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**DnssecMutationData**](DnssecMutationData.md) |  | 

## Example

```python
from ha_sdk_python.models.delete_dnssec_record_response_content import DeleteDnssecRecordResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDnssecRecordResponseContent from a JSON string
delete_dnssec_record_response_content_instance = DeleteDnssecRecordResponseContent.from_json(json)
# print the JSON string representation of the object
print(DeleteDnssecRecordResponseContent.to_json())

# convert the object into a dict
delete_dnssec_record_response_content_dict = delete_dnssec_record_response_content_instance.to_dict()
# create an instance of DeleteDnssecRecordResponseContent from a dict
delete_dnssec_record_response_content_from_dict = DeleteDnssecRecordResponseContent.from_dict(delete_dnssec_record_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



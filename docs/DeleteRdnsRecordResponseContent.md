# DeleteRdnsRecordResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.delete_rdns_record_response_content import DeleteRdnsRecordResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRdnsRecordResponseContent from a JSON string
delete_rdns_record_response_content_instance = DeleteRdnsRecordResponseContent.from_json(json)
# print the JSON string representation of the object
print(DeleteRdnsRecordResponseContent.to_json())

# convert the object into a dict
delete_rdns_record_response_content_dict = delete_rdns_record_response_content_instance.to_dict()
# create an instance of DeleteRdnsRecordResponseContent from a dict
delete_rdns_record_response_content_from_dict = DeleteRdnsRecordResponseContent.from_dict(delete_rdns_record_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



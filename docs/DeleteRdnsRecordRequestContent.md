# DeleteRdnsRecordRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id** | **int** | ID of the PTR record to delete | 

## Example

```python
from hostafrica_sdk_python.models.delete_rdns_record_request_content import DeleteRdnsRecordRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRdnsRecordRequestContent from a JSON string
delete_rdns_record_request_content_instance = DeleteRdnsRecordRequestContent.from_json(json)
# print the JSON string representation of the object
print(DeleteRdnsRecordRequestContent.to_json())

# convert the object into a dict
delete_rdns_record_request_content_dict = delete_rdns_record_request_content_instance.to_dict()
# create an instance of DeleteRdnsRecordRequestContent from a dict
delete_rdns_record_request_content_from_dict = DeleteRdnsRecordRequestContent.from_dict(delete_rdns_record_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



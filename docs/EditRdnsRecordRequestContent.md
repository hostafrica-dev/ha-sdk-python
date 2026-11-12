# EditRdnsRecordRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id** | **int** | ID of the PTR record to update | 
**hostname** | **str** | Updated PTR target hostname | 
**ttl** | **int** | Time-to-live in seconds. When omitted, upstream keeps the existing TTL; clamped to [30, 86400] when set | [optional] 

## Example

```python
from ha_sdk_python.models.edit_rdns_record_request_content import EditRdnsRecordRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of EditRdnsRecordRequestContent from a JSON string
edit_rdns_record_request_content_instance = EditRdnsRecordRequestContent.from_json(json)
# print the JSON string representation of the object
print(EditRdnsRecordRequestContent.to_json())

# convert the object into a dict
edit_rdns_record_request_content_dict = edit_rdns_record_request_content_instance.to_dict()
# create an instance of EditRdnsRecordRequestContent from a dict
edit_rdns_record_request_content_from_dict = EditRdnsRecordRequestContent.from_dict(edit_rdns_record_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



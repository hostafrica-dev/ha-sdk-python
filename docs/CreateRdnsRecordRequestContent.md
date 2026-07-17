# CreateRdnsRecordRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | Zone type: 0&#x3D;OTHER, 1&#x3D;DOMAIN, 2&#x3D;HOSTING, 3&#x3D;ADDON | 
**relid** | **int** | Related service id matching the zone type (hosting, addon, or domain) | 
**ip** | **str** | IPv4 or IPv6 address the PTR record should point from | 
**hostname** | **str** | PTR target hostname | 
**ttl** | **int** | Time-to-live in seconds. Defaults to 14400; clamped to [30, 86400] | [optional] 

## Example

```python
from ha_sdk_python.models.create_rdns_record_request_content import CreateRdnsRecordRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRdnsRecordRequestContent from a JSON string
create_rdns_record_request_content_instance = CreateRdnsRecordRequestContent.from_json(json)
# print the JSON string representation of the object
print(CreateRdnsRecordRequestContent.to_json())

# convert the object into a dict
create_rdns_record_request_content_dict = create_rdns_record_request_content_instance.to_dict()
# create an instance of CreateRdnsRecordRequestContent from a dict
create_rdns_record_request_content_from_dict = CreateRdnsRecordRequestContent.from_dict(create_rdns_record_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateRdnsRecordInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | Zone type: 0&#x3D;OTHER, 1&#x3D;DOMAIN, 2&#x3D;HOSTING, 3&#x3D;ADDON | 
**relid** | **int** | Related service id matching the zone type (tblhosting.id, tblhostingaddons.id or tbldomains.id) | 
**ip** | **str** | IPv4 or IPv6 address the PTR record should point from | 
**hostname** | **str** | PTR target hostname | 
**ttl** | **int** | Time-to-live in seconds. Defaults to 14400; clamped to [30, 86400] | [optional] 

## Example

```python
from hostafrica_sdk_python.models.create_rdns_record_input import CreateRdnsRecordInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRdnsRecordInput from a JSON string
create_rdns_record_input_instance = CreateRdnsRecordInput.from_json(json)
# print the JSON string representation of the object
print(CreateRdnsRecordInput.to_json())

# convert the object into a dict
create_rdns_record_input_dict = create_rdns_record_input_instance.to_dict()
# create an instance of CreateRdnsRecordInput from a dict
create_rdns_record_input_from_dict = CreateRdnsRecordInput.from_dict(create_rdns_record_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



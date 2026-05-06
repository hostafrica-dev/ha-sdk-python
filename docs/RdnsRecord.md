# RdnsRecord

A PTR record owned by the client

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Record identifier — use as record_id in PUT/DELETE | 
**ip** | **str** | The IPv4/IPv6 address the PTR points from | 
**hostname** | **str** | Final concatenated PTR target (sub.from) | 
**ttl** | **int** | Time-to-live in seconds | [optional] 
**type** | **int** | Zone type: 0&#x3D;OTHER, 1&#x3D;DOMAIN, 2&#x3D;HOSTING, 3&#x3D;ADDON | [optional] 
**relid** | **int** | Related service id (tblhosting.id / tblhostingaddons.id / tbldomains.id) | [optional] 
**serverid** | **int** |  | 
**clientid** | **int** |  | 
**packageid** | **int** |  | 
**var_from** | **str** | Reverse-DNS zone name (e.g. 10.113.0.203.in-addr.arpa) | [optional] 
**sub** | **str** | Sub-label component of the PTR | [optional] 
**name** | **str** | Full PTR name (e.g. 10.113.0.203.in-addr.arpa) | [optional] 

## Example

```python
from hostafrica_sdk_python.models.rdns_record import RdnsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of RdnsRecord from a JSON string
rdns_record_instance = RdnsRecord.from_json(json)
# print the JSON string representation of the object
print(RdnsRecord.to_json())

# convert the object into a dict
rdns_record_dict = rdns_record_instance.to_dict()
# create an instance of RdnsRecord from a dict
rdns_record_from_dict = RdnsRecord.from_dict(rdns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RdnsAvailableItem

One service the client can manage PTRs for

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | Zone type matching RdnsRecord.type | 
**relid** | **int** | Related service identifier | 
**name** | **str** | Display label for the service | 
**ips** | **List[str]** | Concrete IP addresses available for this service | 
**pools** | [**List[RdnsPool]**](RdnsPool.md) | Subnet pools available when subnet_custom_ip_mode is on | 
**ptr_limit** | **int** | Per-package PTR limit (-1 &#x3D; unlimited) | 
**server_id** | **int** |  | 
**allow_rdns** | **bool** | Server has ALLOW_RDNS&#x3D;on | 
**rdns_supported** | **bool** | Server module supports rDNS | 

## Example

```python
from hostafrica_sdk_python.models.rdns_available_item import RdnsAvailableItem

# TODO update the JSON string below
json = "{}"
# create an instance of RdnsAvailableItem from a JSON string
rdns_available_item_instance = RdnsAvailableItem.from_json(json)
# print the JSON string representation of the object
print(RdnsAvailableItem.to_json())

# convert the object into a dict
rdns_available_item_dict = rdns_available_item_instance.to_dict()
# create an instance of RdnsAvailableItem from a dict
rdns_available_item_from_dict = RdnsAvailableItem.from_dict(rdns_available_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# VpsNetworkRate

Network rate information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mb_per_sec** | **float** | Network rate in MB per second | [optional] 
**mbit_per_sec** | **float** | Network rate in Mbit per second | [optional] 
**human** | **str** | Human-readable network rate | [optional] 

## Example

```python
from ha_sdk_python.models.vps_network_rate import VpsNetworkRate

# TODO update the JSON string below
json = "{}"
# create an instance of VpsNetworkRate from a JSON string
vps_network_rate_instance = VpsNetworkRate.from_json(json)
# print the JSON string representation of the object
print(VpsNetworkRate.to_json())

# convert the object into a dict
vps_network_rate_dict = vps_network_rate_instance.to_dict()
# create an instance of VpsNetworkRate from a dict
vps_network_rate_from_dict = VpsNetworkRate.from_dict(vps_network_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



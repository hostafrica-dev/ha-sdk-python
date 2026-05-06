# VpsDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message | 
**vm_info** | [**VpsVmInfo**](VpsVmInfo.md) |  | 
**cpu** | [**VpsCpuInfo**](VpsCpuInfo.md) |  | 
**memory** | [**VpsMemoryInfo**](VpsMemoryInfo.md) |  | 
**disk** | [**VpsDiskInfo**](VpsDiskInfo.md) |  | 
**bandwidth** | [**VpsBandwidthInfo**](VpsBandwidthInfo.md) |  | 
**network_rate** | [**VpsNetworkRate**](VpsNetworkRate.md) |  | [optional] 
**ip_addresses** | **List[str]** | List of IP addresses assigned to the VPS | 
**credentials** | [**VpsCredentials**](VpsCredentials.md) |  | 
**available_features** | [**VpsAvailableFeatures**](VpsAvailableFeatures.md) |  | 
**os_info** | [**VpsOsInfo**](VpsOsInfo.md) |  | [optional] 

## Example

```python
from hostafrica_sdk_python.models.vps_details_response import VpsDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VpsDetailsResponse from a JSON string
vps_details_response_instance = VpsDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(VpsDetailsResponse.to_json())

# convert the object into a dict
vps_details_response_dict = vps_details_response_instance.to_dict()
# create an instance of VpsDetailsResponse from a dict
vps_details_response_from_dict = VpsDetailsResponse.from_dict(vps_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FirewallMoveResponseData

Response data for firewall move operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**from_pos** | **int** | Original position of the rule | 
**target_pos** | **int** | New position of the rule | 

## Example

```python
from hostafrica_sdk_python.models.firewall_move_response_data import FirewallMoveResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallMoveResponseData from a JSON string
firewall_move_response_data_instance = FirewallMoveResponseData.from_json(json)
# print the JSON string representation of the object
print(FirewallMoveResponseData.to_json())

# convert the object into a dict
firewall_move_response_data_dict = firewall_move_response_data_instance.to_dict()
# create an instance of FirewallMoveResponseData from a dict
firewall_move_response_data_from_dict = FirewallMoveResponseData.from_dict(firewall_move_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



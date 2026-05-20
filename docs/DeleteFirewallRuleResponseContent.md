# DeleteFirewallRuleResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.delete_firewall_rule_response_content import DeleteFirewallRuleResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFirewallRuleResponseContent from a JSON string
delete_firewall_rule_response_content_instance = DeleteFirewallRuleResponseContent.from_json(json)
# print the JSON string representation of the object
print(DeleteFirewallRuleResponseContent.to_json())

# convert the object into a dict
delete_firewall_rule_response_content_dict = delete_firewall_rule_response_content_instance.to_dict()
# create an instance of DeleteFirewallRuleResponseContent from a dict
delete_firewall_rule_response_content_from_dict = DeleteFirewallRuleResponseContent.from_dict(delete_firewall_rule_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



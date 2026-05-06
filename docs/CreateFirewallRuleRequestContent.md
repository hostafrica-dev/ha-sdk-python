# CreateFirewallRuleRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**type** | [**FirewallRuleType**](FirewallRuleType.md) |  | 
**rule_action** | [**FirewallRuleAction**](FirewallRuleAction.md) |  | 
**enable** | **int** | Whether the rule is enabled (1&#x3D;enabled, 0&#x3D;disabled) | [optional] 
**comment** | **str** | Comment/description for the rule | [optional] 
**source** | **str** | Source address/network | [optional] 
**dest** | **str** | Destination address/network | [optional] 
**proto** | **str** | Protocol (tcp, udp, icmp, etc). Use &#39;0&#39; or omit for none | [optional] 
**dport** | **str** | Destination port | [optional] 
**sport** | **str** | Source port | [optional] 
**macro** | **str** | Firewall macro name | [optional] 
**iface** | **str** | Network interface name | [optional] 
**log** | **str** | Log level | [optional] 
**pos** | **int** | Position/priority of the rule | [optional] 

## Example

```python
from hostafrica_sdk_python.models.create_firewall_rule_request_content import CreateFirewallRuleRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFirewallRuleRequestContent from a JSON string
create_firewall_rule_request_content_instance = CreateFirewallRuleRequestContent.from_json(json)
# print the JSON string representation of the object
print(CreateFirewallRuleRequestContent.to_json())

# convert the object into a dict
create_firewall_rule_request_content_dict = create_firewall_rule_request_content_instance.to_dict()
# create an instance of CreateFirewallRuleRequestContent from a dict
create_firewall_rule_request_content_from_dict = CreateFirewallRuleRequestContent.from_dict(create_firewall_rule_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateOrderProductItem

A product line item returned in the order response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_id** | **int** | Line item identifier | 
**service_id** | **int** | Provisioned service identifier | 
**pid** | **int** | WHMCS product ID | 
**name** | **str** | Product name | 
**billing_cycle** | **str** | Billing cycle (e.g. monthly, annually) | 
**domain** | **str** | Domain associated with this service | [optional] 
**hostname** | **str** | Hostname assigned to this service | [optional] 
**amount** | **str** | Line item amount charged (decimal string, e.g. \&quot;2333.33\&quot;) | 

## Example

```python
from ha_sdk_python.models.create_order_product_item import CreateOrderProductItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderProductItem from a JSON string
create_order_product_item_instance = CreateOrderProductItem.from_json(json)
# print the JSON string representation of the object
print(CreateOrderProductItem.to_json())

# convert the object into a dict
create_order_product_item_dict = create_order_product_item_instance.to_dict()
# create an instance of CreateOrderProductItem from a dict
create_order_product_item_from_dict = CreateOrderProductItem.from_dict(create_order_product_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



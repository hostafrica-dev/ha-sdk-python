# ListOrdersResponseData

Top-level data payload for the ListOrders response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[Order]**](Order.md) | List of orders for the authenticated user | 

## Example

```python
from hostafrica_sdk_python.models.list_orders_response_data import ListOrdersResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrdersResponseData from a JSON string
list_orders_response_data_instance = ListOrdersResponseData.from_json(json)
# print the JSON string representation of the object
print(ListOrdersResponseData.to_json())

# convert the object into a dict
list_orders_response_data_dict = list_orders_response_data_instance.to_dict()
# create an instance of ListOrdersResponseData from a dict
list_orders_response_data_from_dict = ListOrdersResponseData.from_dict(list_orders_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



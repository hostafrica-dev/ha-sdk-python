# CatalogueCurrency

Currency info returned in the catalogue response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | ISO currency code (e.g. KES, ZAR) | 
**prefix** | **str** | Currency prefix symbol (e.g. KSh) | 
**suffix** | **str** | Currency suffix symbol (empty string if none) | 

## Example

```python
from hostafrica_sdk_python.models.catalogue_currency import CatalogueCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogueCurrency from a JSON string
catalogue_currency_instance = CatalogueCurrency.from_json(json)
# print the JSON string representation of the object
print(CatalogueCurrency.to_json())

# convert the object into a dict
catalogue_currency_dict = catalogue_currency_instance.to_dict()
# create an instance of CatalogueCurrency from a dict
catalogue_currency_from_dict = CatalogueCurrency.from_dict(catalogue_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



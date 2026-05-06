# GetCatalogueOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**CatalogueData**](CatalogueData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.get_catalogue_output import GetCatalogueOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetCatalogueOutput from a JSON string
get_catalogue_output_instance = GetCatalogueOutput.from_json(json)
# print the JSON string representation of the object
print(GetCatalogueOutput.to_json())

# convert the object into a dict
get_catalogue_output_dict = get_catalogue_output_instance.to_dict()
# create an instance of GetCatalogueOutput from a dict
get_catalogue_output_from_dict = GetCatalogueOutput.from_dict(get_catalogue_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



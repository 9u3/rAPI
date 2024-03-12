# rAPI
Simple API to interact with the Rolimons API.

## Download

`pip install git+https://github.com/9u3/rAPI`

## Usage

Initialize the module with
```py
import rAPI
roli = rAPI()
```

Syntax
```py
roli.nametoValue("Perfectly Legitimate Business Hat") # Value of an item

roli.isProjected("Perfectly Legitimate Business Hat") # See if an item is projected, Returns True if it is

roli.demand("Perfectly Legitimate Business Hat") # Get the demand of an item, Returns a number from 0 to 5

roli.trend("Perfectly Legitimate Business Hat") # Get the trend of an item, Returns a number from 0 to 5

roli.itemDetails("Perfectly Legitimate Business Hat") # Get JSON data of an item, Unmodified.

roli.isRare("Perfectly Legitimate Business Hat") # See if an item is rare, Returns True if it is.
```

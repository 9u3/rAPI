import requests


class Rolimons:
    """A client for interacting with the Rolimons item API."""
    
    # Field indices in the item data array
    NAME = 0
    ALIAS = 1
    RAP = 2
    VALUE = 3
    DEFAULT_VALUE = 4
    DEMAND = 5
    TREND = 6
    PROJECTED = 7
    HYPED = 8
    RARE = 9
    
    def __init__(self):
        """Initialize the Rolimons client and fetch item data."""
        response = requests.get("https://www.rolimons.com/itemapi/itemdetails")
        self.items = response.json()['items']
        self._name_cache = self._build_name_cache()

    def __repr__(self):
        return f"<Rolimons Client: {len(self.items)} items loaded>"
    
    def _build_name_cache(self):
        """Build a cache mapping item names to item IDs for faster lookups."""
        return {
            item_data[self.NAME]: item_id 
            for item_id, item_data in self.items.items()
        }
    
    def _get_item_by_name(self, name):
        """
        Get item data by name.
        
        Args:
            name: The name of the item to find.
            
        Returns:
            The item data array if found, None otherwise.
        """
        item_id = self._name_cache.get(name)
        if item_id:
            return self.items[item_id]
        return None
    
    def _get_field(self, name, field_index, default=None):
        """
        Get a specific field value for an item by name.
        
        Args:
            name: The name of the item.
            field_index: The index of the field to retrieve.
            default: The value to return if the field is -1 or item not found.
            
        Returns:
            The field value or the default value.
        """
        item = self._get_item_by_name(name)
        if item is None:
            return default
        
        value = item[field_index]
        return default if value == -1 else value
    
    def nametoValue(self, name):
        """
        Get the value of an item by name.
        
        Args:
            name: The name of the item.
            
        Returns:
            The item's value, or RAP if value is not available, or None if not found.
        """
        item = self._get_item_by_name(name)
        if item is None:
            return None
        
        value = item[self.VALUE]
        return value if value != -1 else item[self.RAP]
    
    def isProjected(self, name):
        """
        Check if an item is projected.
        
        Args:
            name: The name of the item.
            
        Returns:
            True if projected, False otherwise.
        """
        projected = self._get_field(name, self.PROJECTED, default=-1)
        return projected != -1
    
    def demand(self, name):
        """
        Get the demand level of an item.
        
        Args:
            name: The name of the item.
            
        Returns:
            The demand level, or 0 if not available.
        """
        return self._get_field(name, self.DEMAND, default=0)
    
    def trend(self, name):
        """
        Get the trend value of an item.
        
        Args:
            name: The name of the item.
            
        Returns:
            The trend value, or 0 if not available.
        """
        return self._get_field(name, self.TREND, default=0)
    
    def itemDetails(self, name):
        """
        Get full details for an item.
        
        Args:
            name: The name of the item.
            
        Returns:
            The complete item data array, or None if not found.
        """
        item = self._get_item_by_name(name)
        return item if item is not None else None
    
    def isRare(self, name):
        """
        Check if an item is rare.
        
        Args:
            name: The name of the item.
            
        Returns:
            True if rare, False otherwise.
        """
        rare = self._get_field(name, self.RARE, default=-1)
        return rare != -1
    
    def aliasToName(self, alias):
        """
        Convert an alias to the official item name.
        
        Args:
            alias: The alias of the item.
            
        Returns:
            The official item name, or None if not found.
        """
        for item_data in self.items.values():
            if item_data[self.ALIAS] == alias:
                return item_data[self.NAME]
        return None
    
    def nameToAlias(self, name):
        """
        Convert an official item name to its alias.
        
        Args:
            name: The official name of the item.
            
        Returns:
            The alias of the item, or None if not found.
        """
        item = self._get_item_by_name(name)
        return item[self.ALIAS] if item else None

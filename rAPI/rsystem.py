import requests


class Rolimons:
    def __init__(self):
        self.cl = {"name": 0, "alias": 1, "rap": 2, "value": 3, "defaultValue": 4, "demand": 5, "trend": 6, "projected": 7, "hyped": 8, "rare": 9}
        self.items = items = requests.get("https://www.rolimons.com/itemapi/itemdetails").json()['items']
        
    def nametoValue(self, n):
        for item in self.items:
            name = self.items[str(item)][self.cl.get("name")]
            if name == n:
                if str(self.items[str(item)][self.cl.get("value")]) != "-1":
                    return self.items[str(item)][self.cl.get("value")]
                else:
                    return self.items[str(item)][self.cl.get("rap")]
                
    def isProjected(self, n):
        for item in self.items:
            name = self.items[str(item)][self.cl.get("name")]
            if name == n:
                if str(self.items[str(item)][self.cl.get("projected")]) != "-1":
                    return True
                else:
                    return False

    def demand(self, n):
        for item in self.items:
            name = self.items[str(item)][self.cl.get("name")]
            if name == n:
                if str(self.items[str(item)][self.cl.get("demand")]) != "-1":
                    return self.items[str(item)][self.cl.get("demand")]
                else:
                    return "0"

    def trend(self, n):
        for item in self.items:
            name = self.items[str(item)][self.cl.get("name")]
            if name == n:
                if str(self.items[str(item)][self.cl.get("trend")]) != "-1":
                    return self.items[str(item)][self.cl.get("trend")]
                else:
                    return "0"

    def itemDetails(self, n):
        for item in self.items:
            name = self.items[str(item)][self.cl.get("name")]
            if name == n:
                if str(self.items[str(item)][self.cl.get("trend")]) != "-1":
                    return self.items[str(item)]
                else:
                    return f"No such item as {n}"

    def isRare(self, n):
        for item in self.items:
            name = self.items[str(item)][self.cl.get("name")]
            if name == n:
                if str(self.items[str(item)][self.cl.get("rare")]) != "-1":
                    return True
                else:
                    return False

roli = Rolimons()

print(roli.nametoValue("Perfectly Legitimate Business Hat"))
print(roli.isProjected("Perfectly Legitimate Business Hat"))
print(roli.demand("Perfectly Legitimate Business Hat"))
print(roli.trend("Perfectly Legitimate Business Hat"))
print(roli.itemDetails("Perfectly Legitimate Business Hat"))
print(roli.isRare("Perfectly Legitimate Business Hat"))

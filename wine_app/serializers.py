from builtins import object

class WineSerializer(object):
    def convert_all(self, all_wines):
        output = { 'wines' : []}

        for wine in all_wines:
            wine_details = self.convert_one(wine)
            output['wines'].append(wine_details)
        return output

    def convert_one(self, wine):

        wine_details = {
                'id' : wine.id,
                'wine_name' : wine.wine_name,
                'price' : wine.price,
                'varietal' : wine.varietal,
                'description' : wine.description
            }

        return wine_details
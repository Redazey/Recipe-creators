"""
a little instruction

lpl = liquid + liquid
lpi = liquid + item
ipi = item + item

call this class like this:
LiquidRecipe('lpl', [["minecraft:fluid", value]], [["minecraft:fluid", value],
[["minecraft:fluid", value], "none", "liquid"]

1-st is a first material
2-nd is a second one
3-rd is a result
4-r is a heat requirement
5 is a result type (liquid or item)

and this will generate you some json recipe files

if you're creating LPL or LPI recipe you should write amount of liquid like this: [["minecraft:water", 1000]]
in another way you should write count of item like this: [["minecraft:diamond", 32], ["minecraft:dirt", 1]]

about heat requirement:
there is three types of heat: none, heated, superheated

creator of this script is Redaxel
"""


class MixerRecipe:

    def __init__(self, recipe_type: str, materials1: list, materials2: list, result: list, heat: str,
                 result_type: str):
        self.rec_type = recipe_type
        self.mat1 = materials1
        self.mat2 = materials2
        self.res = result
        self.heat = heat
        self.res_type = result_type

    def recipe(self):

        if self.rec_type == 'lpl':
            _mam = [['fluid', 'amount'], ['fluid', 'amount']]  # mam means material and material
        elif self.rec_type == 'lpi':
            _mam = [['fluid', 'amount'], ['item', 'count']]
        elif self.rec_type == 'ipi':
            _mam = [['item', 'count'], ['item', 'count']]
        else:
            return "You should write a type of recipe (lpl, lpi or ipi)"

        if self.res_type == 'liquid':
            _res_typo = ['fluid', 'amount']
        elif self.res_type == 'item':
            _res_typo = ['item', 'count']
        else:
            return "You should write liquid or item in type of result"

        for i in range(len(self.res)):
            with open(f'{self.res[i][0].strip("tfc:")}_recipe.json', 'w') as f:
                f.write(
                    '{\n'
                    '  "type": "create:mixing",\n'
                    '  "ingredients": [\n'
                    '     {\n'
                    f'       "{_mam[0][0]}": "{self.mat1[i][0]}",\n'
                    f'       "{_mam[1][1]}": {self.mat1[i][1]}\n'
                    '     },\n'
                    '     {\n'
                    f'       "{_mam[1][0]}": "{self.mat2[i][0]}",\n'
                    f'       "{_mam[1][1]}": {self.mat2[i][1]}\n'
                    '     }\n'
                    '  ],\n'
                    '  "results": [\n'
                    '     {\n'
                    f'       "{_res_typo[0]}": "{self.res[i][0]}",\n'
                    f'       "{_res_typo[1]}": {self.res[i][1]}\n'
                    '     }\n'
                    '  ],\n'
                    f'"heatRequirement": "{self.heat}"\n'
                    '}\n')
        return "recipe files was created"


if __name__ == '__main__':
    rec = MixerRecipe('lpl',
                      [["tfc:vinegar", 1], ["tfc:milk_vinegar", 1], ["tfc:vinegar", 1]],
                      [["minecraft:water", 9], ["", 0], ["minecraft:milk", 9]],
                      [["tfc:brine", 10], ["tfc:curdled_milk", 1], ["tfc:milk_vinegar", 10]],
                      "none",
                      "liquid"
                      )

    print(rec.recipe())

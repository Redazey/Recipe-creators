from typing import Set


def arrays():
    materials = ["bismuth_bronze", "black_bronze", "bronze", "copper", "wrought_iron", "steel", "black_steel",
                 "blue_steel", "red_steel"]

    instrument = ["pickaxe_head", "propick_head", "axe_head", "shovel_head", "chisel_head", "hammer_head",
                  "javelin_head", "sword_blade", "knife_blade", "hoe_head", "saw_blade", "scythe_blade", "mace_head"]

    # <item:tfc:metal/ingot/СЛИТОК>
    # <item:tfc:ceramic/ИНСТРУМЕНТ_mold>
    # <item:tfc:metal/ИНСТРУМЕНТ/СЛИТОК>

    for j in range(len(instrument)):
        with open(f'C:\Users\Reda\Desktop\Files\code\melting_{instrument[j]}_mold_recipe.json', 'w') as f:
            f.write(
                '{\n'
                '  "type": "minecraft:smelting",\n'
                '  "ingredients": [\n'
                '     {\n'
                f'       "item": "tfc:ceramic/unfired_{instrument[j]}_mold"\n'
                '     }\n'
                '  ],\n'
                '  "results": [\n'
                '     {\n'
                f'       "item": "tfc:ceramic/{instrument[j]}_mold",\n'
                '        "count": 1\n' 
                '     }\n'
                '  ]\n'
                '}\n')


if __name__ == '__main__':
    arrays()

import argparse

tank_to_fish = {
    "tank_a": "shark, tuna, herring",
    "tank_b": "cod, flounder",
}

parser = argparse.ArgumentParser(
    description="List fish in aquarium.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument("tank", type=str, help="Tank to print fish from.")
parser.add_argument(
    "--upper-case",
    default=False,
    action="store_true",
    help="Upper case the outputted fish.",
)
args = parser.parse_args()

fish = tank_to_fish[args.tank]

if args.upper_case:
    fish = fish.upper()

print(fish)

#args will be a dictionary containing the arguments 
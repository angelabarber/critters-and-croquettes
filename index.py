from slithering import Anaconda, Boa, Copperhead, Corn, Python

from swimming import Crappie, Goldfish, Guppie, Mallard, Merganzer

from walking import Donkey, Goat, Llama, Pig, Sheep

miss_fuzz = Llama("miss fuzz", "domestic llama", "morning")
esther = Donkey("esther", "donkey", "morning")
bubba = Goat("bubba", "dwarf goat", "midday")
penelope = Pig("penelope", "kune kune", "afternoon")
patsy = Sheep("patsy", "sheep", "morning")
rudy = Copperhead("rudy", "copperhead")
hiss = Python("hiss", "python")
hubert = Corn("hubert", "corn snake")
beth = Anaconda("beth", "anaconda", "pinkies")
donald = Mallard("donald", "mallard")
cloe = Goldfish("cloe", "goldfish")
ron = Guppie("ron", "guppie")
bill = Merganzer("bill", "merganzer")
bob = Crappie("bob", "crappie")
gerald = Boa("gerald", "boa")


print(beth.feed())

print(esther.name)

roberto = Llama("Roberto", "llama", "midday")
print(
    f"{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift."
)
# prints Roberto the alpaca is available to pet during the midday shift.

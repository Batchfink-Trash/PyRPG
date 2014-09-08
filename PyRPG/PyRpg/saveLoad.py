import pickle

def save():
    with open("savegame", "wb") as f:
        print("Saving game...")
        pickle.dump(player, f, protocol=2)
        print("Done!")


def load():
    with open("savegame", "rb") as f:
        print("loading game")
        pickle.load(f)
        print("Done!")
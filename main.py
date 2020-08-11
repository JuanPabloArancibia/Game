from enemy import Enemy, Troll, Vampyre

random_monster = Enemy("Basic enemy", 12, 1)

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()

dracula = Vampyre("Dracula")
vampire2 = Vampyre("José")
print(dracula)
dracula.take_damage(5)
print(dracula)

print("-" * 40)
another_troll.take_damage(35)
print(another_troll)

while dracula.alive:
    dracula.take_damage(1)
    print(dracula)

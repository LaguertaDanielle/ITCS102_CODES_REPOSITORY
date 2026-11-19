Jay = {"High athleticism", "parkour", "agility"}

Cacelia = "is a mythical being with a human head, arms, and upper torso (most often female) \nand the tentacles of an octopus or squid from the lower torso down"
Spell_casting = ") is the act or practice of creating or performing magic spells—typically using\n spoken words, rituals, or symbolic actions—to produce a magical or supernatural effect."
Sea_magic = " - is a nature-based spiritual practice or folklore concept that draws\n on the ocean, tides, coastal elements, and water symbolism for transformation, intuition, or protection."
Uma = {Sea_magic, Spell_casting, "transformation into a", Cacelia}

Potion_brewing = "- is the process of mixing, boiling, or steeping ingredients to make\n a potion—a liquid dose or drink believed or intended to have magical, medicinal, or poisonous effects."
Spell_casting = "Performing magic spells, often through spoken words, chants, or rituals to influence a person, object, or situation."
Fairy_magic = "\"Fairy\" comes from Old/Anglo-French faerie, which originally meant \"enchantment\", \"witchcraft\", or \"the realm of mythical beings\" before coming to refer to an individual creature."
Mal = [Fairy_magic, Spell_casting, Potion_brewing]
descendants = {"Daughter of Maleficent & Hades":Mal, "Daughter of Ursula":Uma, "Son of Jafar":Jay}

print(descendants["Daughter of Maleficent & Hades"][0])
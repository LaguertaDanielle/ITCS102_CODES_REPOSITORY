#dictionary

Size_&_Matter_Manipulation== "\"Size\" - refers to how big or small something is, its physical dimensions, or a standard measurement scale \n  \n\"Matter Manipulation\" - controlling or changing physical substance—anything that has mass and takes up space"
Dark_Magic_&_Curses == "\"Dark Magic\" - the use of supernatural powers, spells, or occult forces for evil, harmful, or selfish purposes. \n \"Curses\" - refer to wishes or invocations of harm or misfortune, words used to express anger or profanity"
Dragon_Shapeshifting = "refers to the mythical or fictional ability to transform between a human (or other creature) \nand a dragon, or the power of a dragon to assume a humanoid form."
Maleficent = [Dragon_Shapeshifting, Dark_Magic, Curses, Size_, Matter_Manipulation]

Dark_Magic_Countering = "the act of blocking, neutralizing, or reversing malevolent supernatural spells, curses, or harmful magic."
Life_Restoration_&_Healing == "efers to the process of bringing a person, living thing, or ecosystem back to a healthy, active, or original state of well-being. \n \"Healing\" is the process of becoming well or healthy again after a physical injury, illness, or emotional pain" 
Pyrokinesis = " - Pyro- (from Greek pyr): Means \"fire\" or \"heat\" \n-kinesis (from Greek kinēsis): Means \"movement,\" modeled after telekinesis. \nPyrokinesis is a noun meaning the supposed or fictional ability to create, \ncontrol, or manipulate fire using the mind or psychic power."
Hades = [Pyrokinesis, Life_Restoration, Healing, Dark_Magic_Countering ]

agility = " - (noun, pronounced uh-JIL-ih-tee) \nis the ability to move quickly, easily, and with control, or to think and adapt rapidly."
parkour = " - Referring to the sport or discipline of moving rapidly, smoothly, and efficiently through \nan environment—often urban—by running, jumping, climbing, and \nvaulting over or around obstacles."
High_athleticism = " - possessing an unusually strong, well-developed combination of physical abilities—such as speed, strength, agility, \npower, coordination, and endurance—that enables someone to excel at sports \nor demanding physical movements."
Jay = {High_athleticism, parkour, agility}

Cacelia = " - is a mythical being with a human head, arms, and upper torso (most often female) \nand the tentacles of an octopus or squid from the lower torso down"
Spell_casting = " - is the act or practice of creating or performing magic spells—typically using\n spoken words, rituals, or symbolic actions—to produce a magical or supernatural effect."
Sea_magic = " - is a nature-based spiritual practice or folklore concept that draws\n on the ocean, tides, coastal elements, and water symbolism for transformation, intuition, or protection."
Uma = {Sea_magic, Spell_casting, "transformation into a", Cacelia}

Potion_brewing = "- is the process of mixing, boiling, or steeping ingredients to make\n a potion—a liquid dose or drink believed or intended to have magical, medicinal, or poisonous effects."
Spell_casting = " - Performing magic spells, often through spoken words, chants, or rituals to influence a person, object, or situation."
Fairy_magic = " - \"Fairy\" comes from Old/Anglo-French faerie, which originally meant \"enchantment\", \"witchcraft\", or \"the realm of mythical beings\" before coming to refer to an individual creature."
Mal = [Fairy_magic, Spell_casting, Potion_brewing]
descendants = {"Daughter of Maleficent & Hades":Mal, "Daughter of Ursula":Uma, "Son of Jafar":Jay, "Lord of the Underworld": Hades, "Mistress of All Evil": Maleficent}

print(descendants["Daughter of Maleficent & Hades"][1])
print(descendants["Daughter of Maleficent & Hades"][1])

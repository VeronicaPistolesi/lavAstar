# CUSTOM FULLY OBSERVABLE ENVIRONMENTS CREATED WITH LEVEL EDITOR

# LEVEL 1
des_file_static_lv1 = """
MAZE: "mylevel", ' '
FLAGS: premapped
GEOMETRY:left,top
MAP
|||||||||||||||
|...L.........|
|.....L.....L.|
|L............|
|.L.......L...|
|...LL..L.....|
|.L.........L.|
|....L..L.....|
|.L........L.L|
|..L..........|
|..L....L...LL|
|....L........|
|.L.......L...|
|.....L.......|
|||||||||||||||
ENDMAP
STAIR:(13, 13),down
BRANCH: (1,1,1,1),(2,2,2,2)
REGION: (0,0,20,80), lit, "ordinary"
"""

# LEVEL 2
des_file_static_lv2 = """
MAZE: "mylevel", ' '
FLAGS: premapped
GEOMETRY:left,top
MAP
|||||||||||||||
|...L...L.L...|
|.....L.....L.|
|L..L.L.......|
|.L.......L..L|
|...LL..L.....|
|..L........L.|
|..L.L...LL...|
|.L..L..LL.L..|
|..L........L.|
|L..L...L...L.|
|....L......L.|
|.L.......L..L|
|.....LL...L..|
|||||||||||||||
ENDMAP
STAIR:(13, 13),down
BRANCH: (1,1,1,1),(2,2,2,2)
REGION: (0,0,20,80), lit, "ordinary"
"""


# LEVEL 3
des_file_static_lv3 = """
MAZE: "mylevel", ' '
FLAGS: premapped
GEOMETRY:left,top
MAP
|||||||||||||||         
|.I.L...L.L...|
|I....L.....L.|
|L..LIL.......|
|.L.......L.IL|
|...LL..L.....|
|IIL.....II.L.|
|..L.L.I.LL...|
|.L..L..LL.L.I|
|..L.II.....L.|
|L..L...L.IIL.|
|I...LI.....L.|
|.L..III..L..L|
|.....LL...L..|
|||||||||||||||
ENDMAP
STAIR:(13, 13),down
BRANCH: (1,1,1,1),(2,2,2,2)
REGION: (0,0,20,80), lit, "ordinary"
"""


#-------------------------------------------
# Dynamic (monster)

# LEVEL 4
des_file_static_lv4 = """
MAZE: "mylevel", ' '
FLAGS: premapped
GEOMETRY:left,top
MAP
|||||||||||||||         
|.I.L...L.L...|
|I....L.....L.|
|L..LIL.......|
|.L.......L.IL|
|...LL..L.....|
|IIL.....II.L.|
|..L.L.I.LL...|
|.L..L..LL.L.I|
|..L.II.....L.|
|L..L...L.IIL.|
|I...LI.....L.|
|.L..III..L..L|
|.....LL...L..|
|||||||||||||||
ENDMAP
STAIR:(13, 13),down
BRANCH: (1,1,1,1),(2,2,2,2)
MONSTER: ('a', "giant beetle"), random, hostile
REGION: (0,0,20,80), lit, "ordinary"
"""

# LEVEL 5
des_file_static_lv5 = """
MAZE: "mylevel", ' '
FLAGS: premapped
GEOMETRY:left,top
MAP
|||||||||||||||         
|.I.L...L.L...|
|I....L.....L.|
|L..LIL.......|
|.L.......L.IL|
|...LL..L.....|
|IIL.....II.L.|
|..L.L.I.LL...|
|.L..L..LL.L.I|
|..L.II.....L.|
|L..L...L.IIL.|
|I...LI.....L.|
|.L..III..L..L|
|.....LL...L..|
|||||||||||||||
ENDMAP
STAIR:(13, 13),down
BRANCH: (1,1,1,1),(2,2,2,2)
OBJECT: ('(',"skeleton key"), (11, 3), blessed, 0, name:"The Master Key of Thievery"
MONSTER: (':', "crocodile"), random, hostile
REGION: (0,0,20,80), lit, "ordinary"
"""
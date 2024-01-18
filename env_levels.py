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

# LEVEL 4_1  no dead end - rat
des_file_static_lv4_1 = """
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
MONSTER: ('r', "sewer rat"), (6,6), hostile
REGION: (0,0,20,80), lit, "ordinary"
"""

# LEVEL 4_2  no dead end - beetle
des_file_static_lv4_2 = """
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
MONSTER: ('a', "giant beetle"), (6,6), hostile
REGION: (0,0,20,80), lit, "ordinary"
"""

# LEVEL 5.1 # rat w/ dead_end - difficult
des_file_static_lv5_1 = """
MAZE: "mylevel", ' '
FLAGS: premapped
GEOMETRY:left,top
MAP
|||||||||||||||         
|.I.L...L.L...|
|I....L.....L.|
|L..LIL.......|
|.L.......L.IL|
|...LL..L.IL..|
|IIL.....IL.L.|
|..L.L.I.LL.L.|
|.L..L..LL.LLI|
|..L.II.....L.|
|L..L...LLLLL.|
|I...LI.....L.|
|.L..III..L..L|
|.....LL...L..|
|||||||||||||||
ENDMAP
STAIR:(13, 13),down
BRANCH: (1,1,1,1),(2,2,2,2)
MONSTER: ('r', "sewer rat"), (6,6), hostile
REGION: (0,0,20,80), lit, "ordinary"
"""

# LEVEL 5.2 # beetle w/ dead_end - difficult
des_file_static_lv5_2 = """
MAZE: "mylevel", ' '
FLAGS: premapped
GEOMETRY:left,top
MAP
|||||||||||||||         
|.I.L...L.L...|
|I....L.....L.|
|L..LIL.......|
|.L.......L.IL|
|...LL..L.IL..|
|IIL.....IL.L.|
|..L.L.I.LL.L.|
|.L..L..LL.LLI|
|..L.II.....L.|
|L..L...LLLLL.|
|I...LI.....L.|
|.L..III..L..L|
|.....LL...L..|
|||||||||||||||
ENDMAP
STAIR:(13, 13),down
BRANCH: (1,1,1,1),(2,2,2,2)
MONSTER: ('a', "giant beetle"), (6,6), hostile
REGION: (0,0,20,80), lit, "ordinary"
"""

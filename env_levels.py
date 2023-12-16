# CUSTOM FULLY OBSERVABLE ENVIRONMENTS CREATED WITH LEVEL EDITOR

#LEVEL 1
des_file_static_lv1 = """
MAZE: "mylevel", ' '
FLAGS: premapped
GEOMETRY:left,top
MAP
|||||||||||||||
|.I.L.........|
|I....L.....L.|
|L...I........|
|.L.......L..I|
|...LL..L.....|
|.I.........L.|
|....L..I.....|
|.L........L.I|
|..L..........|
|..I....L...II|
|....L..I.I...|
|.L.......L...|
|.....I.......|
|||||||||||||||
ENDMAP
STAIR:(13, 13),down
BRANCH: (1,1,1,1),(2,2,2,2)
REGION: (0,0,20,80), lit, "ordinary"
"""
#LEVEL 2
des_file_static_lv2 = """
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
|..L........L.|
|....L........|
|.L........L..|
|..L........L.|
|.......L...L.|
|....L......L.|
|.L.......L..L|
|..........L..|
|||||||||||||||
ENDMAP
STAIR:(13, 13),down
BRANCH: (1,1,1,1),(2,2,2,2)
REGION: (0,0,20,80), lit, "ordinary"
"""

#LEVEL 3
des_file_static_lv3 = """
MAZE: "mylevel", ' '
FLAGS: premapped
GEOMETRY:left,top
MAP
|||||||||||||||
|...L....LL...|
|..LL.L.....L.|
|L.....LLL....|
|.L..L....L...|
|...LL.L......|
|L......LL..L.|
|..L.L........|
|.L....LL...L.|
|..L..L...LL..|
|LL.....L..L..|
|...LLL......L|
|.L.....LL...L|
|...LL.....L..|
|||||||||||||||
ENDMAP
STAIR:(13, 13),down
BRANCH: (1,1,1,1),(2,2,2,2)
REGION: (0,0,20,80), lit, "ordinary"
"""

#------------------------------------------------
#LEVEL 3
des_file_static_lv3 = """
MAZE: "mylevel", ' '
FLAGS: premapped
GEOMETRY:left,top
MAP
|||||||||||||||
|...L....LL...|
|..LL.L.....L.|
|L.....LLL....|
|.L..L....L...|
|...LL.L......|
|L......LL..L.|
|..L.L........|
|.L....LL...L.|
|..L..L...LL..|
|LL.....L..L..|
|...LLL......L|
|.L.....LL...L|
|...LL.....L..|
|||||||||||||||
ENDMAP
STAIR:(13, 13),down
BRANCH: (1,1,1,1),(2,2,2,2)
REGION: (0,0,20,80), lit, "ordinary"
"""

#LEVEL 4 - DYNAMIC
des_file_static_lv4 = """
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
|...........L.|
|....L........|
|.L........L..|
|..L..........|
|.......L.....|
|....L........|
|.L.......L...|
|.............|
|||||||||||||||
ENDMAP
STAIR:(13, 13),down
BRANCH: (1,1,1,1),(2,2,2,2)
MONSTER: ('H', "giant"), random, hostile
REGION: (0,0,20,80), lit, "ordinary"
"""
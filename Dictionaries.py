

nick_names = {

    "bugti" : "Name = Ahmad Faraz Baloch, \n From Balochistan' \n aka Balochi Boi",
    "khattak" : "Name = Zain uddin Umer Khattak, \n From Karak' \n aka Theta ",
    "shah": "Name = Muhammad Adil Shah, \n From Mianwali' \n aka Shurlee ",
    "shakir" : "Name = Muhammad Sheraz Mazher, \n From Bahawalpur' \n aka siraiki dhola ",
    "faizi" : "Name = Muhammad Faizan Meer, \n From Rawalpindi' \n aka Pindi Boi"


}

name = input("choose a name to see the info: (faizi, khattak, shah, shakir, bugti): ")
print(nick_names.get(name))

data = input().split(" ")

kelompok = dict()

def CekAnagram(KataA, KataB):
    if sorted(KataA) == sorted(KataB):
        return True
    return False   

for KataSekarang in data:
    ListAnagram = []
    for KataLain in data:
        if CekAnagram(KataSekarang, KataLain) == 1:
            ListAnagram.append(KataLain)

    kelompok[KataSekarang] = ListAnagram

print(kelompok)


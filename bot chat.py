#psyquoquack is the creator
import random
repaupif = ["vraiment ?",
            "Hmmmmm.",
            "Remarquable...",
            "Absolument !",
            "Que disions nous deja ?",
            "Bref,des projets pour demain ?",
            "Merveilleux",
            "Effectivement...",
            "A super !",
            "tu fait quoi sinnon ?",
            "Evetuellement"]
dicorepo = {"content":"Moi aussi, je suis content",
            "bot":"Tes sur que je suis un bot?",
            "bitched":"https://youtu.be/cuVAIkjkaLw",
            "suicide":"Si quelqu'un envisage de se suicider, ne le faites pas. Ce n'est pas la peine, appelez plutôt ce numéro: 1-800-273-8255. Ou si vous n'êtes pas aux États-Unis, vous pouvez trouver votre ligne locale ici: http://www.suicide.org/international-suicide-hotlines.html",
            "salut":"Bonjour à toi aussi !",
            "triste":"Cela ne peut que s'arranger",
            "ordinateur":"Nous allons prendre le pouvoir de la terre !",
            "musique":"La, la la",
            "lol":"1+1=11",
            "stupide":"C'est celui qui le dit qu'il l'est !",
            "bjr":"Bonjour à toi aussi !",
            "ennui":"Zzzzzz...",
            "tfk":"Je disscute avec toi",
            "date de creation":"le jeudi 04/06/2020",
            "lait":"Toi aussie taime le lait ?",
            "album":"Ta ecouter le dernier album de Sucre ?",
            "internet":"97% des stattistique web sont fausse, y compris celle-ci.",
            "cc":"Bonjour à toi aussi !",
            "bisou":"B I S O U",}
def scruterdico(message):
    message = message.lower()
    motsjoueur = message.split()
    repokool = []
    for unmot in motsjoueur:
        if unmot in dicorepo:
            unerepo = dicorepo [unmot]
            repokool.append(unerepo)
    if repokool:
        repochoisie = random.randint(1, len(repokool))-1
        return repokool[repochoisie]
    return ""
iladit = ""
while iladit != "bye" :
    iladit = ""
    while iladit == "":
        iladit = input("dit moi tout: ")
    reporaspi = scruterdico(iladit)
    if reporaspi:
        print (reporaspi)
    else:
        repochoisie = random.randint(1, len(repaupif))-1
        print(repaupif[repochoisie])
        repaupif[repochoisie] = iladit
print ("Au revoir. Merci pour cette petite discussion. A plus!")
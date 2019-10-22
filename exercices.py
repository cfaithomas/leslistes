

#EX1*************************************
listeami=["Diego","Remi","Adam"]
i=0
while(i<len(listeami)):
    print("Salut",listeami[i],"!")
    i+=1

#************************Les invités****************************
listeinvités=["Tom","Elsa","Daniel"]
i=0
print(listeinvités[-1],"ne peut pas venir") #Affiche l'invité qui ne peut pas venir
listeinvités[2]="Remi" #Remplace Daniel par Remi
#***********************Plus d'invités**************************/
print("J'ai trouvé une plus grande table à manger")
listeinvités.insert(-1,"Emilie")
listeinvités.insert(2,"Pierre")
listeinvités.append("Julie")
#**********************La table n'a pas été livrée**************/
print("je ne peux inviter que deux personnes")
cpt=0
while(cpt<4):
    invitesupp=listeinvités.pop()
    print(invitesupp,"Je regrette de pas pouvoir t'inviter")
    cpt+=1
cpt2=0;
#********************message invités restants*****************/
while(cpt2<len(listeinvités)):
    print(listeinvités[cpt2],"Tu es toujours invité")
    cpt2+=1

#***********Affiche la liste des invités**********************

while(i<len(listeinvités)):
    print(listeinvités[i]+", je t'invites à diner demain")
    i+=1
#****************suppression des invités************************
i=len(listeinvités)-1
while i>=0:
    del listeinvités[i]
    i-=1

print(listeinvités);  #vérification





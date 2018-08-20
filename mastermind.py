# -*- coding: utf-8 -*-

def generate_sequence():
  from random import randint
  sequence = []
  for i in range(4):
    number = randint(1,6)
    sequence.append(number)
  return sequence

def take_user_input():
  user_sequence =[]
  number = raw_input("")
  for i in number:
    user_sequence.append(i)
  return user_sequence

def check_accuracy(sequence, user_sequence):
  count =0
  for a, b in zip(sequence, user_sequence):
    if a==int(b):
      print "X",
      count+=1
      user_sequence.remove(b)
      sequence.remove(a)
  if count==4:
    print u"\n \n Kod złamany",
    return 1   
  for i in user_sequence:
    condition=True
    index=0
    while condition:
      if int(i)==sequence[index]:
        print "*",
        del(sequence[index])
        condition=False
      else:
        index+=1
        if index==len(sequence):
          condition=False
  print ("o "*len(sequence)) 

def play_game():
  sequence = generate_sequence()
  count=1
  print u"\n Podaj 4 cyfry od 1 do 6 i potwierdź enterem: "
  while count<=10:
    print str(count)+": ",
    wrong_data=True
    while wrong_data:
      user_sequence = take_user_input()
      if_wrong=0
      if len(user_sequence)!=4:
        print u"Podano więcej lub mniej niż 4 cyfry! Spróbuj ponownie:"
        if_wrong+=1
      else: 
        for i in range(4):
          if int(user_sequence[i])<1 or int(user_sequence[i])>6:
            print u"Przynajmniej jedna z twoich cyfr jest za duża lub za mała! Spróbuj ponownie:"
            if_wrong+=1
            break
      if if_wrong==0:
        wrong_data=False
    print "           ",
    print " ".join(user_sequence),
    print "   ",      
    sequence_copy=[]
    for i in range(4):
      sequence_copy.append(sequence[i])  
    if check_accuracy(sequence_copy, user_sequence)==1:
      if count==1:
        print "w "+str(count)+ u". próbie!"
      else:
        print "w "+str(count)+ u". próbach!"
      return count
    count+=1
    if count==11:
      print u"Ups, nie udało się! Prawidłowa odpowiedź to: "+str(sequence)+"\n"
      return count

def two_player(names):
  scores=[0,0]  
  round_no=10
  while round_no>6 or round_no<1:
    round_no=int(raw_input("\nPodajcie liczbę rund, jaką chcecie rozegrać (najwyżej 6): "))
    if round_no>6:
      print u"\nChyba chcecie grać do jutra! ",
    elif round_no<1:
      print u"\nTo chcecie grać, czy nie?",
  for i in range(int(round_no)):
    print "\n\nRUNDA", (i+1), "/", round_no
    for j in range(2):
      print "\n"+names[j]+", twoja kolej:"
      count=play_game()
      if j==0:
        scores[1]+=count
      elif j==1:
        scores[0]+=count     
  print "\nWYNIKI:"
  for i in range(2):
    print "\n"+names[i]+": "+str(scores[i])
  if scores[0]>scores[1]:
    print "\nGratulacje, "+ names[0]+"!"
  elif scores[0]<scores[1]:
    print "\nGratulacje, "+ names[1]+"!"
  else:
    print u"\nGra zakończyła się remisem!"

print u"MASTERMIND - INSTRUKCJA \nTwoim celem jest złamanie kodu składającego się z czterech cyfr \no wartościach od 1 do 6 w najwyżej dziesięciu próbach. \nUWAGA: Cyfry w sekwencji mogą się powtarzać. \nPo każdej próbie otrzymasz podpowiedź w postaci symbolu (jeden symbol \ndla każdej cyfry kodu): \nX - któraś z wpisanych cyfr jest prawidłowa i znajduje się na właściwym miejscu,\n* - któraś z cyfr jest prawidłowa, lecz znajduje się na niewłaściwym miejscu,\no - którejś z cyfr nie ma w sekwencji.\n"

#choose game mode
wrong_answer=True
while wrong_answer:
  mode=raw_input("Wybierz 1 aby zagrać w trybie jednego gracza,\nlub wybierz 2 aby zagrać we dwójkę: ")
  if mode=="1":
    wrong_answer=False
  elif mode=="2":
    print u"\nW wersji dla dwóch graczy każdy gracz otrzymuje tyle punktów, \nile prób potrzebował jego przeciwnik do odgadnięcia kodu. \nJeśli kod nie zostanie złamany, przyznawany mu jest dodatkowy punkt. \nZwycięzcą jest gracz, który zdobył więcej punktów po ustalonej z góry \nliczbie rozegranych rund.\nW jednej rundzie każdy z graczy łamie kod jeden raz.\n"
    names=["",""]
    for i in range(2):
      names[i]=raw_input("\nImię gracza "+str(i+1)+": ")
      name_check=names[i].replace(" ", "")
      if not name_check:
        names[i]="GRACZ "+str(i+1)
    wrong_answer=False
  else:
    print "\nHmm, ile?...",

#game loop
best_score=11
answer="t"
while answer=="t"or answer=="T":
  if mode=="1":
    count=play_game()
    if count<best_score:
      best_score=count
      print u"\nTwój najlepszy wynik to:", best_score
    elif best_score==11:
      print u"\nNie udało ci się dotąd złamać kodu. Próbuj dalej!"
    else:
      print u"\nTwój najlepszy wynik to:", best_score
  elif mode=="2":
    two_player(names)
  mistake=True
  while mistake:
    answer = raw_input("\n Czy chcesz zagrać jeszcze raz? (t/n)")
    if answer!="t" and answer != "n" and answer!="T":
      print u"Wpisz t by kontynuować lub n by zakończyć"
    else: 
      mistake=False

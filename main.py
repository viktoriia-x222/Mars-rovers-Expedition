from random import randint
import random
print("""
=======================================
        MISSION EINES ROVERS
=======================================""")

name=input("Names des Rovers: ")
print("Welt ist von -100 bis 100")
x=int(input("Startposition x: "))
y=int(input("Startposition y: "))
if x>100 or x<-100 or y>100 or y<-100:
   print("Ungültig")
   exit()

print("Ein Scritt ist 5")
level=(input("Welche level möchten sie nehmen leicht/mittel oder schwierig?"))
if level=="leicht":
   energie=150
elif level== "mittel":
   energie=100
elif level=="schwierig":
   energie=70
else:
   print("Ungültige Auswahl")
   energie=90
print(energie)
x_ziel=int(input("Zielposition x: "))
y_ziel=int(input("Zielposition y: "))
if x_ziel>100 or x_ziel<-100 or y_ziel>100 or y_ziel<-100:
   print("Diese Eingabe ist nicht erlaubt. Die Mission wurde abgebrochen. ")
   exit()


print("\n=== Missionsziel ===")
print(f"Deine Mission ist es, das Ziel ({x_ziel}, {y_ziel}) zu erreichen.")
print("Du musst dabei deine Energie über 0 halten.")
print("Wenn deine Energie 0 erreicht, ist die Mission gescheitert.")
print(f"""
===== ROVER DATEN =====
Name: {name}
Energie: {energie}
Startposition:{x},{y}
Zielposition:{x_ziel},{y_ziel}
=======================
""")
print("3,2,1 Start🌌")

def move():
    global x,y, energie
    vector=input("Wohin wollen sie gehen,drücken w oder a oder s oder d: ").lower()

    if vector=="w":
      y+=5
    elif vector =="s":
      y-=5
    elif vector=="a":
      x-=5
    elif vector=="d":
      x+=5
    else:
      print("drücken sie bitee eine von adsw")
      return 
   
    print("Ein Schritt",x, y)
    energie-=1
    print("Energie",energie)

get_position_g={
  "s_x":10,
  "s_y":55
}
get_position_e={
  "s_x":60,
  "s_y":20
}
get_position_s={
  "s_x":10,
  "s_y":10
}


sachen=[{"was":"Grube",
  "position":get_position_g,
  "nachricht":"Der Rover ist in eine Grube gefahren☹️"},
{"was":"Energiequelle",
  "position":get_position_e,
  "nachricht":"Sie haben eine Enrgiequelle gefunden😁"},
  {"was":"Felsen",
    "position":get_position_s,
    "nachricht":"Der Rover ist gegen einen Felsen gefahren😔"}
]




while x!=x_ziel or y!=y_ziel:
    if energie <= 0:
        print("Energie leer! Mission gescheitert.")
        break
    move()
    if x==x_ziel and y==y_ziel:
        print("\n=======================================")
        print("        MISSION ABGESCHLOSSEN🏆")
        print("=======================================\n")

        print("📡 Missionsbericht des Rovers")

        print(f"Name der Mission: {name}")
        print(f"Zielposition: ({x_ziel}, {y_ziel})")
        print(f"Endposition: ({x}, {y})")
        print(f"Verbleibende Energie: {energie}")
      

        print("MISSION ERFOLGREICH ABGESCHLOSSEN 🚀")
        break

    if x==get_position_g["s_x"] and y==get_position_g["s_y"]:
      energie-=10
      print(sachen[0]["nachricht"])
      print(f"Jetz deine energie ist:{energie}")
    if x==get_position_e["s_x"] and y==get_position_e["s_y"]:
      energie+=30
      print(sachen[1]["nachricht"])
      print(f"Jetz deine energie ist:{energie}")
    if x==get_position_s["s_x"] and y==get_position_s["s_y"]:
      energie+=30
      print(sachen[2]["nachricht"])
      print(f"Jetz deine energie ist:{energie}")
    if random.randint(1,20)==1:
      energie-=30
      print("Ein Meteoritenschauer beginnt ☄️")
      print(f"Jetz deine energie ist:{energie}")
    if random.randint(1,15)==2:
      energie-=10
      print("Der Marsstaub klebt an den Rädern des Rovers.🔴")
      print(f"Jetz deine energie ist:{energie}")


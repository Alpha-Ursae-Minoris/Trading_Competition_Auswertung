# Trading_Competition_Auswertung

## Installation Windows

1. python3 von der offiziellen Python Website oder aus Windows app store installieren (empfohlene version 3.9.10)
- version in cmd prompt überprüfen 

  ```python3 --version```

2. numpy and pandas installation mittels Command Prompt
- jeweils enter taste nach den Command prompts

	```pip3 install python```
	
	```pip3 install numpy```


## Erstinstallation und Update des Codes
1. Zip datei von github herunterladen(grüner code button -> Download Zip). 
2. In Downloads zip Ordner finden und mit rechtslick "extract all" auswählen, such eine speicher stelle aus (empfohlen C:\Users\(dein user Name)\Desktop)

In der github datei sind bereits zwei testdatein enthalten, alle zukunfüntigen Downloads der Marketwatch (holding) files sollten im Trading_Competition_Auswertung-main Ordner abgespeichert werden.(Ansonsten muss beim upload anstatt dem filename auch der filepath angegeben werden)

***Diese Schritte müssen für jede Version erneut ausgeführt werden (zuvor den alten Ordner löschen)***


## Ausführung Windows

1. Öffne Command Prompt 

2. Wechsel in den Code Ordner
- tippe cd Leerzeichen und drag und droppe den Trading_Competition_Auswertung-main Ordner in die Command Prompt, das sollte automatisch den Path eingeben

- Alternative: cd Leerzeichen C:\Users\(dein user Name)\Desktop\Trading_Competition_Auswertung-main

- Sollte dann so aussehen:  

  	```cd C:\Users\(dein user Name)\Desktop\Trading_Competition_Auswertung-main```

3. ***Beginne immer mit dem Upload deiner Holdings Datei***:
- Ausführung von upload

	```python3 Auswertung.py upload```
	
- Eingabe der Holdings Datei (z.B. test.csv):

	```Enter filename: test.csv```

4. Danach einfach eines der commands aussuchen und folgendes eingeben:
- Code
  	```python3 Auswertung.py command```
  
  ***Hinweis: Derzeit wird immer nur ein Command akzeptiert(gerne auch mehrere ausprobieren) und für die liste der möglichen commands einfach irgendein wort als command eingeben***

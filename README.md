# CHAP_exercice

 Ist eine Client-/Server-Anwendung, mit der eine CHAP-basierte Authentifizierung zwischen zwei Rechnern über ein IP-basiertes Netzwerk erfolgen kann.
 
 

## Aufbau

Um das Projekt zu nutzen, musst du nur diese repo zu deinem Geräte clonen.

```bash
# mit SSH 
git@github.com:gitfarah/CHAP_exercice.git

# mit HTTPS
https://github.com/gitfarah/CHAP_exercice.git
```

## Technologie

In dem Projekt wird bestimmte Bibliotheken verwendet, um richtig zu funktionieren. Die Bibliotheken sind:
 ```python
 * from xmlrpc.server import SimpleXMLRPCServer     # bietet die Möglichkeit, einfache, eigenständige XML-RPC-Server zu erstellen.
 * SimpleXMLRPCRequestHandler     # Erstellen Sie eine neue Request-Handler-Instanz.
 * import random     # Implementiert Pseudozufallszahlengeneratoren für verschiedene Verteilungen
 * import hashlib     # Implementierung eines sicheren Hash- und Message Digest-Algorithmus
 * import xmlrpc.client     #Der Client kann Methoden mit Parametern auf einem Remote-Server aufrufen (der Server wird durch einen URI benannt) und strukturierte Daten zurückerhalten.
 ```
 
 ## Features
Der Benutzer can aus dem cleints Datein eine Methode "calculate()" aus dem Server aufrufen. Diese Methode berechnet zwei Zahlen mit (Addition, Subtraktion, Dividieren oder Multiplizieren)
```python
def calculate():
 # Take input from the user  
select = int(input("Select operations form add, sub, multi, div :")) 
  
number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 
  
if select == "add": 
    print(number_1, "+", number_2, "=", 
                    add(number_1, number_2)) 
  
elif select == "sub": 
    print(number_1, "-", number_2, "=", 
                    subtract(number_1, number_2)) 
  
elif select == "multi": 
    print(number_1, "*", number_2, "=", 
                    multiply(number_1, number_2)) 
  
elif select == "div": 
    print(number_1, "/", number_2, "=", 
                    divide(number_1, number_2)) 
else: 
    print("Invalid input") 
```
## Datein
Das Projekt besteht aus mehreren Dateien. Diese Dateien sind:
```bash
 server.py  # hier ist die Server Datei, wo die Client sich authentifizieren kann und wo das Calculate Methode aufgerufen wird.
 clientOne.py  # von dieser Datei kann ein Benutzer sich einlogen.
 cleintTwo.py  # zusätzliche Client Datei, um zu testen, ob mehrer Benutzer gleichzeitig mit dem Server verbinden können. 
 user.txt      # In diese Datei befindet sich die vorhandenen Kontos (username & password).
```


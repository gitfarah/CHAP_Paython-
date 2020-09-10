# CHAP_exercice

 Ist eine Client-/Server-Anwendung, mit der eine CHAP-basierte Authentifizierung zwischen zwei Rechnern über ein IP-basiertes Netzwerk erfolgen kann.
 
 

# Installation

Um das Projekt zu nutzen, musst du nur diese repo zu deinem Geräte clonen.

```bash
# mit SSH 
git@github.com:gitfarah/CHAP_exercice.git

# mit HTTPS
https://github.com/gitfarah/CHAP_exercice.git
```

## Technologie

In dem Projekt wird bestimmte Biblöthik verwendet, um richtig zu funktionieren. Die Biblöthike sind:
 ```python
 * from xmlrpc.server import SimpleXMLRPCServer     # bietet die Möglichkeit, einfache, eigenständige XML-RPC-Server zu erstellen.
 * SimpleXMLRPCRequestHandler     # Erstellen Sie eine neue Request-Handler-Instanz.
 * import random     # Implementiert Pseudozufallszahlengeneratoren für verschiedene Verteilungen
 * import hashlib     # Implementierung eines sicheren Hash- und Message Digest-Algorithmus
 * import xmlrpc.client     #Der Client kann Methoden mit Parametern auf einem Remote-Server aufrufen (der Server wird durch einen URI benannt) und strukturierte Daten zurückerhalten.
 ```
 
 ## Features
Der Client can in diesem Tool eine Methode "calculate()" aus dem Server aufrufen. Diese Methode ermöglicht zwei Zahlen zu(Addieren, subtrahieren, dividieren oder multiplizieren)
```python
def calculate():
 # Take input from the user  
select = int(input("Select operations form 1, 2, 3, 4 :")) 
  
number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 
  
if select == 1: 
    print(number_1, "+", number_2, "=", 
                    add(number_1, number_2)) 
  
elif select == 2: 
    print(number_1, "-", number_2, "=", 
                    subtract(number_1, number_2)) 
  
elif select == 3: 
    print(number_1, "*", number_2, "=", 
                    multiply(number_1, number_2)) 
  
elif select == 4: 
    print(number_1, "/", number_2, "=", 
                    divide(number_1, number_2)) 
else: 
    print("Invalid input") 
```


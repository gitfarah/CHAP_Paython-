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
> Unterschützte Python Version in diesem Projekt ist Python 3.8

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
Der Benutzer can aus dem Cleints Datein eine Methoden aus dem Server nach einem erfolgreichen login aufrufen. Diese Methode berechnet zwei Zahlen mit (Addition, Subtraktion, Dividieren oder Multiplizieren)
```python
# method that adds two numbers
def add(x, y, username) :

# method that substract a numbers from another
def subtract(x, y, username) :

# method that multiply two numbers
def multiply(x, y, username) :

# method that divide two numbers
def divide(x, y, username) :
```
## Datein
Das Projekt besteht aus mehreren Dateien. Diese Dateien sind:
```bash
 server.py  # hier ist die Server Datei, wo die Client sich authentifizieren kann und wo das Calculate Methode aufgerufen wird.
 clientOne.py  # von dieser Datei kann ein Benutzer sich einlogen.
 cleintTwo.py  # zusätzliche Client Datei, um zu testen, ob mehrer Benutzer gleichzeitig mit dem Server verbinden können. 
 user.txt      # In diese Datei befindet sich die vorhandenen Kontos mit(username & password).
```

## Aufruf & Verwendung 
Um das Projekt zu verwenden, starten Sie einfach die folgenden Dateien:
> 1- Starten Sie zuerst die Datei "server.py" auf Ihrer IDE

> 2- Nach erfolgreichem Start der Datei "server.py" werden entweder die Dateien "clientOne.py" oder "clientTwo.py" gestartet oder beide können auch gleichzeitig gestartet werden.

> 3- Implementierte Methoden in der Datei "server.py" werden automatisch aufgerufen, wenn der Benutzer den ausreichenden Benutzernamen und das Kennwort eingibt.


## License
[MIT](mr.omarfarah@gmail.com) 

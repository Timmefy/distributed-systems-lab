# Distributed Systems Lab - General Wiki

Willkommen im allgemeinen Wiki des **Distributed Systems Lab**-Projekts. Dieses Projekt demonstriert die Integration von Front-End- und Back-End-Technologien unter Verwendung von Angular, FastAPI, Docker und Docker-Compose. Im Folgenden findest du einen Überblick über die Projektstruktur, die verwendeten Technologien sowie Anweisungen zum Einrichten und Ausführen des Projekts.

## Inhaltsverzeichnis
1. [Projektübersicht](#projektübersicht)
2. [Verwendete Technologien](#verwendete-technologien)
3. [Projektstruktur](#projektstruktur)
4. [Einrichtungsanweisungen](#einrichtungsanweisungen)
5. [Ausführen des Projekts](#ausführen-des-projekts)
6. [Lizenz](#lizenz)

## Projektübersicht

Das **Distributed Systems Lab** ist ein umfassendes Projekt, das zeigt, wie ein verteiltes System mit modernen Webentwicklungstools und -frameworks aufgebaut werden kann. Das Projekt ist in zwei Hauptkomponenten unterteilt: die Front-End-Anwendung und der Back-End-API-Dienst. Diese Komponenten sind mit Docker containerisiert und werden mithilfe von Docker-Compose orchestriert, um eine einfache Bereitstellung und Verwaltung zu ermöglichen.

## Verwendete Technologien

### Front-End
- **Angular**: Eine Plattform zum Erstellen von Webanwendungen für mobile und Desktop-Geräte.

### Back-End
- **FastAPI**: Ein modernes, schnelles (High-Performance) Webframework zum Erstellen von APIs mit Python 3.7+ basierend auf standardmäßigen Python-Typ-Hinweisen.

### Containerisierung und Orchestrierung
- **Docker**: Eine Reihe von Platform-as-a-Service-Produkten, die Betriebssystemebenenvirtualisierung verwenden, um Software in Paketen bereitzustellen, die als Container bezeichnet werden.
- **Docker-Compose**: Ein Tool zum Definieren und Ausführen mehrerer Docker-Anwendungen.

## Projektstruktur

Die Projektverzeichnisstruktur ist wie folgt organisiert:

![image](https://github.com/Timmefy/distributed-systems-lab/assets/115172642/eda2044f-6fa8-4ca7-b063-a2db353d61ad)

### api/

Enthält die FastAPI-Anwendung.

- **app/**: Enthält den Anwendungscode der FastAPI-Anwendung.
  - `__init__.py`: Initialisierungsdatei für das Python-Modul.
  - `main.py`: Hauptdatei der FastAPI-Anwendung.
  - `models.py`: Datenbank- und Pydantic-Modelle.
- `Dockerfile`: Docker-Build-Datei für die FastAPI-Anwendung.
- `requirements.txt`: Abhängigkeiten der FastAPI-Anwendung.

### frontend/

Enthält die Angular-Anwendung.

- **todo-lab/**: Hauptverzeichnis der Angular-Anwendung.
  - `.angular/`: Angular-spezifische Konfigurationsdateien.
  - `.vscode/`: VS Code spezifische Konfigurationsdateien.
  - `node_modules/`: Abhängigkeiten der Angular-Anwendung.
  - `src/`: Quellcode der Angular-Anwendung.
  - `.editorconfig`: Editor-Konfiguration.
  - `.gitignore`: Git Ignore-Datei.
  - `angular.json`: Angular-Projektkonfiguration.
  - `package-lock.json`: Automatisch generierte Datei zur Verwaltung der genauen Versionen der Abhängigkeiten.
  - `package.json`: Abhängigkeitsmanagement und Skripte für das Projekt.
  - `tsconfig.app.json`: TypeScript-Konfigurationsdatei für die Angular-Anwendung.
  - `tsconfig.json`: TypeScript-Konfigurationsdatei.
  - `tsconfig.spec.json`: TypeScript-Konfigurationsdatei für Tests.
- `Dockerfile`: Docker-Build-Datei für die Angular-Anwendung.
- `README.md`: Dokumentation für die Front-End-Anwendung.

### docker-compose.yml
Konfigurationsdatei für Docker-Compose, um die Front-End- und Back-End-Container zu orchestrieren.


## Einrichtungsanweisungen
Befolge diese Schritte, um das Projekt auf deinem lokalen Rechner einzurichten:

1. **Repository klonen**

   ```bash
   git clone https://github.com/Timmefy/distributed-systems-lab.git
   ```
## Einrichtungsanweisungen

Stelle sicher, dass Docker und Docker-Compose installiert sind

- [Installiere Docker](https://docs.docker.com/get-docker/)
- [Installiere Docker-Compose](https://docs.docker.com/compose/install/)

Baue und starte die Container

```bash
docker-compose up -d
```

## Ausführen des Projekts

Sobald die Container gestartet sind, kannst du die Anwendung über die folgenden URLs aufrufen:

- **Front-End-Anwendung**: [http://localhost:4200](http://localhost:4200)
- **Back-End-API**: [http://localhost:8000](http://localhost:8000)

## Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert.

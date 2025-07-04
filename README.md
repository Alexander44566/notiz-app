# Notiz-App

### 📝 Beschreibung

Eine moderne Notiz-Anwendung mit Dark Mode Theme, entwickelt mit PySide6 und SQLite. Die App bietet eine intuitive Benutzeroberfläche mit geteilter Ansicht - Notizenliste links, Editor rechts.

### ✨ Features

- **🌙 Dark Mode Interface**: Schöne dunkle Benutzeroberfläche
- **📝 Notizenverwaltung**: Erstellen, bearbeiten und löschen von Notizen
- **💾 Automatisches Speichern**: Änderungen werden alle 3 Sekunden gespeichert
- **🗄️ SQLite Datenbank**: Lokale Speicherung aller Notizen
- **🔄 Geteilte Ansicht**: Notizenliste links, Editor rechts
- **🎯 Intuitive Bedienung**: Einfache und benutzerfreundliche Oberfläche

### 🛠️ Installation

#### Voraussetzungen
- Python 3.7 oder höher
- Git

#### Schritt-für-Schritt Anleitung

1. **Repository klonen**
   ```bash
   git clone https://github.com/Alexander44566/notiz-app.git
   cd notiz-app
   ```

2. **Virtual Environment erstellen**
   ```bash
   python -m venv .venv
   ```

3. **Virtual Environment aktivieren**
   
   **Windows:**
   ```bash
   .venv\Scripts\activate
   ```
   
   **Mac/Linux:**
   ```bash
   source .venv/bin/activate
   ```

4. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

5. **App starten**
   ```bash
   python main.py
   ```

### 🎮 Bedienung

- **Neue Notiz**: Klicken Sie auf "Neue Notiz" und geben Sie einen Titel ein
- **Notiz öffnen**: Klicken Sie auf eine Notiz in der Liste links
- **Notiz löschen**: Wählen Sie eine Notiz aus und klicken Sie auf "Löschen"
- **Bearbeiten**: Ändern Sie Titel und Inhalt im rechten Editor
- **Automatisches Speichern**: Ihre Änderungen werden automatisch gespeichert

### 🔧 Eigene .exe erstellen (Optional)

Falls Sie eine eigenständige .exe Datei erstellen möchten:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "Notiz-App" main.py
```

Die .exe Datei befindet sich dann im `dist/` Ordner.

### 🗄️ Datenbank

Die Notizen werden in einer lokalen SQLite-Datenbank (`notizen.db`) gespeichert, die automatisch beim ersten Start erstellt wird.

### 🔒 Sicherheit & Datenschutz

Diese Anwendung speichert **ausschließlich lokal** auf Ihrem Gerät. Es findet **keine Datenübertragung** über das Internet oder an Dritte statt.  
Die Nutzung erfolgt auf eigene Verantwortung. Für Datenverlust oder Schäden wird keine Haftung übernommen.

### 📋 Systemanforderungen

- Python 3.7+
- PySide6
- SQLite3 (im Python Standard enthalten)
- Windows, macOS oder Linux

### 🐛 Fehlerbehebung

**Problem: "python" wird nicht erkannt**
- Stellen Sie sicher, dass Python installiert ist und im PATH steht
- Versuchen Sie `python3` statt `python`

**Problem: Import-Fehler**
- Stellen Sie sicher, dass das Virtual Environment aktiviert ist
- Installieren Sie die Abhängigkeiten erneut: `pip install -r requirements.txt`

### 📄 Lizenz

[MIT License](LICENSE)

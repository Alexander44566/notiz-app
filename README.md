# Notiz-App / Notes App

[🇩🇪 Deutsch](#deutsch) | [🇺🇸 English](#english)

---

## Deutsch

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

MIT License

---

## English

### 📝 Description

A modern note-taking application with Dark Mode theme, built with PySide6 and SQLite. The app provides an intuitive user interface with split view - notes list on the left, editor on the right.

### ✨ Features

- **🌙 Dark Mode Interface**: Beautiful dark user interface
- **📝 Note Management**: Create, edit and delete notes
- **💾 Auto-Save**: Changes are automatically saved every 3 seconds
- **🗄️ SQLite Database**: Local storage of all notes
- **🔄 Split View**: Notes list on left, editor on right
- **🎯 Intuitive Operation**: Simple and user-friendly interface

### 🛠️ Installation

#### Prerequisites
- Python 3.7 or higher
- Git

#### Step-by-Step Guide

1. **Clone the repository**
   ```bash
   git clone https://github.com/Alexander44566/notiz-app.git
   cd notiz-app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   
   **Windows:**
   ```bash
   .venv\Scripts\activate
   ```
   
   **Mac/Linux:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Start the app**
   ```bash
   python main.py
   ```

### 🎮 Usage

- **New Note**: Click "Neue Notiz" and enter a title
- **Open Note**: Click on a note in the left list
- **Delete Note**: Select a note and click "Löschen"
- **Edit**: Change title and content in the right editor
- **Auto-Save**: Your changes are automatically saved

### 🔧 Create your own .exe (Optional)

If you want to create a standalone .exe file:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "Notiz-App" main.py
```

The .exe file will be located in the `dist/` folder.

### 🗄️ Database

Notes are stored in a local SQLite database (`notizen.db`) that is automatically created on first start.

### 📋 System Requirements

- Python 3.7+
- PySide6
- SQLite3 (included in Python standard library)
- Windows, macOS or Linux

### 🐛 Troubleshooting

**Problem: "python" is not recognized**
- Make sure Python is installed and in PATH
- Try `python3` instead of `python`

**Problem: Import errors**
- Make sure the virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

### 📄 License

MIT License
- **Geteilte Ansicht**: Notizenliste links, Editor rechts
- **Intuitive Bedienung**: Einfache und benutzerfreundliche Oberfläche

## Installation

1. Stellen Sie sicher, dass Python 3.7+ installiert ist
2. Installieren Sie die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```

## Verwendung

Starten Sie die Anwendung mit:
```bash
python main.py
```

### Bedienung

- **Neue Notiz**: Klicken Sie auf "Neue Notiz" und geben Sie einen Titel ein
- **Notiz öffnen**: Klicken Sie auf eine Notiz in der Liste links
- **Notiz löschen**: Wählen Sie eine Notiz aus und klicken Sie auf "Löschen"
- **Bearbeiten**: Ändern Sie Titel und Inhalt im rechten Editor
- **Automatisches Speichern**: Ihre Änderungen werden automatisch gespeichert

## Datenbank

Die Notizen werden in einer lokalen SQLite-Datenbank (`notizen.db`) gespeichert, die automatisch beim ersten Start erstellt wird.

## Systemanforderungen

- Python 3.7+
- PySide6
- SQLite3 (im Python Standard enthalten)

## Lizenz

MIT License

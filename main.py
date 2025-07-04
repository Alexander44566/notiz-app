#!/usr/bin/env python3
"""
Notiz-App mit PySide6 und SQLite
Eine einfache Notiz-Anwendung mit Dark Mode Theme
"""

import sys
import sqlite3
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QListWidget, QTextEdit, QPushButton, 
                              QLabel, QMessageBox, QInputDialog, QListWidgetItem,
                              QSplitter, QFrame)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont


class NotizApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notiz-App")
        self.setGeometry(100, 100, 1200, 800)
        
        # Datenbank initialisieren
        self.init_database()
        
        # UI erstellen
        self.init_ui()
        
        # Dark Mode anwenden
        self.apply_dark_theme()
        
        # Notizen laden
        self.load_notes()
        
        # Auto-Save Timer
        self.auto_save_timer = QTimer()
        self.auto_save_timer.timeout.connect(self.auto_save_current_note)
        self.auto_save_timer.start(3000)  # Alle 3 Sekunden speichern
        
    def init_database(self):
        """SQLite Datenbank initialisieren"""
        self.conn = sqlite3.connect('notizen.db')
        self.cursor = self.conn.cursor()
        
        # Tabelle erstellen falls nicht vorhanden
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS notizen (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titel TEXT NOT NULL,
                inhalt TEXT,
                erstellt DATETIME DEFAULT CURRENT_TIMESTAMP,
                geaendert DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
        
    def init_ui(self):
        """Benutzeroberfläche erstellen"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Hauptlayout (horizontal)
        main_layout = QHBoxLayout(central_widget)
        
        # Splitter für die zwei Bereiche
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)
        
        # Linker Bereich (Notizenliste)
        left_frame = QFrame()
        left_frame.setFrameStyle(QFrame.StyledPanel)
        left_frame.setMinimumWidth(300)
        left_frame.setMaximumWidth(400)
        
        left_layout = QVBoxLayout(left_frame)
        
        # Titel für Notizenliste
        notes_label = QLabel("Notizen")
        notes_label.setFont(QFont("Arial", 14, QFont.Bold))
        left_layout.addWidget(notes_label)
        
        # Buttons für Notizen verwalten
        button_layout = QHBoxLayout()
        
        self.new_note_btn = QPushButton("Neue Notiz")
        self.new_note_btn.clicked.connect(self.new_note)
        button_layout.addWidget(self.new_note_btn)
        
        self.delete_note_btn = QPushButton("Löschen")
        self.delete_note_btn.clicked.connect(self.delete_note)
        self.delete_note_btn.setEnabled(False)
        button_layout.addWidget(self.delete_note_btn)
        
        left_layout.addLayout(button_layout)
        
        # Notizenliste
        self.notes_list = QListWidget()
        self.notes_list.itemClicked.connect(self.load_selected_note)
        self.notes_list.itemSelectionChanged.connect(self.on_selection_changed)
        left_layout.addWidget(self.notes_list)
        
        # Rechter Bereich (Editor)
        right_frame = QFrame()
        right_frame.setFrameStyle(QFrame.StyledPanel)
        
        right_layout = QVBoxLayout(right_frame)
        
        # Editor-Titel
        editor_label = QLabel("Editor")
        editor_label.setFont(QFont("Arial", 14, QFont.Bold))
        right_layout.addWidget(editor_label)
        
        # Notiz-Titel Editor
        self.title_edit = QTextEdit()
        self.title_edit.setMaximumHeight(50)
        self.title_edit.setPlaceholderText("Titel der Notiz...")
        self.title_edit.setFont(QFont("Arial", 12, QFont.Bold))
        self.title_edit.textChanged.connect(self.on_title_changed)
        right_layout.addWidget(self.title_edit)
        
        # Haupteditor für Notizinhalt
        self.content_edit = QTextEdit()
        self.content_edit.setPlaceholderText("Hier können Sie Ihre Notiz schreiben...")
        self.content_edit.setFont(QFont("Arial", 11))
        self.content_edit.textChanged.connect(self.on_content_changed)
        right_layout.addWidget(self.content_edit)
        
        # Status-Label
        self.status_label = QLabel("Bereit")
        self.status_label.setAlignment(Qt.AlignRight)
        right_layout.addWidget(self.status_label)
        
        # Splitter konfigurieren
        splitter.addWidget(left_frame)
        splitter.addWidget(right_frame)
        splitter.setStretchFactor(0, 0)  # Linker Bereich nicht stretchbar
        splitter.setStretchFactor(1, 1)  # Rechter Bereich stretchbar
        
        # Variablen für aktuelle Notiz
        self.current_note_id = None
        self.is_editing = False
        
    def apply_dark_theme(self):
        """Dark Mode Theme anwenden"""
        dark_style = """
        QMainWindow {
            background-color: #2b2b2b;
            color: #ffffff;
        }
        
        QWidget {
            background-color: #2b2b2b;
            color: #ffffff;
        }
        
        QFrame {
            background-color: #353535;
            border: 1px solid #555555;
            border-radius: 5px;
        }
        
        QListWidget {
            background-color: #3c3c3c;
            border: 1px solid #555555;
            border-radius: 5px;
            color: #ffffff;
            selection-background-color: #4a90e2;
        }
        
        QListWidget::item {
            padding: 8px;
            border-bottom: 1px solid #555555;
        }
        
        QListWidget::item:selected {
            background-color: #4a90e2;
            color: #ffffff;
        }
        
        QListWidget::item:hover {
            background-color: #4a4a4a;
        }
        
        QTextEdit {
            background-color: #3c3c3c;
            border: 1px solid #555555;
            border-radius: 5px;
            color: #ffffff;
            selection-background-color: #4a90e2;
        }
        
        QPushButton {
            background-color: #4a90e2;
            border: none;
            border-radius: 5px;
            color: #ffffff;
            padding: 8px 15px;
            font-weight: bold;
        }
        
        QPushButton:hover {
            background-color: #357abd;
        }
        
        QPushButton:pressed {
            background-color: #2968a3;
        }
        
        QPushButton:disabled {
            background-color: #666666;
            color: #999999;
        }
        
        QLabel {
            color: #ffffff;
        }
        
        QSplitter::handle {
            background-color: #555555;
        }
        
        QSplitter::handle:horizontal {
            width: 3px;
        }
        """
        
        self.setStyleSheet(dark_style)
        
    def load_notes(self):
        """Alle Notizen aus der Datenbank laden"""
        self.notes_list.clear()
        
        self.cursor.execute('''
            SELECT id, titel, geaendert FROM notizen 
            ORDER BY geaendert DESC
        ''')
        
        notes = self.cursor.fetchall()
        
        for note_id, title, modified in notes:
            item = QListWidgetItem(f"{title}")
            item.setData(Qt.UserRole, note_id)
            # Datum als Tooltip anzeigen
            item.setToolTip(f"Geändert: {modified}")
            self.notes_list.addItem(item)
            
    def new_note(self):
        """Neue Notiz erstellen"""
        title, ok = QInputDialog.getText(self, 'Neue Notiz', 'Titel der neuen Notiz:')
        
        if ok and title.strip():
            # Notiz in Datenbank erstellen
            self.cursor.execute('''
                INSERT INTO notizen (titel, inhalt) 
                VALUES (?, ?)
            ''', (title.strip(), ''))
            
            note_id = self.cursor.lastrowid
            self.conn.commit()
            
            # UI aktualisieren
            self.load_notes()
            
            # Neue Notiz auswählen
            for i in range(self.notes_list.count()):
                item = self.notes_list.item(i)
                if item.data(Qt.UserRole) == note_id:
                    self.notes_list.setCurrentItem(item)
                    self.load_selected_note()
                    break
                    
            self.status_label.setText("Neue Notiz erstellt")
            
    def delete_note(self):
        """Ausgewählte Notiz löschen"""
        current_item = self.notes_list.currentItem()
        if not current_item:
            return
            
        note_id = current_item.data(Qt.UserRole)
        title = current_item.text()
        
        # Bestätigung
        reply = QMessageBox.question(
            self, 'Notiz löschen', 
            f'Möchten Sie die Notiz "{title}" wirklich löschen?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # Aus Datenbank löschen
            self.cursor.execute('DELETE FROM notizen WHERE id = ?', (note_id,))
            self.conn.commit()
            
            # UI aktualisieren
            self.load_notes()
            
            # Editor leeren
            self.title_edit.clear()
            self.content_edit.clear()
            self.current_note_id = None
            self.is_editing = False
            
            self.status_label.setText("Notiz gelöscht")
            
    def load_selected_note(self):
        """Ausgewählte Notiz in den Editor laden"""
        current_item = self.notes_list.currentItem()
        if not current_item:
            return
            
        note_id = current_item.data(Qt.UserRole)
        
        # Notiz aus Datenbank laden
        self.cursor.execute('''
            SELECT titel, inhalt FROM notizen WHERE id = ?
        ''', (note_id,))
        
        result = self.cursor.fetchone()
        if result:
            title, content = result
            
            # Editor füllen
            self.is_editing = True  # Flag setzen um Auto-Save zu verhindern
            self.title_edit.setPlainText(title)
            self.content_edit.setPlainText(content or '')
            self.current_note_id = note_id
            self.is_editing = False
            
            self.status_label.setText(f"Notiz '{title}' geladen")
            
    def on_selection_changed(self):
        """Auswahl in der Notizenliste geändert"""
        has_selection = self.notes_list.currentItem() is not None
        self.delete_note_btn.setEnabled(has_selection)
        
    def on_title_changed(self):
        """Titel der Notiz wurde geändert"""
        if not self.is_editing and self.current_note_id:
            self.update_note_in_list()
            
    def on_content_changed(self):
        """Inhalt der Notiz wurde geändert"""
        if not self.is_editing and self.current_note_id:
            self.status_label.setText("Ungespeicherte Änderungen...")
            
    def update_note_in_list(self):
        """Notiz-Titel in der Liste aktualisieren"""
        if not self.current_note_id:
            return
            
        new_title = self.title_edit.toPlainText().strip()
        if not new_title:
            return
            
        # Titel in der Liste aktualisieren
        current_item = self.notes_list.currentItem()
        if current_item:
            current_item.setText(new_title)
            
    def auto_save_current_note(self):
        """Aktuelle Notiz automatisch speichern"""
        if not self.current_note_id or self.is_editing:
            return
            
        title = self.title_edit.toPlainText().strip()
        content = self.content_edit.toPlainText()
        
        if not title:
            title = "Unbenannte Notiz"
            
        # In Datenbank speichern
        self.cursor.execute('''
            UPDATE notizen 
            SET titel = ?, inhalt = ?, geaendert = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (title, content, self.current_note_id))
        
        self.conn.commit()
        
        # Liste aktualisieren wenn sich der Titel geändert hat
        current_item = self.notes_list.currentItem()
        if current_item and current_item.text() != title:
            current_item.setText(title)
            
        self.status_label.setText("Automatisch gespeichert")
        
    def closeEvent(self, event):
        """Beim Schließen der Anwendung"""
        # Letzte Änderungen speichern
        if self.current_note_id:
            self.auto_save_current_note()
            
        # Datenbankverbindung schließen
        self.conn.close()
        
        event.accept()


def main():
    app = QApplication(sys.argv)
    
    # App-Eigenschaften setzen
    app.setApplicationName("Notiz-App")
    app.setApplicationVersion("1.0")
    
    # Hauptfenster erstellen und anzeigen
    window = NotizApp()
    window.show()
    
    # Event Loop starten
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

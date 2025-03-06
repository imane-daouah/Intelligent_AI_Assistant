# 🤖 Intelligent AI Assistant

## 📌 Description
**Intelligent AI Assistant** est un assistant virtuel développé en Python utilisant **Tkinter** pour l'interface graphique, **speech_recognition** pour la reconnaissance vocale et **pyttsx3** pour la synthèse vocale.

## 🛠️ Fonctionnalités
✅ **Reconnaissance vocale** : Comprend et interprète la voix de l'utilisateur.  
✅ **Synthèse vocale** : Répond à l'utilisateur par une voix artificielle.  
✅ **Affichage d'une interface utilisateur (Tkinter)** : Fenêtre interactive avec des boutons et une boîte de dialogue.  
✅ **Navigation web automatique** : Ouvre Google, YouTube et d'autres services en fonction des commandes.  
✅ **Lecture de musique** : Joue des morceaux en ligne ou depuis le PC.

## 📂 Structure du projet
```
📂 Intelligent_AI_Assistant
│── gui.py                # Interface graphique avec Tkinter
│── action.py             # Gestion des commandes utilisateur
│── speak_to_text.py      # Reconnaissance vocale
│── speak.py              # Synthèse vocale
│── requirements.txt      # Liste des dépendances nécessaires
│── README.md             # Documentation du projet
```

## 🚀 Installation et Exécution
### 1️⃣ **Cloner le projet**
```bash
git clone https://github.com/ton-utilisateur/Intelligent_AI_Assistant.git
cd Intelligent_AI_Assistant
```

### 2️⃣ **Créer un environnement virtuel et installer les dépendances**
python -m venv assistant
source assistant/bin/activate  # Sur macOS/Linux
assistant\Scripts\activate    # Sur Windows
pip install -r requirements.txt


### 3️⃣ **Exécuter l'application**
```bash
python gui.py
```

## 📌 Technologies utilisées
- **Python 3.x**
- **Tkinter** (Interface utilisateur)
- **SpeechRecognition** (Reconnaissance vocale)
- **pyttsx3** (Synthèse vocale)
- **requests_html** (Web Scraping)



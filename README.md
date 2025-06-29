# Smart File Organizer

Automatyczne sortowanie plików według typu, rozmiaru i daty utworzenia.

## 🎯 Cel Projektu

Automatyzacja organizacji plików na dysku, oszczędność 2-3 godzin tygodniowo na ręcznym sortowaniu dokumentów.

## 🚀 Funkcjonalności

- **Automatyczne sortowanie** według rozszerzeń plików
- **Kategoryzacja** dokumentów, obrazów, arkuszy, prezentacji, archiwów
- **Szczegółowe logowanie** wszystkich operacji
- **Obsługa błędów** z raportowaniem problemów
- **Sprawdzanie duplikatów** przed przeniesieniem plików

## 🛠️ Technologie

- **Python 3.x** - język programowania
- **pathlib** - operacje na ścieżkach plików
- **shutil** - przenoszenie i kopiowanie plików
- **os** - operacje systemowe

## 📁 Struktura Projektu

```

smart-file-organizer/
├── src/
│   └── file_organizer.py    \# Główny kod aplikacji
├── logs/                    \# Logi operacji (planowane)
├── tests/                   \# Testy jednostkowe (planowane)
├── docs/                    \# Dokumentacja (planowane)
└── README.md               \# Ten plik

```

## 🔧 Instalacja i Użycie

### Wymagania
- Python 3.7+
- System Windows/Linux/macOS

### Uruchomienie
1. Sklonuj repozytorium:
```

git clone https://github.com/pzoladkiewicz/projekty.git
cd projekty/1-smart-file-organizer

```

2. Dostosuj ścieżki w pliku `src/file_organizer.py`:
```

source = r"C:\Twoja\Ścieżka\Do\Folderu\Źródłowego"
destination = r"C:\Twoja\Ścieżka\Do\Folderu\Docelowego"

```

3. Uruchom skrypt:
```

python src/file_organizer.py

```

## 📊 Przykład Działania

**Przed:**
```

Downloads/
├── dokument.pdf
├── zdjecie.jpg
├── raport.xlsx
└── prezentacja.pptx

```

**Po:**
```

OrganizedFiles/
├── Documents/
│   └── dokument.pdf
├── Images/
│   └── zdjecie.jpg
├── Spreadsheets/
│   └── raport.xlsx
└── Presentations/
└── prezentacja.pptx

```

## 🎯 Business Value

- **Oszczędność czasu**: 2-3 godziny tygodniowo
- **Automatyzacja**: Eliminacja ręcznego sortowania
- **Organizacja**: Przejrzysta struktura plików
- **Skalowalność**: Łatwe dodawanie nowych kategorii

## 🔄 Status Projektu

- ✅ **v1.0** - Podstawowa funkcjonalność sortowania
- ✅ **v1.1** - System logowania
- ✅ **v1.2** - Konfiguracja przez plik config
- ✅ **v1.3** - Scheduler automatyczny
- 📋 **v1.4** - Sortowanie według rozmiaru
- 📋 **v1.5** - Sortowanie według daty

## 🧪 Testowanie

Projekt przetestowany na:
- Windows 10/11
- Różne typy plików (.pdf, .jpg, .xlsx, .pptx, .zip)
- Foldery z 50+ plikami

## 🤝 Wkład w Rozwój

Ten projekt jest częścią mojej ścieżki rozwoju.


## 📞 Kontakt

**Paweł Żołądkiewicz**
- LinkedIn: [linkedin.com/in/pzoladkiewicz](https://linkedin.com/in/pzoladkiewicz)
- Email: pzoladkiewicz@gmail.com
- Portfolio: [github.com/pzoladkiewicz/projekty](https://github.com/pzoladkiewicz/projekty)

---
*Projekt stworzony w ramach rozwoju kompetencji Python Automation - Czerwiec 2025*
```

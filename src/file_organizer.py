"""
Smart File Organizer v1.2
Automatyczne sortowanie plików według typu i daty
Autor: pzoladkiewicz
Data: 2025-06-24
"""

import os
import shutil
from pathlib import Path
import datetime
from logger import setup_logger, log_file_operation # <- nowe linia
from config import Config # <- Nowa linia

def create_folders(base_path):
    """
    Tworzy foldery dla różnych typów plików na podstawie konfiguracji

    """
    categories = Config.get_file_categories()

    print(f"Tworzę foldery w: {base_path}")
    
    for folder_name in categories.keys():
        folder_path = os.path.join(base_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"✓ Utworzono folder: {folder_name}")
        else:
            print(f"→ Folder juz istnieje: {folder_name}")
            
    return categories

def get_file_category(file_extension, categories):
    """
    Okresla kategorię pliku na podstawie rozszerzenia
    
    Args:
        file_extension (str): Rozszerzenie pliku (np. '.pdf')
        categories (dict): Słownik kategorii i rozszerzeń
        
    Returns:
        str: Nazwa kategorii
    """

    file_extension = file_extension.lower()
    
    for category, extensions in categories.items():
        if file_extension in extensions:
            return category
        
    return 'Others'

def organize_files(source_folder=None, destination_folder=None):
    """
    Główna funkcja organizująca pliki z logowniem i konfiguracją
    """
    
    # Użyj domyslnych scieżek z konfiguracji jesli nie podano
    
    if source_folder is None:
        source_folder = Config.DEFAULT_SOURCE
    if destination_folder is None:
        destination_folder = Config.DEFAULT_DESTINATION
        
    # Wyswietl konfigurację
    Config.print_config()
    
    # Skonfiguruj logger tylko jesli włączony
    logger = None
    if Config.LOG_ENABLED:
        logger = setup_logger(Config.LOG_DIRECTORY)
        
    
    
    print("=" * 50)
    print("🗂️  SMART FILE ORGANIZER")
    print("=" * 50)
    print(f"📁 Folder źródłowy: {source_folder}")
    print(f"📂 Folder docelowy: {destination_folder}")
    print("-" * 50)
    
    if logger:
        logger.info(f"Rozpoczęto organizację plików: {source_folder} -> {destination_folder}")
    
    # Sprawdź, czy folder źródłowy istnieje
    if not os.path.exists(source_folder):
        error_msg = f"Folder źródłowy nie istnieje: {source_folder}"
        print(f"❌ BŁĄD: {error_msg}")
        logger.error(error_msg)
        return False   
    
    # Utwórz folder docelowy jesli nie istnieje
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        logger.info(f"Utworzono folder docelowy: {destination_folder}")
        print(f"✓ Utworzono folder docelowy: {destination_folder}")
        
    # Utwórz foldery kategorii
    categories = create_folders(destination_folder)
    logger.info(f"Utworzono {len(categories)} kategorii folderów")
    
    # Liczniki
    
    moved_files = 0
    errors = 0
    skipped_files = 0
    
    print("\n🔄 Rozpoczynam organizację plików...")
    print("-" * 50)
    
    # Przejdź przez wszystkie pliki w folderze źródłowym
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
    
        # Pomiń foldery, organizuj tylko pliki
        if os.path.isfile(source_path):
            try:
                
                # Sprawdź czy plik jest wykluczony
                if Config.is_file_excluded(filename):
                    print(f"🚫  Wykluczono plik: {filename}")
                    if logger:
                        log_file_operation(logger, "SKIP", filename, source_path, "N/A", "EXCLUDED")
                    skipped_files += 1
                    continue
                
                # Sprawdź rozmiar pliku
                if not Config.is_file_size_valid(source_path):
                    print(f"📏 Plik poza limitami rozmiaru: {filename}")
                    if logger:
                        log_file_operation(logger, "SKIP", filename, source_path, "N/A", "SIZE_LIMIT")
                    skipped_files += 1
                    continue
                
                
                # Pobierz rozszerzenie pliku
                file_extension = Path(filename).suffix
                
                if not file_extension:
                    print(f"⚠️  Pominięto plik bez rozszerzenia: {filename}")
                    log_file_operation(logger, "SKIP", filename, source_path, "N/A", "NO_EXTENSION")
                    skipped_files += 1
                    continue
                
                # Okresl kategorię
                category = get_file_category(file_extension, categories)
    
    
                # Ścieżka docelowa
                destination_path = os.path.join(destination_folder, category, filename)
                
                # Sprawdź, czy plik już istnieje w miejscu docelowym
                if os.path.exists(destination_path):
                    print(f"⚠️  Plik już istnieje: {filename} → {category}/")
                    log_file_operation(logger, "SKIP", filename, source_path, destination_path, "FILE_EXISTS")
                    skipped_files +=  1
                    continue
                
                # Przenies plik
                shutil.move(source_path, destination_path)
                print(f"✅ Przeniesiono: {filename} → {category}/")
                log_file_operation(logger, "MOVE", filename, source_path, destination_path, "SUCCESS")
                moved_files += 1
                
            except Exception as e:
                error_msg = f"Błąd przy przenoszeniu {filename}: {str(e)}"
                print(f"❌ {error_msg}")
                log_file_operation(logger, "ERROR", filename, source_path, "N/A", str(e))
                errors += 1
                
    # Podsumowanie
    print("\n" + "=" * 50)
    print("📊 PODSUMOWANIE")
    print("=" * 50)
    print(f"✅ Przeniesiono plików: {moved_files}")
    print(f"⚠️  Pominięto plików: {skipped_files}")
    print(f"❌ Błędów: {errors}")
    print(f"📁 Łączna liczba plików: {moved_files + skipped_files + errors}")
    
    # Loguj podsumowanie
    logger.info(f"Operacja zakończona, Przeniesiono: {moved_files}, Pominięto: {skipped_files}, Błędów: {errors}") 
    return True

# Funkcja testowa
def test_organizer():
    """Funkcja do testowania organizatora z konfiguracją"""
    print("🧪 SMART FILE ORGANIZER v1.2 - TRYB TESTOWY")
    print("\n🔧 Sprawdź konfigurację w pliku config.py przed uruchomieniem")
    
    
    # Użyj konfiguracji domyslnej
    organize_files()

if __name__ == "__main__":
    test_organizer()
    
    
    
    
    
    
    
    
    
    
    
    
    

"""
Smart File Organizer v1.0
Automatyczne sortowanie plików według typu i daty
Autor: pzoladkiewicz
Data: 2025-06-24
"""

import os
import shutil
from pathlib import Path
import datetime

def create_folders(base_path):
    """
    Tworzy foldery dla różnych typów plików
    
    Args:
        base_path (str): Ścieżka do folderu głównego
        
    Returns:
        dict: Słownik z kategoriami i rozszerzeniami

    """
    
    folders = {
        'Documents': ['.pdf', '.doc', 'docx', '.txt', '.rtf'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Spreadsheets': ['.xls', '.xlsx', '.csv', '.ods'],
        'Presentations': ['.ppt', '.pptx', 'odp'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', 'gz'],
        'Others': []    
        }

    print(f"Tworzę foldery w: {base_path}")
    
    for folder_name in folders.keys():
        folder_path = os.path.join(base_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"✓ Utworzono folder: {folder_name}")
        else:
            print(f"→ Folder juz istnieje: {folder_name}")
            
    return folders

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

def organize_files(source_folder, destination_folder):
    """
    Główna funkcja organizująca pliki
    
    Args:
        source_folder (str): Folder źródłowy z plikami
        destination_folder (str): Folder docelowy
    """
    print("=" * 50)
    print("🗂️  SMART FILE ORGANIZER")
    print("=" * 50)
    print(f"📁 Folder źródłowy: {source_folder}")
    print(f"📂 Folder docelowy: {destination_folder}")
    print("-" * 50)
    
    # Sprawdź, czy folder źródłowy istnieje
    if not os.path.exists(source_folder):
        print(f"❌ BŁĄD: Folder {source_folder} nie istnieje!")
        return False   
    
    # Utwórz folder docelowy jesli nie istnieje
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"✓ Utworzono folder docelowy: {destination_folder}")
        
    # Utwórz foldery kategorii
    categories = create_folders(destination_folder)
    
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
                # Pobierz rozszerzenie pliku
                file_extension = Path(filename).suffix
                
                if not file_extension:
                    print(f"⚠️  Pominięto plik bez rozszerzenia: {filename}")
                    skipped_files += 1
                    continue
                
                # Okresl kategorię
                category = get_file_category(file_extension, categories)
    
    
                # Ścieżka docelowa
                destination_path = os.path.join(destination_folder, category, filename)
                
                # Sprawdź, czy plik już istnieje w miejscu docelowym
                if os.path.exists(destination_path):
                    print(f"⚠️  Plik już istnieje: {filename} → {category}/")
                    skipped_files +=  1
                    continue
                
                # Przenies plik
                shutil.move(source_path, destination_path)
                print(f"✅ Przeniesiono: {filename} → {category}/")
                moved_files += 1
                
            except Exception as e:
                print(F"❌ BŁĄD przy przenoszeniu {filename}: {e}")
                errors += 1
                
    # Podsumowanie
    print("\n" + "=" * 50)
    print("📊 PODSUMOWANIE")
    print("=" * 50)
    print(f"✅ Przeniesiono plików: {moved_files}")
    print(f"⚠️  Pominięto plików: {skipped_files}")
    print(f"❌ Błędów: {errors}")
    print(f"📁 Łączna liczba plików: {moved_files + skipped_files + errors}")
    
    return True

# Funkcja testowa
def test_organizer():
    """Funkcja do testowania organizatora"""
    print("🧪 TRYB TESTOWY")
    print("Przed uruchomieniem na prawdziwych plikach, przetestuj na kopii!")
    
    # ZMIEŃ TE ŚCIEŻKI NA SWOJE!
    source = r"C:\Users\pzoladkiewicz\Desktop\TestFolder"
    destination = r"C:\Users\pzoladkiewicz\Desktop\OrganizedFiles"
    
    print("\n⚠️  UWAGA: Sprawdź ścieżki przed uruchomieniem!")
    print(f"Źródło: {source}")
    print(f"Cel: {destination}")
    
    # Odkomentuj poniższą linię gdy będziesz gotowy
    organize_files(source, destination)

if __name__ == "__main__":
    test_organizer()
    
    
    
    
    
    
    
    
    
    
    
    
    

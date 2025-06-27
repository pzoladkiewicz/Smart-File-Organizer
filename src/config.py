"""
Konfiguracja Smart File Organizer
Wszystkie ustawienia wjednym miejscu
"""


import os

class Config:
    """ Klasa konfiguracji dla File Organizer """
    
    # Domysle folder (ZMIEŃ NA SWOJE)
    DEFAULT_SOURCE = r"C:\Users\pzoladkiewicz\Desktop\TestFolder"
    DEFAULT_DESTINATION = r"C:\Users\pzoladkiewicz\Desktop\OrganizedFiles"

    # Kategorie plików i rozszerzenia
    FILE_CATEGORIES = {
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'],
        'Spreadsheets': ['.xls', '.xlsx', '.csv', '.ods'],
        'Presentations': ['.ppt', '.pptx', '.odp'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php'],
        'Others': []
        }

    # Ustawienia logowania
    LOG_ENABLED = True
    LOG_DIRECTORY = "../logs"
    LOG_LEVEL = "INFO" # DEBUG, INFO, WARNING, ERROR
    
    # Ustawienia operacji
    MOVE_FILES = True  # True = przenies, False = kopiuj
    SKIP_EXISTING = True  # True = pomiń istniejące, False = nadpisz
    CREATE_DATE_FOLDERS = False  # True = dodatkowe foldery z datami
    
    # Filtr plików
    MIN_FILE_SIZE_MB = 0 # Minimalna wielkosć pliku w MB (0 = bez limitu)
    MAX_FILE_SIZE_MB = 0 # Maksymalna wielkosć pliku w MB (0 = bez limitu)
    EXCLUDED_EXTENSIONS = ['.temp', '.tmp', '.log', '.cache']
    
    @classmethod
    def get_file_categories(cls):
        """ Zwraca słownik kategorii plików """
        return cls.FILE_CATEGORIES.copy()
    
    @classmethod
    def is_file_excluded(cls, filename):
        """ Sprawdza, czy plik jest wykluczony """
        from pathlib import Path
        extension = Path(filename).suffix.lower()
        return extension in cls.EXCLUDED_EXTENSIONS
    
    
    @classmethod
    def is_file_size_valid(cls, file_path):
        """ Sprawdza, czy rozmiar pliku miesci się w limitach """
        if cls.MIN_FILE_SIZE_MB == 0 and cls.MAX_FILE_SIZE_MB == 0:
            return True
        
        try:
            size_mb = os.path.getsize(file_path) / (1024 * 1024)
            
            if cls.MIN_FILE_SIZE_MB > 0 and size_mb < cls.MIN_FILE_SIZE_MB:
                return False
            
            if cls.MAX_FILE_SIZE_MB > 0 and size_mb > cls.MAX_FILE_SIZE_MB:
                return False
            
            return True
        except:
            return True  # W przypadku błędu, akceptuj plik
        
    @classmethod
    def print_config(cls):
        """ Wyswietla aktualną konfigurację """

        print("🔧 KONFIGURACJA SMART FILE ORGANIZER")
        print("=" * 50)
        print(f"📁 Folder źródłowy: {cls.DEFAULT_SOURCE}")
        print(f"📂 Folder docelowy: {cls.DEFAULT_DESTINATION}")
        print(f"🗂️  Liczba kategorii: {len(cls.FILE_CATEGORIES)}")
        print(f"📝 Logowanie: {'Włączone' if cls.LOG_ENABLED else 'Wyłączone'}")
        print(f"🔄 Operacja: {'Przenoszenie' if cls.MOVE_FILES else 'Kopiowanie'}")
        print(f"⏭️  Pomijanie duplikatów: {'Tak' if cls.SKIP_EXISTING else 'Nie'}")
        print(f"📅 Foldery z datami: {'Tak' if cls.CREATE_DATE_FOLDERS else 'Nie'}")
        
        if cls.MIN_FILE_SIZE_MB > 0 or cls.MAX_FILE_SIZE_MB > 0:
            print(f"📏 Limity rozmiaru: {cls.MIN_FILE_SIZE_MB}MB - {cls.MAX_FILE_SIZE_MB}MB")
        
        if cls.EXCLUDED_EXTENSIONS:
            print(f"🚫 Wykluczone rozszerzenia: {', '.join(cls.EXCLUDED_EXTENSIONS)}")
        
        print("-" * 50)       
            
            
            
            
    
    
    

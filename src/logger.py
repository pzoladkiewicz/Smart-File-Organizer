# -*- coding: utf-8 -*-
"""
System logowania dla Smart File Organizer
Zapisuje wszystkie operacje do pliku log
"""

import logging
import os
from datetime import datetime

def setup_logger(log_dir="../logs"):
    """
    Konfiguruje system logowania

    Args:
        log_dir (str): Katalog na pliki log
        
    Returns:
        logging.logger: Skonfigurowany logger
    """
    # Utwórz katalog logs jeli nie istnieje
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    # Nazwa pliku log z datą
    log_filename = f"file_orgnizer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_path = os.path.join(log_dir, log_filename)
    
    # Konfiguracja loggera
    logger = logging.getLogger('FileOrganizer')
    logger.setLevel(logging.INFO)
    
    # Usuń poprzednie handlery jesli istnieją
    if logger.handlers:
        logger.handlers.clear()
        
    # Handler do pliku
    file_handler = logging.FileHandler(log_path, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    
    #Handler dla konsoli
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Format logów
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Dodaj handlery do loggera
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
                                  
    logger.info(f"Logger skonfigurowany. Plik log: {log_path}")
    return logger

def log_file_operation(logger, operation, filename, source, destination, status="SUCCESS"):
    """
    Loguje operacje na pliku
    
    Args:
        logger: logger object
        operation (str): Typ operacji (MOVE, COPY, SKIP, ERROR)
        filename (str): Nazwa pliku
        source (str): Ścieżka źródłowa
        destination (str): Ścieżka docelowa
        status (str): Status operacji
    """
    message = f"{operation} | {filename} | {source} → {destination} | {status}"
    
    if status == "SUCCESS":
        logger.info(message)
    elif status == "SKIP":
        logger.warning(message)
    else:
        logger.error(message)
    
    
    
    
    
    
    
    
    
    
    
    
    

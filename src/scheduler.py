# -*- coding: utf-8 -*-
"""
Scheduler dla Smart File Organizer
Automatyczne uruhcamianie w okreslonych interwałach
"""


import time
import schedule
from datetime import datetime
from file_organizer import organize_files
from config import Config
from logger import setup_logger


class FileOrganizerScheduler:
    """ Klasa do zarządzania harmonogramem organizacji plików """
    
    def __init__(self):
        self.logger = setup_logger() if Config.LOG_ENABLED else None
        self.is_running = False
        
    def run_organization(self):
        """ Uruchamia organizację plików """
        try:
            print(f"\n⏰ {datetime.now().strf3time('%Y-%m-%d %H:%M:%S')} - Rozpoczynam automatyczną organizację...")
            if self.logger:
                self.logger.info("Automatyczna organizacja plików - START")
                
            # Uruchom organizację
            success = organize_files()
            
            if success:
                print("✅  Automatyczna organizacja zakończona pomyslnie")
                if self.logger:
                    self.logger.info("Automatyczna organizacja - SUKCES")
            else:
                print("❌ Automatyczna organizacja zakończona błędem")
                if self.logger:
                    self.logger.error("Automatyczna organizacja plików - BŁĄD")
                    
        except Exception as e:
            error_msg = f"Błąd podczas automatycznej organizacji: {str(e)}"
            print(f"❌  {error_msg}")
            if self.logger:
                self.logger.error(error_msg)

    def setup_schedule(self, interval_minutes=30):
        """
        Konfiguruje harmonogram uruchamiania
        
        Args:
            interval_minutes (int): Interwał w minutach

        """
        schedule.clear() # Wyczysć poprzednie harmonogramy
        
        if interval_minutes > 0:
            schedule.every(interval_minutes).minutes.do(self.run_organization)
            print(f"📅 Harmonogram ustawiony: co {interval_minutes} minut")
            if self.logger:
                self.logger.info(f"Harmonogram ustawiony: co {interval_minutes} minut")
        else:
            print("Harmonogram wyłączony (interwał = 0)")
            
    def setup_daily_schedule(self, time_str="09:00"):
        """
        Konfiguruje codzienne uruchamianie o okreslonej godzinie
        
        Args:
            time_str (str): Godzina w formacie "HH:MM"
        """
        schedule.clear()
        schedule.every().day.at(time_str).do(self.run_organization)
        print(f"📅 Harmonogram dzienny ustawiony: codziennie o {time_str}")
        if self.logger:
            self.logger.info(f"Harmonogram dzienny ustawiony: codziennie o {time_str} ")
            
    def start_scheduler(self, mode="interval", interval_minutes=30, daily_time="09:00"):
        """
        Uruchamia scheduler

        Args:
            mode (str): "interval" lub "daily"
            interval_minutes (int): Interwa ł w minutach (dla trybu interval)
            daily_time (str): Godzina (dla trybu daily)

        """
        print("🚀 SMART FILE ORGANIZER - TRYB AUTOMATYCZNY")
        print("=" * 50)
        
        if mode == "interval":
            self.setup_schedule(interval_minutes)
        elif mode == "daily":
            self.setup_daily_schedule(daily_time)
        else:
            print("❌ Nieznany tryb harmonogramu")
            return
        
        self.is_running = True
        print("🔄 Scheduler uruchomiony. Nacinij Ctrl+C aby zatrzymać")
        print("-" * 50)
        
        try:
            while self.is_running:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Scheduler zatrzymany przez użytkownika")
            if self.logger:
                self.logger.info("Scheduler zatrzymany przez uźytkownika")
        except Exception as e:
            print(f"\n❌ Błąd schedulera: {str(e)}")
            if self.logger:
                self.logger.error(f"Błąd schedulera: {str(e)}")
                
    def stop_scheduler(self):
        """Zatrzymuje scheduler"""
        self.is_running = False
        schedule.clear()
        print("🛑 Scheduler zatrzymany")

def main():
    """Główna funkcja uruchamiająca scheduler"""
    scheduler = FileOrganizerScheduler()
    
    print("🔧 KONFIGURACJA SCHEDULERA")
    print("=" * 30)
    print("1. Tryb interwałowy (co X minut)")
    print("2. Tryb dzienny (codziennie o określonej godzinie)")
    print("3. Jednorazowe uruchomienie")
        
    try:
        choice = input("\nWybierz opcję (1-3): ").strip()
        
        if choice == "1":
            interval = int(input("Podaj interwał w minutach (np. 30): "))
            scheduler.start_scheduler("interval", interval_minutes=interval)
        elif choice == "2":
            time_str = input("Podaj godzinę (HH:MM, np. 09:00): ").strip()
            scheduler.start_scheduler("daily", daily_time=time_str)
        elif choice == "3":
            scheduler.run_organization()
        else:
            print("❌ Nieprawidłowy wybór")
            
    except ValueError:
        print("❌ Nieprawidłowa wartosć")
    except Exception as e:
        print(f"❌ Błąd: {str(e)}")
        
if __name__ == "__main__":
    main()
                                 
        
        
        
        
# This is a sample Python script.

# Converting file PDF to file MP3.
# Rdosław Tecmer radek69tecmer@gmail.com
# GitHub - https://github.com/remceTkedaR.


import pdfplumber
import pyttsx3
import time

# Otwórz plik PDF
with pdfplumber.open('file.pdf') as pdf:
    # Konfiguracja silnika TTS
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 100)  # Ustawienie szybkości mówienia (100 to domyślna wartość)
    speaker.setProperty('voice', 'your_preferred_male_voice')  # Wprowadź nazwę preferowanego męskiego lektora

    for page in pdf.pages:
        text = page.extract_text()
        clean_text = text.strip().replace('\n', ' ')
        print(clean_text)

        # Zapisz tekst do pliku MP3
        mp3_file = f'page_{page.page_number}.mp3'
        speaker.save_to_file(clean_text, mp3_file)
        speaker.runAndWait()

        # Poczekaj chwilę przed przetworzeniem kolejnej strony
        time.sleep(1)

    speaker.stop()





# This is a sample Python script.

# Converting file PDF to file MP3.
# Rdosław Tecmer radek69tecmer@gmail.com
# GitHub - https://github.com/remceTkedaR.


import pdfplumber
import pyttsx3
import time

# Open file PDF
with pdfplumber.open('file.pdf') as pdf:
    # Engine TTS configuration
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 100)  # Speech rate setting (100 is the default value)
    speaker.setProperty('voice', 'your_preferred_male_voice')  # Enter the name of your preferred male voiceover

    for page in pdf.pages:
        text = page.extract_text()
        clean_text = text.strip().replace('\n', ' ')
        print(clean_text)

        # Save to MP3
        mp3_file = f'page_{page.page_number}.mp3'
        speaker.save_to_file(clean_text, mp3_file)
        speaker.runAndWait()

        # Please wait a while before processing the next page
        time.sleep(1)

    speaker.stop()





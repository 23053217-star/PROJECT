# main.py

from datetime import datetime

def save_entry(date, emotion, note):
    with open("journal.txt", "a") as file:
        file.write(f"{date} | {emotion} | {note}\n")

def main():
    print("AI Emotion Journal App")
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"Date/Time: {date}")
    
    emotions = ['Happy', 'Sad', 'Angry', 'Anxious', 'Excited', 'Calm', 'Other']
    print("Select your emotion today:")
    for idx, em in enumerate(emotions, 1):
        print(f"{idx}. {em}")

    choice = 1  # default choice for demo, can be changed or asked from user if input desired.
    emotion = emotions[choice - 1]

    note = "Had a productive day."  # default note, can be changed or asked from user if input desired.
    
    save_entry(date, emotion, note)
    print(f"Entry saved: {date} | {emotion} | {note}")

if __name__ == "__main__":
    main()

# Match The Cards
Train your memorizing ability, reflexes, and perseverance by playing Match The Cards! 

## WARNING!!!
This game contains jumpscares, flashing lights, and loud noises. Do not play this game if you have epilepsy!

## Overview
Match The Cards is a fun sometimes stressful card matching game developed using Python and Pygame. The objective of the game is to match pairs of cards with the same image. It helps in improving memory, concentration, reflexes, and yout ability to stay calm under pressure.

## Game mechanics
The game is entirely based on cursor movements. Therefore, no keyboard input, and the only required device besides a PC is a mouse or mousepad (for laptop users).

To play, click the start game button, then the game will display some cards for you to remember, then the cards will flip and you would need to find matching cards. If the cards match it will stay faced-up, else it will flip back.

Do this repeateadly until all the cards are matching and faced up, then the game will start another round.

### Note
- You cannot win the game, it will loop forever until you lose
- When the countdown reaches zero you lose the game

- The game can give you random bonus time if you matched the cards 3 times in a row*, and 6 times in a row*
- The game can give you random time penalty if you fail in matching the cards 3 times in a row*

- The game will get progressively harder by changing the variables above, Example: 
    - After 10 rounds won, the random time penalty happens when you fail matching the cards 2 times in a row.
    - After 10 rounds won, the random bonus time happens only if you matched the cards 4 times, and 6 times in a row

## Story
This game doesn't really have any initial design. I, Barri Nur Pratama, A university student studying computer science in Binus International, created this game to learn about more about Algorithm and Programming, especially python. My aim for this game is to add as many features as I want from the simple idea of a card matching game.

In the beggining of this project, I am still a newbie, and I believed that I have learned a lot more about programming by doing this project. Therefore, you will be able to see my one month coding journey in the source code. 

# Dependencies
- Python 3
- Pygame
- PyInstaller

# Installation Steps
1. Install Python 3 from the official website: https://www.python.org/
2. Install Pygame by using pip, run this command:
   ```
   pip install pygame
   ```
3. Install PyInstaller by using pip, run this command:
   ```
   pip install pyinstaller
   ```
4. Then to create the EXE file I run this command:
   ```
   python -m PyInstaller main.py --onefile --windowed
   ```

# Instructions to Run the Code
## The first way:
1. Download the all the files in the github repo as zip
2. Extract the zip file
3. Locate and run main.exe

## The second way:
1. Ensure you have Python 3 installed on your system
2. Install Pygame by following the steps above
3. Clone the github repo into a code editor
4. Run main.py

# Screenshots of the game
![image alt](https://github.com/Barrizzz/CardGame/blob/8d3d44c5bb7ef39119bb3824f9b7e381c81c0dce/screenshots/Screenshot1.png)

![image alt](https://github.com/Barrizzz/CardGame/blob/8d3d44c5bb7ef39119bb3824f9b7e381c81c0dce/screenshots/Screenshot2.png)

![image alt](https://github.com/Barrizzz/CardGame/blob/8d3d44c5bb7ef39119bb3824f9b7e381c81c0dce/screenshots/Screenshot3.png)

![image alt](https://github.com/Barrizzz/CardGame/blob/8d3d44c5bb7ef39119bb3824f9b7e381c81c0dce/screenshots/Screenshot4.png)

# Credits and references
## Music
- Kahoot soundtrack for the countdown music taken from Youtube: https://www.youtube.com/watch?v=-O3z9xRM5Rc&list=PLsa7dvIdIrDll1frTUiwSVZri51TF7-ax
- SFX 34. (2021, June 13). Who invited this kid Mp3 (TikTok) [Video]. YouTube. https://www.youtube.com/watch?v=RfQyq851SaE
- Discobre. (2024, October 6). Let It Snow (Brainrot Edition) “Ohio, Ohio, Ohio” AI Parody cover (lyrics by notjewboi) [Video]. YouTube. https://www.youtube.com/watch?v=h3vbvdesee8
- RAHILU. (2024, November 5). Thick of It by KSI but it’s Big Band Jazz (Full Version) [Video]. YouTube. https://www.youtube.com/watch?v=vKoC8bNQrFA
- Know Your TikTok. (2024, December 9). The viral cursed Plankton moaning meme explained [Video]. YouTube. https://www.youtube.com/watch?v=VvHkYjZZP3M

NOTE: The rest of the music and images used are royalty free

Special thanks to my friends: Michael, Jason, Attalah, and Salomo for allowing me to use their funny pictures :)

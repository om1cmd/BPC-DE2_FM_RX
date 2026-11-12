# BPC-DE2_FM_RX
Project for digital electronics course BPC-DE2 on BUT FEEC, FM radio receiver with digital tuning.
The project's goal is to create a functional FM radio receiver tuned by rotary encoder. Outputs consist of audio output routed to headphones and information shown on a OLED display.

## Team members:
- Marek Mička
- Šimon Tokarčík
- Pavel Trojan
- Alexandr Stoljar 

## Component list:

| Component | Model |
| ------ | -------------- |
| Microcontroller | Raspberry Pi Pico W |
| I2C FM radio tuner | Si4073 |
| I2C OLED display | SSD1306 |
| Rotary encoder | Rotary encoder |

## Block diagram  

![Block diagram](visualization&graphics/block_diagram.png)

*Block diagram may be subject to change*

## Pinout schematic

![Pinout schematic](visualization&graphics/pinout-schematic.png)

*Certain parts of pinout schematic such as GPIO connections may be subject to change*

## Progression and responsibilities
### Week 1
Git creation, agree on project proposal; component list and pin plan; repository structure, creation of block diagram.

| Person | Responsibility |
| ------ | -------------- |
| Marek Mička | Git creation, component research, experimentation with FM module |
| Šimon Tokarčík | Pinout schematic creation, git maintenance, component research |
| Pavel Trojan | Block diagram creation, component research |
| Alexandr Stoljar | Git maintenance, component research |

## Git structure
Currently proposed repository structure:

![Git structure](visualization&graphics/git-structure.png)

*Git structure may be subject to change*

## Readme - required contents (TO DO list)
- Problem statement and summary of the solution.
- Setup and operating instructions, including required MicroPython modules.
- Hardware inventory and any assumptions or limitations.
- Links to the poster and demonstration video.





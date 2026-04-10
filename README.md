# Digital-film-camera
This is a project I made for the Hackclub stasis YSWS. It is a camera that uses the raspberry pi camera module 3 and a raspberry pi zero to take pictures. I made it be a bit like the older film cameras so you don't get a preview on a screen, only after you took the picture.

**Why did I make this project?**

I made this project since I like photography, and hardware design and thought this would be a nice way to blend them together. I also wanted to have a simple camera I could just slip in my backpack, and don't have to worry about settings, lenses, etc.I usually use my phone for this, but sometimes I just like to leave my phone at home and have a seperate device for taking photos.

Camera assembly:
![Full camera assembly](https://github.com/jivespark/Digital-film-camera/blob/main/Pictures/Full%20assembly.png?raw=true)
Internal layout(for assembly):
![Internal layout](https://github.com/jivespark/Digital-film-camera/blob/main/Pictures/Internal%20layout.png?raw=true)
Schematic:
![Schematic](https://github.com/jivespark/Digital-film-camera/blob/main/Pictures/Schematic.png?raw=true)
PCB:
![PCB](https://github.com/jivespark/Digital-film-camera/blob/main/Pictures/PCB.png?raw=true)
BOM:
|Name                            |Purpose                                                   |Quantity|Total Cost (USD)|Link                                                 |Distributor|
|--------------------------------|----------------------------------------------------------|--------|----------------|-----------------------------------------------------|-----------|
|Resistor kit                    |Resistors for power and buzzer control                    |1       |6.26            |https://www.aliexpress.com/item/1005009689760726.html|Aliexpress |
|Passive buzzer                  |A passive buzzer for audio feedback                       |1       |4.52            |https://www.aliexpress.com/item/1005009689760726.html|Aliexpress |
|Female header                   |A female header to connect the pi                         |1       |0.83            |https://www.aliexpress.com/item/32854215610.html     |Aliexpress |
|0805 1A 6V fuse                 |A fuse for safeguarding the power managment               |1       |1.48            |https://www.aliexpress.com/item/1005011924342826.html|Aliexpress |
|4.7UH 1210 inductor             |Inductor for the power managment circuit                  |1       |2.76            |https://www.aliexpress.com/item/1005006118890471.html|Aliexpress |
|100µF 25V electrolytic capacitor|A capacitor for voltage regulation                        |1       |1.26            |https://www.aliexpress.com/item/1005006192445408.html|Aliexpress |
|IP5306 chip                     |Charging and discharging the battery with boost conversion|1       |1.94            |https://www.aliexpress.com/item/1005007505994153.html|Aliexpress |
|0805 Ceramic capacitors         |Ceramic capacitors for power managment.                   |1       |7.45            |https://www.aliexpress.com/item/1005010516436707.html|Aliexpress |
|15 to 22 pin CSI cable          |A CSI cable to connect the pi and the camera              |1       |2.17            |https://www.aliexpress.com/item/1005006522239991.html|Aliexpress |
|Raspberry pi camera module 3    |Camera module for taking pictures                         |1       |32.00           |https://www.amazon.com/n/dp/B0C9PYCV9S/              |Amazon     |
|Raspberry pi zero 2WH           |The main microcontroller controlling everything           |1       |32.99           |https://www.amazon.com/dp/B0GJQMKJ4V                 |Amazon     |
|Usb-c connector                 |Usb-c connector for charging                              |1       |4.43            |https://www.aliexpress.com/item/1005010700033077.html|Aliexpress |

# BlinkenHertz
Lets two RasPis communicate over blinking lights, with a high refresh rate.

Blinken (Like the telnet protocol joke) and Hertz(Sounds like hearts and the light flashes)


#### Setup
Must have internet connection on both PIs. Find their public IP address, may need to port forward the specific port (7129 - (GABI) to each device in router settings). Then wire up a button and led to the correct pins in your RasPi, mine are 10 and 12. Running the bash script will run both python scripts simultaniously. If you want to run unteathered, you may want to add the bash script to the startup sequence. Enjoy!

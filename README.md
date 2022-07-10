<h1>MUSIC Synth</h1>
<p><h3>This repo is a prototype for music synth AI. It takes in a midi file and returns a midi file.</h3><p>

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/VQFU5VyuM0k/0.jpg)](https://www.youtube.com/watch?v=VQFU5VyuM0k)

 ## Samples
 
 [Soundcloud](https://soundcloud.com/aditya-khadilkar/sets/paths?si=ea2c884fd76540b9abf7e9e843f52dc8)

## Installation

 1. Clone the repo
 2. Make sure you have python and [java](https://www.java.com/en/download/) installed
 3. Download midi of a song you like. (mp3 to midi won't work)
 4. Put the midi in the "rawmidis" folder (you should see Beethoven's moonlight sonata there)
 5. run master.py
 6. A few new folders will be created automatically.
 7. The newly generated midi will appear in the "generatedMIDIs" folder.
 8. You can use sound fonts to make this midi sound more organic, cut out parts you don't like or simply re run master.py again to get a different result.

## Working
I first convert midi to ABC notation and extract the verses
I then use Byte Pair encoding to compress the repeated patterns and finally a markov model to generate the sequence.
The sequence is then converted to abc notation which is then converted to a midi file
I use soundfonts to get a mp3

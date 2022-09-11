# Exercise 1: Using the on-board RGB


### Idea
Create a mood using the LED RGB light for the scene in this URL (2 minutes)

### Video

[Bean's War Movie?! | Mr Bean's Holiday | Mr Bean Official](https://www.youtube.com/watch?v=a-VLZ0T8WMo)

### Idea

The idea was to set a mood for a short clip from Mr. Bean’s movie, using the on-board RGB LED by creating a sequence of color patterns. It lasts for 2 minutes  – most of which is repetition as long as a particular scene progresses. 

### Working

The video starts with a scene where Mr. Bean opens his eyes and looks to understand where he is. For this I used a white color that gradually increases in brightness to show how light enters the eye of the person when they’re opening their eyes gradually. Further, the video’s next scene shows people having coffee and kids playing which sets a pleasant mood. So I’ve used a yellow color (a light that goes off very slowly and turns on again) to show the happy and calm vibe. For the third scene when Bean senses a danger, I’ve used the red light for a certain time with 50% and 100% brightness alternatively. The video then progresses to the next scene where the army enters and shooting begins – I’ve depicted this with alternating red and blue lights. When Mr. Bean sees and hits the girl, there’s a rainbow light that glows and turns back to the yellow light that gradually goes off once there is a lot of confusion in the air. When the video shows the yoghurt, it goes back to rainbow color to focus on the main object and display the hype created. 

### Code Explanation

```python
#scene - fear: panzer enters
j = 0 # used in the while loop to end the loop at a specific point
# Red light goes on and off at 2 different brightness settings
# NOTE: the numbers for the while loop are chosen after testing with the time of each scene in the video
while j < 0.25:
    led.brightness = 1 # 100% brightness
    led[0] = (255,0,0) # (r,g,b) format – red color
    time.sleep(1) # wait for a second
    led.brightness = 0.5 # 50% brightness
    time.sleep(1)
    led.brightness = 1 # 100% brightness
    time.sleep(1)
    j+=0.1 # increment j by 0.1
```

Consider this code block for the scene when the tank enters the area. I wanted to depict alarm🚨, caution⛔️, and fear😨 – so I used the red color. But I had to show that there is an ongoing action so I constantly alternated the brightness from 50% and 100%. It starts with 100% brightness, goes red for a second, and then goes red at 50% brightness for a second, and then 100% again, and the loop repeats until the condition to terminate is satisfied (using the `variable j`)

### Further Developments

It was a tedious process to time specific scene and find the comparative value for the termination condition of while loop. I want to learn how to use time library to time the scenes and the patterns correctly. What I used in this script was more of a trial and error method where I guessed how long it would take for the scene to end (in seconds) v/s how fast the loop is being executed. I would love to explore how the time library can handle this using its methods.

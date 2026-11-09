# Reflections

1. Share one aspect of building this project you found challenging and how you
   overcame it.

One of the most challenging components of completing this assignment was determining how to write the save functions so that overall stats are saved in a json file. I have never written a program that uses json files, however I was pleased to find that there is a builtin module for it already, so implementation didn't initially appear challenging. Upon writing the code that I wanted, however, the program began to crash, as the first run of the program did not have a json file to load with zeroes in it. Solving this issue involved using `try/except` to tell the program what to do when there was no file already stored. Allowing the program to save stats across multiple games became another issue that occurred during development. That was resolved without too much difficulty, however the structure of my files started to become an issue. My initial writing for the tests of the save function required the `test_game.py` file to be placed in the `src` folder, rather than in its own dedicated test folder. With this structure not looking as organized, I wanted to change the way the code was written, however it took me a couple of tries to refer to the correct folder when I was importing modules from `game.py`.

2. Share one technical concept that you gained a deeper understanding of
   through building this project. Explain that concept in simple terms and
   explain how it is used in your project.

In Python, a class is used to directly link data with the functions that are meant to operate on it. In regards to my own work, A class is being used to organize the results of each instance of every test that is included. The value for `self` is changed with each instance of the functions it is used in, being used to pass data that is relevant to that instance through the function before it is stored as the output that is returned. In the case of a test function, such as `test_every_choice_can_appear`, self refers to the instance that the test method is being used on. The class that is defined within `test_game.py` is actually a subclass of `TestCase`, which `unittest` uses to identify and properly execute each test within.

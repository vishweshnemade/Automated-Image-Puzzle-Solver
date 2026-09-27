----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Project Report Structure
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

AUTOMATED IMAGE PUZZLE SYSTEM
Automated Image Puzzle Reconstruction and Solving System

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Submitted By:
Name: Vishwesh Nemade
Program: B.Tech CSE Core
Institution: VIT Bhopal University
Academic Year: 2026–27
Registration Number: 26BCE10989
Programming Language used: Python
Technologies: Python, Streamlit, Pill
University Email Id: vishwesh.26bce10989@vitbhopal.ac.in

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Introduction
The Automated Image Puzzle System is a Python-based interactive application designed to create and solve image-based puzzles. The system allows a user to upload an image and select a grid dimension such as 2 × 2 or 3 × 3.
The uploaded image is resized and divided into smaller pieces. These pieces are then randomly shuffled to create a scrambled puzzle. The user can manually arrange the pieces using the provided interface and check whether the arrangement is correct.
The system also provides an automated hint mechanism that compares the scrambled pieces with the original pieces and determines the correct position of each piece.
The application uses Streamlit to provide a simple web-based interface and Pillow for image processing.

Problem Statement
Manually solving image puzzles requires the user to identify the correct position of each piece and arrange them accordingly. For beginners, understanding how an image can be divided and reconstructed can also be difficult.
The objective of this project is to develop an interactive system that can divide an uploaded image into puzzle pieces, randomly scramble them, allow manual solving, verify the user's solution, and provide an automated solution hint.



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Functional Requirements
The system shall provide the following functions:
1.	Upload an image. 
2.	Display the uploaded image. 
3.	Display image details such as filename and file size. 
4.	Provide an image preview. 
5.	Allow the user to select the grid dimension. 
6.	Divide the image into puzzle pieces. 
7.	Randomly shuffle the puzzle pieces. 
8.	Display the scrambled pieces. 
9.	Allow the user to select pieces for each position. 
10.	Check the manually entered solution. 
11.	Display a success message when the solution is correct. 
12.	Display an error message when the solution is incorrect. 
13.	Provide an automated hint. 
14.	Display step-by-step solution instructions. 


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



Non-Functional Requirements
Performance
The system should generate puzzle pieces and process normal-sized images within a reasonable amount of time.

Usability
The interface should be simple enough for a beginner to understand.

Reliability
The application should handle normal image uploads and puzzle operations without unexpected failures.

Maintainability
The puzzle-generation logic is separated into grid.py, while the main application is maintained in home.py.

Portability
The application should be able to run on systems supporting Python and Streamlit.

Scalability
The project structure should allow additional puzzle sizes and solving methods to be added in the future.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 System Architecture
The system follows a simple modular architecture:
              ┌───────────────────┐
              │       User        │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │ Streamlit UI      │
              │     home.py       │
              └─────────┬─────────┘
                        │
              ┌─────────▼─────────┐
              │ Image Processing  │
              │     Pillow        │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │ Puzzle Generation │
              │     grid.py       │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │ Scrambling /      │
              │ Solution Checking │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │ Results / Hint    │
              └───────────────────┘




--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



Design Diagrams
 Use Case Diagram
Actors:
•	User 
Use Cases:
•	Upload Image 
•	Preview Image 
•	Select Grid 
•	Generate Puzzle 
•	View Scrambled Puzzle 
•	Arrange Pieces 
•	Check Solution 
•	Get Hint 
•	View Solution Steps 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
                    ┌─────────────────────────────┐
                    │ Automated Image Puzzle      │
                    │          System             │
                    │                             │
User ──────────────►│ Upload Image                │
User ──────────────►│ Preview Image               │
User ──────────────►│ Select Grid                 │
User ──────────────►│ Generate Puzzle             │
User ──────────────►│ View Scrambled Puzzle       │
User ──────────────►│ Arrange Pieces              │
User ──────────────►│ Check Solution              │
User ──────────────►│ Get Hint                    │
User ──────────────►│ View Solution Steps         │
                    └─────────────────────────────┘
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Workflow Diagram

START
  │
  ▼
Upload Image
  │
  ▼
Show Image Preview
  │
  ▼
Select Grid Dimension
  │
  ▼
Divide Image into Pieces
  │
  ▼
Shuffle Pieces
  │
  ▼
Display Scrambled Puzzle
  │
  ▼
User Arranges Pieces
  │
  ▼
Check Solution
  │
  ├──────── Correct ───────► Success
  │
  └──────── Incorrect ─────► Try Again
                                │
                                ▼
                           Get Hint
                                │
                                ▼
                         Show Solution


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Algorithm
Algorithm: Automated Image Puzzle System
Input: An image uploaded by the user and selected grid dimension g.
Output: Scrambled puzzle, solution verification, and automated solution steps.
Steps
1.	Start the application. 
2.	Display the Streamlit interface. 
3.	Ask the user to upload an image. 
4.	Check whether an image has been uploaded. 
5.	If an image is uploaded, display its filename and file size. 
6.	Allow the user to preview the uploaded image. 
7.	Allow the user to select the grid dimension: 
o	2 × 2 
o	3 × 3 
8.	Open the uploaded image using Pillow. 
9.	Convert the image into RGB format. 
10.	Resize the image to 600 × 600 pixels. 
11.	Send the image and selected grid dimension to the grid.py module. 
12.	Divide the image into equal-sized puzzle pieces. 
13.	Store the original puzzle pieces. 
14.	Create a copy of the puzzle pieces. 
15.	Randomly shuffle the copied pieces using random.shuffle(). 
16.	Store the scrambled pieces using Streamlit session state. 
17.	Display the scrambled puzzle pieces. 
18.	Provide selection boxes for the user to arrange the pieces. 
19.	Store the user's selected arrangement. 
20.	When Check Solution is clicked, compare each selected piece with the corresponding original piece. 
21.	If all pieces match: 
•	Display a success message. 
•	Display balloons. 
22.	Otherwise: 
•	Display an error message. 
•	Ask the user to rearrange the pieces or use the hint. 
23.	If Get Hint is selected: 
•	Compare every original piece with every scrambled piece. 
•	Use tobytes() to compare the image data. 
•	Find the scrambled position corresponding to each original piece. 
24.	Store the resulting solution order. 
25.	Display the solution step-by-step. 
26.	End the process.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



Pseudocode
START
Upload Image
IF image is uploaded THEN
    Display image details
    Display preview
    Select grid dimension
    Open image
    Convert image to RGB
    Resize image to 600 × 600
    Generate puzzle pieces
    Store original pieces
    Copy puzzle pieces
    Shuffle copied pieces
    Display scrambled pieces
    User selects piece for each position
    IF Check Solution is clicked THEN
        Compare selected pieces
        with original pieces
        IF all pieces match THEN
            Display "Wow, You winned"
        ELSE
            Display "ohh, You loosed"
        END IF
    END IF
    IF Get Hint is clicked THEN
        FOR every original piece
            Find matching piece
            in scrambled pieces
            Store its position
        END FOR
        Display solution steps
    END IF
END IF
END

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




Sequence Diagram
┌────────┐       ┌──────────────┐       ┌──────────┐       ┌─────────┐
│  User  │       │  home.py     │       │ grid.py  │       │ Pillow  │
└───┬────┘       └──────┬───────┘       └────┬─────┘       └────┬────┘
    │                   │                    │                  │
    │ Upload Image      │                    │                  │
    ├──────────────────►│                    │                  │
    │                   │ Open Image         │                  │
    │                   ├──────────────────────────────────────►│
    │                   │                    │                  │
    │ Select Grid Size  │                    │                  │
    ├──────────────────►│                    │                  │
    │                   │ Generate Pieces    │                  │
    │                   ├───────────────────►│                  │
    │                   │                    │ Crop Image       │
    │                   │                    ├─────────────────►│
    │                   │                    │                  │
    │                   │                    │◄─────────────────┤
    │                   │◄───────────────────┤                  │
    │                   │  Puzzle Pieces     │                  │
    │                   │                    │                  │
    │ Generate Puzzle   │                    │                  │
    ├──────────────────►│                    │                  │
    │                   │ Shuffle Pieces     │                  │
    │                   │                    │                  │
    │                   │ Store in Session   │                  │
    │                   │ State              │                  │
    │                   │                    │                  │
    │◄──────────────────┤                    │                  │
    │ Scrambled Puzzle  │                    │                  │
    │                   │                    │                  │
    │ Arrange Pieces    │                    │                  │
    ├──────────────────►│                    │                  │
    │                   │                    │                  │
    │ Check Solution    │                    │                  │
    ├──────────────────►│                    │                  │
    │                   │ Compare Pieces    │                  │
    │                   │                    │                  │
    │◄──────────────────┤                    │                  │
    │ Result / Hint     │                    │                  │
    │                   │                    │                  │
    └───────────────────┴────────────────────┴──────────────────┘

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Class/Component Diagram
                         ┌─────────────────────────┐
                         │          USER           │
                         └────────────┬────────────┘
                                      │
                                      ▼
                 ┌────────────────────────────────────┐
                 │             home.py                │
                 │                                    │
                 │  • Streamlit User Interface        │
                 │  • Image Upload                     │
                 │  • Image Preview                    │
                 │  • Grid Selection                   │
                 │  • Puzzle Generation                │
                 │  • Random Scrambling                │
                 │  • Manual Solution                  │
                 │  • Solution Checking                │
                 │  • Automated Hint                  │
                 └──────────────┬─────────────────────┘
                                │
                         imports / calls
                                │
                                ▼
                 ┌────────────────────────────────────┐
                 │              grid.py               │
                 │                                    │
                 │  Function: f(g, d, originalimg)    │
                 │                                    │
                 │  • Calculate piece size             │
                 │  • Crop image                       │
                 │  • Create puzzle pieces             │
                 │  • Return pieces                    │
                 └──────────────┬─────────────────────┘
                                │
                                ▼
                 ┌────────────────────────────────────┐
                 │             Pillow                 │
                 │                                    │
                 │  • Image.open()                    │
                 │  • Image.convert()                 │
                 │  • Image.resize()                  │
                 │  • Image.crop()                    │
                 │  • ImageDraw                       │
                 │  • Image.tobytes()                 │
                 └────────────────────────────────────┘

                 ┌────────────────────────────────────┐
                 │        Python Built-ins            │
                 │                                    │
                 │  • random.shuffle()                │
                 │  • range()                         │
                 │  • enumerate()                     │
                 │  • len()                           │
                 └────────────────────────────────────┘
.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ER Diagram
There is:
•	No MySQL database 
•	No SQLite database 
•	No MongoDB 
•	No external database 
•	No permanent user-data storage 
Therefore, an ER diagram is not applicable.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




Design Decisions & Rationale
Python
Python was selected because it provides simple syntax and has libraries suitable for image processing and application development.

Streamlit
Streamlit was selected to create an interactive web interface without requiring a separate HTML, CSS, or JavaScript frontend.




Pillow
Pillow is used for:
•	Opening images 
•	Resizing images 
•	Cropping images 
•	Creating image objects 
•	Comparing image pieces 
•	
Separate grid.py
Puzzle-piece generation is separated from the main application to make the project modular and easier to maintain.

Random Shuffling
Python's random.shuffle() is used to create a different puzzle arrangement.

Session State
Streamlit's session_state is used to preserve puzzle pieces and the scrambled puzzle between interactions.



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





Implementation Details
The project consists mainly of two Python files.
home.py
The main application performs:
Image Upload
      ↓
Image Preview
      ↓
Grid Selection
      ↓
Puzzle Generation
      ↓
Random Shuffling
      ↓
Manual Arrangement
      ↓
Solution Checking
      ↓
Automated Hint

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



Important libraries used:

import streamlit as st
from PIL import Image, ImageDraw
import time
import random

grid.py
The grid.py module contains the function:
f(g, d, a):
This function divides the resized image into smaller pieces based on the selected grid dimension





For example:
3 × 3 grid
┌────┬────┬────┐
│  1 │  2 │  3 │
├────┼────┼────┤
│  4 │  5 │  6 │
├────┼────┼────┤
│  7 │  8 │  9 │
└────┴────┴────┘
The pieces are then copied and shuffled.







--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




Screenshots / Results


Main Interface
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/85aa566c-6de5-4dff-b4b0-0b7a5a27e337" />

Uploaded Image
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/bbd8ad95-220c-4f78-8a4d-31004cd31529" />
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/ddfce5d5-e63d-4b40-a6e0-bb20be3a9dc2" />
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/fbea7b29-05a8-4d5f-b5c8-3bf3f7e87f6e" />

Generated Puzzle
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/42e8c440-b755-4952-8c9b-ac05023f7a20" />

Wrong Solution
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/1c4cf9a3-043d-465a-9a1c-b952c49bf715" />

Automated Hint
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/b3d4ed59-5d9a-4006-aea2-d6e95728caca" />


Correct Solution
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/cbb79f77-fb86-4323-bab3-1023a72cfd32" />
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/8b14ea91-fd9d-4632-bd45-55c4b8a020c1" />

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Testing Approach
Testing was performed by checking the application with different images and grid dimensions.
Test	Input	Expected Result
Image Upload	JPG/PNG	Image uploaded
Preview	Uploaded image	Image displayed
2 × 2 Grid	Image + 2×2	4 pieces
3 × 3 Grid	Image + 3×3	9 pieces
Generate	Valid image	Scrambled puzzle
Correct Solution	Correct arrangement	Success message
Wrong Solution	Incorrect arrangement	Error message
Get Hint	Generated puzzle	Solution steps
Different Images	Multiple images	Puzzle generated

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 Challenges Faced
During development, several challenges were encountered.
Image Division
Dividing the image into equal puzzle pieces required correct calculation of the coordinates for cropping.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Random Scrambling
The puzzle pieces needed to be shuffled while preserving the original pieces for later comparison.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Maintaining Data
Streamlit reruns the Python script when the user interacts with the interface. Therefore, st.session_state was used to preserve puzzle information.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Solution Comparison
The program compares the image pieces using:
tobytes()
This allows the program to check whether two image pieces contain identical pixel data.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


User Interaction
Creating an interface where the user can select a piece for every puzzle position required multiple Streamlit selection boxes.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Learnings & Key Takeaways
•	Python programming 
•	Functions and modules 
•	Importing custom Python modules 
•	Image processing using Pillow 
•	Image cropping and resizing 
•	Lists and list operations 
•	Randomization using random.shuffle() 
•	Streamlit application development 
•	Streamlit session state 
•	User input handling 
•	Conditional statements 
•	Comparing image data 
•	Basic software project organization 
•	Testing and debugging 
•	GitHub project organization 


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 Future Enhancements
The following features can be added in future versions:
1.	Support for larger grids such as 4 × 4 and 5 × 5. 
2.	Drag-and-drop puzzle pieces. 
3.	Automatic puzzle solving without requiring a hint button. 
4.	Puzzle solving based on image similarity. 
5.	Puzzle difficulty levels. 
6.	Timer and score system. 
7.	Puzzle completion percentage. 
8.	Similarity percentage between original and solved images. 
9.	Support for additional image formats. 
10.	Object detection-based puzzle solving. 
11.	Improved image-matching algorithms. 
12.	Saving puzzle results for later use.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    
 References
1.	Python Documentation
https://docs.python.org/ 
2.	Streamlit Documentation
https://docs.streamlit.io/ 
3.	Pillow Documentation
https://pillow.readthedocs.io/ 
4.	Python random Module Documentation
https://docs.python.org/3/library/random.html 
5.	Python time Module Documentation
https://docs.python.org/3/library/time.html 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------











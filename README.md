Project Tittle:
Automated Image Puzzle Reconstruction and Solving System

Overview of the project
The Automated Image Puzzle System is a Python-based project that takes an uploaded image and converts it into a puzzle by dividing it into smaller pieces and rearranging them randomly. The system provide an interface in which the user himself can solve the pussel by assigning the number to each image as well as the system then automatically reconstructs the scrambled puzzle back into its original arrangement if asked by the user. It provides a simple and interactive web interface using Streamlit. The project demonstrates basic concepts of image processing, Python programming, randomization, and web application development. 

Features of the programme:
Upload an image from your device
Preview of the original image
Divide the image into smaller puzzle pieces. 
Automatically scramble the puzzle pieces. 
Display the scrambled puzzle.
 Automatically solve/reconstruct the puzzle. 
Display the reconstructed image.
Show puzzle information and solving results. 
Interactive interface using Streamlit.

Technologies Used
Tools Used  
Programming Language – Python
Framework – Streamlit
Libraries 
PIL (Pillow)  Used for image processing and manipulation. 
Random – Used for randomly rearranging puzzle pieces. 
Time – Used for measuring/displaying solving time. 

Development Tools 
 Python 
Streamlit 
VS Code / Python IDE 
Web Browser


Installation

Step 1: Install Python
Download and install Python from the official Python website.

Step 2: Install Required Libraries
Open Command Prompt or Terminal and run:
pip install streamlit pillow


How to Run the Project

Step 1: Open the Project Folder
Open Terminal .

Step 2: Run the Streamlit Application
Run:
streamlit run home.py

Step 3: Open the Application
Streamlit will start the local web server.


Instructions for Testing
Use the following procedure to test the Automated Image Puzzle System 

1. Start the Application
Open the project folder in Command Prompt/Terminal and run:
streamlit run home.py

The application will open in the browser.

2. Test Image Upload
1.	Click "Click here to upload an image". 
2.	Select a .jpg, .jpeg, or .png image. 
3.	Check that: 
o	The filename is displayed. 
o	The uploaded file size is displayed. 

3. Test Image Preview
1.	Upload an image. 
2.	Click "Show preview". 

Expected result:
The original uploaded image should appear with the caption:
Preview

4. Test Grid Dimension
Use the sidebar option:
Grid Dimension = Test both available values:
•	2 × 2 
•	3 × 3 

Expected result:
For:
2 × 2 → 4 puzzle pieces
3 × 3 → 9 puzzle pieces
The application should display: Generated 4 puzzle pieces or Generated 9 puzzle pieces.

5. Test Puzzle Generation
1.	Upload an image. 
2.	Select a grid dimension. 
3.	Click "Generate puzzle" in the sidebar. 

Expected result:
The application should:
•	Divide the image into pieces. 
•	Randomly shuffle the pieces. 
•	Display the "Let's Solve The Puzzle" section. 
•	Display the scrambled puzzle pieces. 
•	Display position selection boxes. 

6. Test Manual Puzzle Solving
After generating the puzzle:
1.	Look at the displayed scrambled pieces. 
2.	Use the Position 1, Position 2, Position 3... selection boxes. 
3.	Select the piece number you think belongs in each position. 
4.	Click "Check Solution". 

Correct arrangement
If all pieces are placed correctly: Wow, You winned and balloons should appear.

Incorrect arrangement
If one or more pieces are incorrect: ohh, You loosed
The application should also display a message asking you to rearrange the pieces.

7. Test Automated Hint/Solution
1.	Generate a puzzle. 
2.	Click "Get Hint" in the sidebar. 
3.	The program compares the scrambled pieces with the original pieces. 

Expected result:
The application should display: Puzzel solution found
Then the Solution of the Problem section should appear.
Example:
Step 1: Place Piece 5 at Position 1
Step 2: Place Piece 2 at Position 2
Step 3: Place Piece 8 at Position 3

8. Test Different Images
Repeat the above tests with different images, such as:
•	Landscape 
•	Building 
•	Animal 
•	Object 
•	Nature 
Expected result: The system should generate and solve the puzzle for each uploaded image.

9. Test Invalid/Edge Cases
Test Case	Input	Expected Result
TC01	No image uploaded	Puzzle should not be generated
TC02	JPG image	Image should upload successfully
TC03	PNG image	Image should upload successfully
TC04	2×2 grid	4 pieces generated
TC05	3×3 grid	9 pieces generated
TC06	Correct manual arrangement	Success message + balloons
TC07	Incorrect arrangement	Error message
TC08	Get Hint	Solution steps displayed
TC09	Different image	New puzzle generated
TC10	Generate puzzle multiple times	Pieces should be randomly rearranged


Overall Testing Flow
Run home.py
      ↓
Upload Image
      ↓
Show Preview
      ↓
Select Grid Dimension
      ↓
Generate Puzzle
      ↓
Check Scrambled Pieces
      ↓
Manual Arrangement
      ↓
Check Solution
      ↓
Correct? ── Yes ──→ Success + Balloons
   │
   No
   ↓
Try Again / Get Hint
      ↓
Get Hint
      ↓
Solution Steps Displayed


Expected Final Result
The project should successfully demonstrate:
Image → Puzzle Pieces → Random Scrambling → Manual Solving → Solution Checking → Automated Hint/Solution




Screenshots / Results

Main Interface
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/de19a477-1d8b-42df-a27d-18b87a3aa1b2" />

Uploaded Image
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/d0e052d7-2f6a-4a3d-a72b-ec07b298b2e0" />
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/ef63433f-d5f3-42b5-86d0-93a43ac2dbf1" />
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/18006ad8-e0db-4da4-8317-48f8048c51c2" />

Generated Puzzle
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/b871f3aa-bc3d-4309-8069-33631311de49" />

Wrong Solution
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/85299096-12cf-4d63-b474-100b200a3e92" />

Automated Hint
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/c84cb97d-0c72-47b4-a7fb-f8d997c6e51d" />

Correct Solution
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/2b5dd06f-72e8-45e1-bcbe-feb8883101cf" />
<img width="1014" height="633" alt="image" src="https://github.com/user-attachments/assets/32bfd5aa-65c2-4962-9525-5e174d92eefb" />


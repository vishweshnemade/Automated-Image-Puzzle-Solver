import streamlit as st
from PIL import Image, ImageDraw
import time 
import random

#using the module instlled using PIP
#consit of user defined as well as built in function

st.set_page_config(page_title="Automated Image Puzzle Solver", page_icon="🧩", layout="wide")
#setting up layout

#setting up Header
#settingg up tittle
st.text("")
st.header("Lets Solve a Puzzle")
st.text("")
st.title("🧩 Automated Image Puzzle System")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.header("Upload image here")


#LETS SET UP COLUMN
col1, col2, col3 = st.columns(3)

#selecting first column
with col1:
    #let's upload an image
    a = st.file_uploader("Click here to upload an image")

#setting up second column
with col2:
    pass

#setting up third column
with col3:
    if a is not None:
        #this is a code to set up the rectangle in the form of pictorial image
        img = Image.new("RGB", (300, 100), "black")
        #here image is a module
        draw = ImageDraw.Draw(img)
        draw.rectangle([10,10,490,120], outline="white")
        #assigning the colour to it
        draw.text((20, 20), "Details of the uploaded image", fill="white")
        #setting up orientation of the rectangle on the basis of the coordinates
        draw.text((20, 45), f"Filename: {a.name}", fill="white")
        draw.text((20, 60), f"Size of image uploaded: {a.size} bytes", fill="white")
        #setting up orientation of the text and rectangle on the basis of the coordinates
        st.image(img)

#applying condition
if a is not None:
    #setting up the button so that when we will click on it it will solve the problem
    if st.button("Show preview"):
        preview = Image.open(a)
        #command to see preview of the uploaded image
        st.image(preview, caption="Preview") 

g = st.sidebar.slider("Grid Dimension = ", 2, 3, 3)
#it sets up the slider insted of writting or typing of the grid proportion we can slid it to get the proportion of the grid

if a is not None:
    #resizing the image 
    originalimg = Image.open(a).convert("RGB")
    #d refers to the dimensions
    d = 600
    originalimg = originalimg.resize((d, d))

    import grid
    #importing grid.py

    pieces = grid.f(g, d, originalimg)
    st.write(f"Generated {len(pieces)} puzzle pieces.")

    if st.sidebar.button("Generate puzzle"):
        #sets up data in the sidebar
        #stores pices in session state
        st.session_state.pieces = pieces.copy()
        #create a scramnbled puzzle
        scrambled = pieces.copy()
        random.shuffle(scrambled)
        st.session_state.scrambled = scrambled
        #start manual solution
        st.session_state.solution = [None]*len(scrambled)

    #####  Manual Solving  ######
    if "scrambled" in st.session_state:
        st.header("Let's Solve The Puzzle")
        #setting up header
        #helps in scrambliing the image
        scrambled = st.session_state.scrambled
        st.write("moove the puzzle pieces to arrange them")
        #display Scrambled pices
        st.subheader("puzzle pieces")

        
     
       
        for i, place in enumerate(scrambled):
            if i%9 == 0:
                #setting up the column
                cols = st.columns(9)
            with cols[i%9]:
                st.image(place, width=80)   

        st.subheader("Arrange the puzzle")      

        #store selected pices
        selected = []  

        for row in range(g):
            cols = st.columns(g)
            #setting up
            for col in range(g):
                position = row*g + col

                with cols[col]:
                    #setting up select box
                    choise = st.selectbox(f"Position{position + 1}", range(1, len(scrambled)+1), key=f"position_{position}")
                    selected.append(choise - 1)

        #lets make a check 
        if st.sidebar.button("Check Solution"):
            #setting up the button in the sidebar
            original_pieces = st.session_state.pieces
            #storing the value in session state
            user_order_correct = True

            for pos, scrambled_idx in enumerate(selected):
                #erunmate stores multiple values
                user_piece = scrambled[scrambled_idx]
                target_piece = original_pieces[pos]
                if user_piece.tobytes() != target_piece.tobytes():
                    user_order_correct = False
                    break

            if user_order_correct:    
            #correct = list(range(len(pieces))) 
                st.success("Wow, You winned") 
                #if succes it gives green
                st.balloons()
            else:
                #erroe gives error print on such condition
                st.error("ohh, You loosed")
                st.write("Try again or get Hints using Automated System")
   #         if selected == correct:    
   #             st.success("Wow, You winned") 
   #             st.balloons()
   #         else:
   #             st.error("ohh, You loosed")

                       

#####    automated system    #####
        st.text("")
        st.text("")
        st.text("")
        #wriiten to increase the space
        st.text("")
        if "scrambled" in st.session_state:
            if st.sidebar.button("Get Hint"):
                scrambled = st.session_state.scrambled
                original = st.session_state.pieces
                #find where every unscramble pice belong
                solution = []

                for original_piece in original:
                    #checking the codition if available
                    for j, scrambled_piece in enumerate(scrambled):
                        if scrambled_piece.tobytes() == original_piece.tobytes():
                        #tobytes() is a method in Pillow (PIL) used to convert an image into a raw sequence of bytes.
                            solution.append(j)
                            break

                st.session_state.solution = solution
                #assing value in solution
                st.success("Puzzel solution found")

##showing the solution steps

#if not in quets
#"Look for whatever value is currently inside the Python variable solution."
                if "solution" in st.session_state:
                    st.title("Solution of the Problem")
                    #setting up tittle
                    st.text("")
                    st.text("")
                    st.subheader("Let's see solution steps")
                    #setting up subheader
                    solution = st.session_state.solution

                    #simplifing condition if can be applied

                    for i, piece_number in enumerate(solution):
                        st.write(
                                f"Step {i + 1}: "
                                f"Place Piece {piece_number + 1} "
                                f"at Position {i + 1}"
                                )

st.text("")
st.text("")
st.text("")
st.text("")
st.text("Vishwesh Nemade")


             





       







        


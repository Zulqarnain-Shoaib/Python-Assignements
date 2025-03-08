import streamlit as st
import random

def new_game():
    st.session_state.target = random.randint(st.session_state.low, st.session_state.high)
    st.session_state.attempts = 0
    st.session_state.game_over = False

def check_guess():
    if st.session_state.game_over:
        return
    
    guess = st.session_state.guess
    st.session_state.attempts += 1
    if guess < st.session_state.target:
        st.session_state.feedback = "Too low!"
    elif guess > st.session_state.target:
        st.session_state.feedback = "Too high!"
    else:
        st.session_state.feedback = f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts."
        st.session_state.game_over = True

st.title("🔢 Number Guessing Game")

# Difficulty selection
st.session_state.low = st.number_input("Enter lower bound:", value=1)
st.session_state.high = st.number_input("Enter upper bound:", value=100)
st.button("Start New Game", on_click=new_game)

# Game play
if "target" in st.session_state:
    st.number_input("Your Guess:", key="guess")
    st.button("Submit Guess", on_click=check_guess)
    if "feedback" in st.session_state:
        st.write(st.session_state.feedback)
        
    st.write(f"Attempts: {st.session_state.attempts}")

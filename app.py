import streamlit as st
import random

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Janu's Rock Paper Scissors Game",
    page_icon="🎮",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "draw_score" not in st.session_state:
    st.session_state.draw_score = 0

if "round_number" not in st.session_state:
    st.session_state.round_number = 0

if "user_choice" not in st.session_state:
    st.session_state.user_choice = None

if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = None

if "result" not in st.session_state:
    st.session_state.result = ""

if "history" not in st.session_state:
    st.session_state.history = []


# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #667eea 0%,
        #764ba2 50%,
        #f093fb 100%
    );
    min-height: 100vh;
}

.main-title {
    text-align: center;
    color: white;
    font-size: 42px;
    font-weight: bold;
    margin-top: 10px;
}

.subtitle {
    text-align: center;
    color: #f5f5f5;
    font-size: 18px;
    margin-bottom: 25px;
}

.game-card {
    background: rgba(255,255,255,0.95);
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.20);
    margin-bottom: 20px;
}

.choice-card {
    background: white;
    border-radius: 20px;
    padding: 20px;
    text-align: center;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.12);
}

.choice-emoji {
    font-size: 65px;
}

.choice-name {
    font-size: 22px;
    font-weight: bold;
    color: #4f46e5;
}

.result-box {
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    font-size: 25px;
    font-weight: bold;
    margin: 20px 0;
}

.win {
    background: #dcfce7;
    color: #166534;
}

.lose {
    background: #fee2e2;
    color: #991b1b;
}

.draw {
    background: #fef3c7;
    color: #92400e;
}

.score-title {
    color: white;
    text-align: center;
    font-size: 25px;
    font-weight: bold;
}

.footer {
    text-align: center;
    color: white;
    margin-top: 30px;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- GAME FUNCTIONS ----------------
choices = ["Rock", "Paper", "Scissors"]

emoji = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}


def find_winner(user, computer):

    if user == computer:
        return "draw"

    if (
        (user == "Rock" and computer == "Scissors")
        or
        (user == "Paper" and computer == "Rock")
        or
        (user == "Scissors" and computer == "Paper")
    ):
        return "user"

    return "computer"


# ---------------- TITLE ----------------
st.markdown(
    '<div class="main-title">🎮 Janu\'s Rock Paper Scissors Game</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Choose your weapon and challenge the computer! 🔥</div>',
    unsafe_allow_html=True
)


# ---------------- SCORE BOARD ----------------
st.markdown(
    '<div class="score-title">🏆 SCORE BOARD</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "👤 You",
        st.session_state.user_score
    )

with col2:
    st.metric(
        "🤖 Computer",
        st.session_state.computer_score
    )

with col3:
    st.metric(
        "🤝 Draws",
        st.session_state.draw_score
    )


# ---------------- GAME AREA ----------------
st.markdown('<div class="game-card">', unsafe_allow_html=True)

st.subheader("🎯 Choose Your Move")

user_choice = st.radio(
    "Select one:",
    choices,
    horizontal=True
)

st.markdown("</div>", unsafe_allow_html=True)


# ---------------- PLAY BUTTON ----------------
if st.button(
    "🔥 PLAY ROUND",
    use_container_width=True
):

    computer_choice = random.choice(choices)

    result = find_winner(
        user_choice,
        computer_choice
    )

    # Save choices
    st.session_state.user_choice = user_choice
    st.session_state.computer_choice = computer_choice
    st.session_state.result = result

    # Increase round
    st.session_state.round_number += 1

    # Update score
    if result == "user":
        st.session_state.user_score += 1

    elif result == "computer":
        st.session_state.computer_score += 1

    else:
        st.session_state.draw_score += 1

    # Save history
    st.session_state.history.append({
        "Round": st.session_state.round_number,
        "You": user_choice,
        "Computer": computer_choice,
        "Result": result
    })


# ---------------- SHOW RESULT ----------------
if st.session_state.user_choice is not None:

    st.markdown("---")

    st.subheader("⚔️ Battle Result")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class="choice-card">
                <div>You</div>
                <div class="choice-emoji">
                    {emoji[st.session_state.user_choice]}
                </div>
                <div class="choice-name">
                    {st.session_state.user_choice}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="choice-card">
                <div>Computer</div>
                <div class="choice-emoji">
                    {emoji[st.session_state.computer_choice]}
                </div>
                <div class="choice-name">
                    {st.session_state.computer_choice}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # ---------------- RESULT MESSAGE ----------------

    if st.session_state.result == "user":

        st.markdown(
            """
            <div class="result-box win">
                🎉 YOU WIN! 🎉
                <br>
                🔥 Amazing! You defeated the computer!
            </div>
            """,
            unsafe_allow_html=True
        )

        st.balloons()

        st.success(
            "🏆 Champion! Keep going — you're on fire!"
        )

    elif st.session_state.result == "computer":

        st.markdown(
            """
            <div class="result-box lose">
                🤖 COMPUTER WINS!
                <br>
                💪 Don't give up! Try another round!
            </div>
            """,
            unsafe_allow_html=True
        )

        st.warning(
            "🔥 Cheer up! You can beat the computer next round!"
        )

    else:

        st.markdown(
            """
            <div class="result-box draw">
                🤝 IT'S A DRAW!
                <br>
                ⚡ Both players chose the same move!
            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(
            "😎 Nice battle! Try again and become the champion!"
        )


# ---------------- OVERALL WINNER ----------------
if st.session_state.round_number > 0:

    st.markdown("---")

    st.subheader("🏆 Current Champion")

    if (
        st.session_state.user_score
        > st.session_state.computer_score
    ):

        st.success(
            f"👑 You are leading! "
            f"{st.session_state.user_score} - "
            f"{st.session_state.computer_score}"
        )

    elif (
        st.session_state.computer_score
        > st.session_state.user_score
    ):

        st.error(
            f"🤖 Computer is leading! "
            f"{st.session_state.computer_score} - "
            f"{st.session_state.user_score}"
        )

    else:

        st.info("🤝 The match is currently tied!")


# ---------------- GAME HISTORY ----------------
if len(st.session_state.history) > 0:

    st.markdown("---")

    st.subheader("📜 Match History")

    for match in reversed(
        st.session_state.history[-5:]
    ):

        if match["Result"] == "user":
            result_text = "🏆 You Won"

        elif match["Result"] == "computer":
            result_text = "🤖 Computer Won"

        else:
            result_text = "🤝 Draw"

        st.write(
            f"**Round {match['Round']}** | "
            f"You: {emoji[match['You']]} {match['You']} | "
            f"Computer: {emoji[match['Computer']]} "
            f"{match['Computer']} | "
            f"{result_text}"
        )


# ---------------- RESET GAME ----------------
st.markdown("---")

if st.button(
    "🔄 RESET GAME",
    use_container_width=True
):

    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.draw_score = 0
    st.session_state.round_number = 0
    st.session_state.user_choice = None
    st.session_state.computer_choice = None
    st.session_state.result = ""
    st.session_state.history = []

    st.rerun()


# ---------------- FOOTER ----------------
st.markdown(
    """
    <div class="footer">
        🎮 Janu's Rock Paper Scissors Game
        <br>
        Built with ❤️ using Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
import streamlit as st
import random

tab_Mindtree, tab_lorenz, tab_decision = st.tabs(
    ["MindTree", "Expectation Model", "Decision Model"]
)

# ----------------- TAB 1: MINDTREE -----------------
with tab_Mindtree:
    st.title("MindTree")
    st.header("Step 1: Identify the emotion")

    class Mood:
        def __init__(self, options):
            self.selected = st.multiselect("What do you feel?", options)

    class Context:
        def __init__(self, options):
            self.selected = st.multiselect(
                "What was the context of your thoughts before?", options
            )

    class ThoughtPattern:
        def __init__(self, options):
            self.selected = st.multiselect(
                "What is current pattern of your thoughts?", options
            )

    Context_options_Happy = [
        "Playful", "Content", "Interested", "Proud",
        "Accepted", "Powerful", "Peaceful", "Trusting"
    ]

    Context_options_Sad = ["Lonely", "Vulnerable", "Despair", "Depressed", "Hurt"]

    Context_options_Angry = [
        "Let down", "Humiliated", "Bitter", "Mad",
        "Aggressive", "Frustrated", "Distant"
    ]

    Context_options_Disgusted = [
        "Critical", "Disapproving", "Disappointed", "Awful", "Repelled"
    ]

    Context_options_Fearful = [
        "Scared", "Anxious", "Insecure", "Weak", "Rejected", "Threatened"
    ]

    Context_options_Bad = ["Tired", "Stressed", "Busy", "Bored"]

    Context_options_Surprised = ["Startled", "Confused", "Amazed", "Excited"]

    Mood_options = [
        "Happy 😊", "Sad 😢", "Disgusted 🤢",
        "Angry 😡", "Fearful 😨", "Bad 😞", "Surprised 😲"
    ]

    mood_1 = Mood(Mood_options)

    context_1 = None
    thought_1 = None

    if "Happy 😊" in mood_1.selected:
        context_1 = Context(Context_options_Happy)

        if "Playful" in context_1.selected:
            thought_1 = ThoughtPattern(["Aroused", "Cheeky"])
        elif "Content" in context_1.selected:
            thought_1 = ThoughtPattern(["Free", "Joyful"])
        elif "Interested" in context_1.selected:
            thought_1 = ThoughtPattern(["Curious", "Inquisitive"])
        elif "Proud" in context_1.selected:
            thought_1 = ThoughtPattern(["Successful", "Confident"])
        elif "Accepted" in context_1.selected:
            thought_1 = ThoughtPattern(["Respected", "Valued"])
        elif "Powerful" in context_1.selected:
            thought_1 = ThoughtPattern(["Courageous", "Creative"])
        elif "Peaceful" in context_1.selected:
            thought_1 = ThoughtPattern(["Loving", "Thankful"])
        elif "Trusting" in context_1.selected:
            thought_1 = ThoughtPattern(["Sensitive", "Intimate"])

    elif "Sad 😢" in mood_1.selected:
        context_1 = Context(Context_options_Sad)

        if "Lonely" in context_1.selected:
            thought_1 = ThoughtPattern(["Isolated", "Abandoned"])
        elif "Vulnerable" in context_1.selected:
            thought_1 = ThoughtPattern(["Victimized", "Fragile"])
        elif "Despair" in context_1.selected:
            thought_1 = ThoughtPattern(["Grief", "Powerless"])
        elif "Depressed" in context_1.selected:
            thought_1 = ThoughtPattern(["Inferior", "Empty"])
        elif "Hurt" in context_1.selected:
            thought_1 = ThoughtPattern(["Guilty", "Remorseful"])

    elif "Angry 😡" in mood_1.selected:
        context_1 = Context(Context_options_Angry)

        if "Let down" in context_1.selected:
            thought_1 = ThoughtPattern(["Betrayed", "Resentful"])
        elif "Humiliated" in context_1.selected:
            thought_1 = ThoughtPattern(["Disrespected", "Ridiculed"])
        elif "Bitter" in context_1.selected:
            thought_1 = ThoughtPattern(["Indignant", "Violated"])
        elif "Mad" in context_1.selected:
            thought_1 = ThoughtPattern(["Furious", "Jealous"])
        elif "Aggressive" in context_1.selected:
            thought_1 = ThoughtPattern(["Provoked", "Hostile"])
        elif "Frustrated" in context_1.selected:
            thought_1 = ThoughtPattern(["Infuriated", "Annoyed"])
        elif "Distant" in context_1.selected:
            thought_1 = ThoughtPattern(["Withdrawn", "Numb"])

    elif "Disgusted 🤢" in mood_1.selected:
        context_1 = Context(Context_options_Disgusted)

        if "Critical" in context_1.selected:
            thought_1 = ThoughtPattern(["Judgmental", "Embarrassed"])
        elif "Disapproving" in context_1.selected:
            thought_1 = ThoughtPattern(["Appalled", "Revolted"])
        elif "Disappointed" in context_1.selected:
            thought_1 = ThoughtPattern(["Detestable", "Horrified"])
        elif "Awful" in context_1.selected:
            thought_1 = ThoughtPattern(["Nauseated", "Hesitant"])
        elif "Repelled" in context_1.selected:
            thought_1 = ThoughtPattern(["Revolted", "Horrified"])

    elif "Fearful 😨" in mood_1.selected:
        context_1 = Context(Context_options_Fearful)

        if "Scared" in context_1.selected:
            thought_1 = ThoughtPattern(["Frightened", "Helpless"])
        elif "Anxious" in context_1.selected:
            thought_1 = ThoughtPattern(["Overwhelmed", "Worried"])
        elif "Insecure" in context_1.selected:
            thought_1 = ThoughtPattern(["Inadequate", "Worthless"])
        elif "Weak" in context_1.selected:
            thought_1 = ThoughtPattern(["Insignificant", "Excluded"])
        elif "Rejected" in context_1.selected:
            thought_1 = ThoughtPattern(["Persecuted", "Exposed"])
        elif "Threatened" in context_1.selected:
            thought_1 = ThoughtPattern(["Nervous", "Exposed"])

    elif "Bad 😞" in mood_1.selected:
        context_1 = Context(Context_options_Bad)

        if "Tired" in context_1.selected:
            thought_1 = ThoughtPattern(["Sleepy", "Unfocused"])
        elif "Stressed" in context_1.selected:
            thought_1 = ThoughtPattern(["Pressured", "Out of control"])
        elif "Busy" in context_1.selected:
            thought_1 = ThoughtPattern(["Unfocused", "Pressured"])
        elif "Bored" in context_1.selected:
            thought_1 = ThoughtPattern(["Apathetic", "Indifferent"])

    elif "Surprised 😲" in mood_1.selected:
        context_1 = Context(Context_options_Surprised)

        if "Startled" in context_1.selected:
            thought_1 = ThoughtPattern(["Shocked", "Dismayed"])
        elif "Confused" in context_1.selected:
            thought_1 = ThoughtPattern(["Disillusioned", "Hesitant"])
        elif "Amazed" in context_1.selected:
            thought_1 = ThoughtPattern(["Astonished", "Energetic"])
        elif "Excited" in context_1.selected:
            thought_1 = ThoughtPattern(["Eager", "Inspired"])

    if (
        mood_1.selected
        and context_1 is not None and context_1.selected
        and thought_1 is not None and thought_1.selected
    ):
        st.header("Step 2: Identify the Thinking Error")
        st.write("""
Black-and-white thinking: Seeing things in extreme terms.

Shoulding: Thinking the way we want things to be is the way they ought to be.

Overgeneralization: Believing that one instance applies to every situation.

Catastrophizing: Thinking a situation is much worse than it is.

Discounting the positive: Minimizing evidence that contradicts one’s negative automatic thoughts.

Emotional reasoning: Assuming our feelings convey useful information (feelings = facts).

Fortune telling: Making predictions based on scant information.

Mind reading: Assuming we know what someone else is thinking.

Personalization: Thinking events that have nothing to do with us are actually about us.

Entitlement: Expecting to reach a certain outcome based on our actions or position.

Outsourcing happiness: Giving outside factors the final say regarding our emotions.

False sense of helplessness: Believing we have less power than we actually do.

False sense of responsibility: Believing we have more power than we actually do.
""")

        distortions = [
            "Black-and-white thinking",
            "Shoulding",
            "Overgeneralization",
            "Catastrophizing",
            "Discounting the positive",
            "Emotional reasoning",
            "Fortune telling",
            "Mind reading",
            "Personalization",
            "Entitlement",
            "Outsourcing happiness",
            "False sense of helplessness",
            "False sense of responsibility"
        ]

        selected_distortion = st.multiselect(
            "Which thinking error fits your thought best?",
            distortions
        )

# ----------------- TAB 2: EXPECTATION MODEL -----------------
with tab_lorenz:
    st.title("Expectation Model")

    intentions = st.text_input("What are your intentions?")
    motives = st.text_input("What are your motives?")
    expectations = st.text_input("What are your expectations?")
    outcomes = st.text_input("What are the outcomes?")
    gradient = st.text_input("How does the difference make you feel?")

    if st.button("Show Reflection"):
        st.write(
            f"So you intended to {intentions}, because of {motives}, "
            f"and expected {expectations} but got {outcomes}, "
            f"and that made you feel {gradient}."
        )

# ----------------- TAB 3: DECISION MODEL -----------------
with tab_decision:
    st.title("Decision Model")

    question = st.text_input("Ask a question:")

    answers = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
    ]

    if st.button("Get Random Answer"):
        st.write("Magic 8 Ball says:", random.choice(answers))
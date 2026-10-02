import streamlit as st


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)


# ---------------------------------------------------------
# ORIGINAL GRADING FUNCTION
# ---------------------------------------------------------

def get_grade(mark):
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark < 90:
        return "B"
    elif 70 <= mark < 80:
        return "C"
    elif 60 <= mark < 70:
        return "D"
    else:
        return "E"


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

# Streamlit reruns the entire program whenever the user
# interacts with the page.
#
# session_state keeps the student information between reruns.

if "students" not in st.session_state:
    st.session_state.students = []


# ---------------------------------------------------------
# CUSTOM EDUCATIONAL THEME
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    /* Main page background */

    .stApp {
        background:
            linear-gradient(
                135deg,
                #f8f5ed 0%,
                #fffdf8 50%,
                #f3efe5 100%
            );
    }


    /* Main content width */

    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* Main title */

    .main-title {
        font-family: Georgia, serif;
        font-size: 44px;
        font-weight: 700;
        color: #17324d;
        margin-bottom: 5px;
    }


    /* Subtitle */

    .subtitle {
        font-family: Georgia, serif;
        font-size: 18px;
        color: #7a6250;
        margin-bottom: 25px;
    }


    /* Top university style banner */

    .education-banner {
        background:
            linear-gradient(
                120deg,
                #17324d,
                #234e70
            );

        border-radius: 18px;
        padding: 28px 32px;

        box-shadow:
            0 12px 30px rgba(20, 40, 60, 0.15);

        border-bottom: 5px solid #c79a3b;

        margin-bottom: 28px;
    }


    .banner-small {
        color: #e9d8a6;
        font-size: 14px;
        letter-spacing: 2px;
        font-weight: 600;
    }


    .banner-title {
        font-family: Georgia, serif;
        color: white;
        font-size: 38px;
        font-weight: bold;
        margin-top: 4px;
    }


    .banner-text {
        color: #dce6ef;
        font-size: 16px;
    }


    /* Section headings */

    h2, h3 {
        font-family: Georgia, serif !important;
        color: #17324d !important;
    }


    /* Form */

    div[data-testid="stForm"] {

        background-color: rgba(255, 255, 255, 0.88);

        border: 1px solid #ddd3bf;

        border-radius: 18px;

        padding: 25px;

        box-shadow:
            0 8px 22px rgba(0, 0, 0, 0.06);
    }


    /* Inputs */

    .stTextInput input,
    .stNumberInput input {

        background-color: #fffdf8 !important;

        border: 1px solid #c9bda9 !important;

        border-radius: 10px !important;

        color: #17324d !important;

        font-size: 16px !important;
    }


    /* Main buttons */

    .stButton > button,
    .stFormSubmitButton > button {

        background:
            linear-gradient(
                120deg,
                #7b2334,
                #9b3549
            ) !important;

        color: white !important;

        border: none !important;

        border-radius: 10px !important;

        font-weight: 600 !important;

        height: 46px;

        transition: 0.2s;
    }


    .stButton > button:hover,
    .stFormSubmitButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
            0 8px 20px rgba(123, 35, 52, 0.25);
    }


    /* Metrics */

    div[data-testid="stMetric"] {

        background: white;

        border-radius: 14px;

        padding: 18px;

        border-top: 4px solid #c79a3b;

        box-shadow:
            0 7px 18px rgba(0,0,0,0.06);
    }


    div[data-testid="stMetricLabel"] {
        color: #7b2334;
        font-weight: 600;
    }


    div[data-testid="stMetricValue"] {
        color: #17324d;
        font-family: Georgia, serif;
    }


    /* Table */

    div[data-testid="stDataFrame"] {

        background-color: white;

        border-radius: 15px;

        padding: 8px;

        box-shadow:
            0 8px 20px rgba(0,0,0,0.05);
    }


    /* Helper text */

    .helper-text {

        padding: 14px 18px;

        background-color: #f4ead3;

        border-left: 5px solid #c79a3b;

        color: #554536;

        border-radius: 6px;

        margin-bottom: 20px;
    }


    /* Footer */

    .footer {

        text-align: center;

        color: #8b7b6b;

        font-family: Georgia, serif;

        border-top: 1px solid #ded5c5;

        margin-top: 40px;

        padding-top: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
"""
<div class="education-banner">
<div class="banner-small">ACADEMIC PERFORMANCE PORTAL</div>
<div class="banner-title">🎓 Student Grade Manager</div>
<div class="banner-text">Record student marks, calculate grades and monitor classroom performance.</div>
</div>
""",
unsafe_allow_html=True
)


# ---------------------------------------------------------
# PAGE COLUMNS
# ---------------------------------------------------------

left_column, right_column = st.columns(
    [1, 1.6],
    gap="large"
)


# ---------------------------------------------------------
# LEFT SIDE - STUDENT FORM
# ---------------------------------------------------------

with left_column:

    st.markdown("## ✏️ Add Student")

    st.markdown(
        """
        <div class="helper-text">
        Enter the student's name and mark below.
        Marks must be between <b>0 and 100</b>.
        </div>
        """,
        unsafe_allow_html=True
    )


    with st.form("add_student_form"):

        name = st.text_input(
            "Student Name",
            placeholder="Example: Divya"
        )


        mark = st.number_input(
            "Student Mark",
            min_value=0.0,
            max_value=100.0,
            value=75.0,
            step=1.0
        )


        submitted = st.form_submit_button(
            "➕ Add Student",
            use_container_width=True
        )


        if submitted:

            if not name.strip():

                st.error(
                    "Please enter the student's name."
                )

            else:

                grade = get_grade(mark)

                student = {
                    "Name": name.strip(),
                    "Mark": mark,
                    "Grade": grade
                }

                st.session_state.students.append(student)

                st.success(
                    f"{name} has been added successfully."
                )


    # -----------------------------------------------------
    # GRADING SCALE
    # -----------------------------------------------------

    st.markdown("### 📘 Grading Scale")

    st.markdown(
        """
        | Mark | Grade |
        |------|------:|
        | 90 – 100 | **A** |
        | 80 – 89 | **B** |
        | 70 – 79 | **C** |
        | 60 – 69 | **D** |
        | Below 60 | **E** |
        """
    )


# ---------------------------------------------------------
# RIGHT SIDE - CLASS RESULTS
# ---------------------------------------------------------

with right_column:

    st.markdown("## 📊 Class Overview")


    if st.session_state.students:

        # -------------------------------------------------
        # CALCULATIONS
        # -------------------------------------------------

        marks = [
            student["Mark"]
            for student in st.session_state.students
        ]

        average = sum(marks) / len(marks)

        highest = max(marks)

        lowest = min(marks)


        # -------------------------------------------------
        # CLASS METRICS
        # -------------------------------------------------

        metric1, metric2, metric3, metric4 = st.columns(4)


        metric1.metric(
            "Students",
            len(st.session_state.students)
        )


        metric2.metric(
            "Average",
            f"{average:.1f}"
        )


        metric3.metric(
            "Highest",
            f"{highest:g}"
        )


        metric4.metric(
            "Lowest",
            f"{lowest:g}"
        )


        st.markdown("### 📋 Student Results")


        # -------------------------------------------------
        # FORMAT TABLE
        # -------------------------------------------------

        display_students = []

        for number, student in enumerate(
            st.session_state.students,
            start=1
        ):

            student_mark = student["Mark"]

            # Display whole number without .0
            if float(student_mark).is_integer():
                student_mark = int(student_mark)


            display_students.append(
                {
                    "No.": number,
                    "Student Name": student["Name"],
                    "Mark": student_mark,
                    "Grade": student["Grade"]
                }
            )


        st.dataframe(
            display_students,
            use_container_width=True,
            hide_index=True
        )


        # -------------------------------------------------
        # CLEAR BUTTON
        # -------------------------------------------------

        st.markdown("")

        if st.button(
            "🗑️ Clear All Students",
            use_container_width=True
        ):

            st.session_state.students = []

            st.rerun()


    else:

        st.info(
            """
            No student records have been added yet.

            Add your first student using the form on the left.
            """
        )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">
        Student Grade Manager
        &nbsp; • &nbsp;
        Built with Python and Streamlit
        &nbsp; • &nbsp;
        Academic Dashboard
    </div>
    """,
    unsafe_allow_html=True
)
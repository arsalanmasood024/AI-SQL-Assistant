def load_css():
    return """
    <style>

    /* ---------- Main App ---------- */

    .main{
        background-color:#0E1117;
        color:white;
    }

    /* ---------- Hide Streamlit Menu ---------- */

    #MainMenu{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    header{
        visibility:hidden;
    }

    /* ---------- Buttons ---------- */

    .stButton>button{

        width:100%;

        height:48px;

        border-radius:10px;

        font-size:16px;

        font-weight:600;

        border:none;

        background:#4F46E5;

        color:white;

    }

    .stButton>button:hover{

        background:#6366F1;

    }

    /* ---------- Metric Cards ---------- */

    div[data-testid="metric-container"]{

        background:#161B22;

        border:1px solid #30363D;

        border-radius:12px;

        padding:15px;

    }

    /* ---------- DataFrame ---------- */

    div[data-testid="stDataFrame"]{

        border:1px solid #30363D;

        border-radius:10px;

        overflow:hidden;

    }

    /* ---------- Sidebar ---------- */

    section[data-testid="stSidebar"]{

        background:#161B22;

    }

    /* ---------- Code Block ---------- */

    pre{

        border-radius:10px;

    }

    /* ---------- Chat ---------- */

    div[data-testid="stChatMessage"]{

        border-radius:10px;

    }

    /* ---------- Download Buttons ---------- */

    div.stDownloadButton>button{

        width:100%;

        border-radius:10px;

    }

    </style>
    """
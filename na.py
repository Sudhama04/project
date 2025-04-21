import subprocess
import streamlit as st  # Ensure streamlit is imported here as well

notebook_path = 'project.ipynb' 
command = ['streamlit', 'run', notebook_path]

try:
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(timeout=10)

    if process.returncode == 0:
        st.success("Streamlit app is likely running. Check your browser (usually http://localhost:8501)")
        # The app will open in your web browser
    else:
        st.error(f"Error starting Streamlit:")
        st.error(stderr.decode('utf-8'))

except FileNotFoundError:
    st.error("Error: Streamlit command not found. Make sure Streamlit is installed and accessible.")
except subprocess.TimeoutExpired:
    st.warning("Streamlit app took too long to start.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
import streamlit as st
import time
import os
import json

def quiz_passed(module_number):
    st.balloons()
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')
    st.toast('You finished the module', icon='🫣')

    module_json_path = os.path.join(os.getcwd(),  "modules", f"module_{module_number}", "module.json")
    # Check if module.json exists
    if os.path.exists(module_json_path):
        # Read the existing data
        with open(module_json_path, "r") as f:
            module_data = json.load(f)
        
        # Update the relevant value (Example: Marking module as completed)
        module_data["progress"]["quiz_passed"] = True  # Fix: Access "progress" directly

        # Write the updated data back to module.json
        with open(module_json_path, "w") as f:
            json.dump(module_data, f, indent=4)
    else:
        st.error("Could not update progress.")

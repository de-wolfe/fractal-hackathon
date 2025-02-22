# Makefile for running a Streamlit application

.PHONY: run install clean

# Install dependencies from requirements.txt, if available.
install:
	pip3 install -r requirements.txt

# Run the Streamlit app.
run:
	streamlit run app.py

# (Optional) Clean up any temporary or cache files.
clean:
	@echo "Cleaning up..."
	# Add cleanup commands if necessary.


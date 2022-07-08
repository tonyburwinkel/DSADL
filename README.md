this is a quick script for downloading the CLRS DSA textbook

requirements.txt contains all python dependencies:

	pip3 install -r requirements.txt

on a linux system, wkhtmltopdf must be installed via apt:
	
	sudo apt install wkhtmltopdf

on macos (requires homebrew):

	brew install homebrew/cask/wkhtmltopdf


once all dependencies are installed, simply run

	python3 dl.py

from the directory you want to save the pdfs in.

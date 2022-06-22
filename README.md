# Handball Youtube Data Video Pipeline

These are python scripts to extract JSON data from the [Youtube Data API](https://developers.google.com/youtube/v3/docs/search/list). More specifically, using these scripts to extract from data from handball videos that can be fed into a database for a web-application to read from. 


## Instructions for using the script
1. Installing a  [Python virtual environment](https://docs.python.org/3/tutorial/venv.html) within the directory is highly recommended to use this script in isolation from other dependencies from different projects. 
2. Installing the dependencies. Run this in the command line within the directory `pip freeze > requirements.txt` to get your dependencies. Then `pip install -r requirements.txt` for installation. 
3. Get your [Youtube API key](https://developers.google.com/youtube/registering_an_application) and create a `.env` file within the directory that references your API key. Check out this [video](https://www.youtube.com/watch?v=YdgIWTYQ69A) to learn how to do this. 
4. Activate the Python virtualenv `(your-virtual-env)\Scripts\activate`
5. Running the script. `python main.py` or `python3 main.py`

![alt text](Project%20Diagram.drawio.png)

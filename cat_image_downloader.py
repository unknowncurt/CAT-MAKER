import requests   # tool that requests library to make http requests
import time # just the time dude. jk. time module to generate unique filenames using timestamps


def fetch_cat_image():

    url = "https://cataas.com/cat"  # the API

    response = requests.get(url)   #http GET request 

    # i think i learned this from a bald guy on youtube

    if response.status_code == 200 :
        filename = f"cat_{int(time.time())}.jpg"


        with open(filename,'wb') as f:

            f.write(response.content)


            print ( f"cat image saved as {filename}")
    else :

        print("failed.")


if __name__ == "__main__":
    fetch_cat_image()
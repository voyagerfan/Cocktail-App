from flask import Flask, render_template, json, redirect
from flask import request
import requests
import json
import os

app = Flask(__name__)


@app.route('/')
def test():
    return redirect("/homepage")

@app.route('/homepage')
def homepage():
    return render_template('home.html')

@app.route('/searchName', methods = ['POST', 'GET'])
def searchName():

    #clear the txt file from previous search
    f = open('sessiondata.txt', 'r+')
    f.truncate(0)
    f.close()

    
    #grab the drink name
    drinkName = request.form['drinkName']
    
    #add drink name to the drink name to the string query. Returns Json data
    drink = requests.get('https://thecocktaildb.com/api/json/v1/1/search.php?s='+drinkName)
    
    #json data for the drink searched 
    jsonData = drink.content

    #parse the json data
    parseData = json.loads(jsonData)
    
    if(parseData['drinks'] == None):
        drinkData =  drinkName +" could not be found, please try again"
    
    #add drink name from nested json data
    else:
        drinkData = parseData['drinks'][0]['strDrink']
        f = open('sessiondata.txt', 'r+')
        f.write(drinkData)
        f.close()
    
    return render_template('home.html', drinkData=drinkData)


@app.route('/displayData', methods = ['POST', 'GET'])
def displayData():


    
    #read the form, give default value of None if empty
    default_value = None
    instruction = request.form.get('instruction', default_value)
    picture = request.form.get('picture', default_value)
    recipe = request.form.get('recipe', default_value)

    #initialize variables passed to HMTL as None
    instructionData = None
    drinkPicture = None
    recipe1arr = None
    recipe2arr = None
    
    #get the drink name
    f = open('sessiondata.txt', 'r+')
    drinkName = f.read()
    f.close()
    drinkData=drinkName
    

    
    if instruction is not None:
        
        #retreive drink name from the session data
        f = open('sessiondata.txt', 'r+')
        drinkName = f.read()
        f.close()
       
        #add drink name to the drink name to the string query. Returns Json data
        drink = requests.get('https://thecocktaildb.com/api/json/v1/1/search.php?s=' + drinkName)
        
        #json data for the drink searched 
        jsonData = drink.content
        
        #parse the json data
        parseData = json.loads(jsonData)
        instructionData = parseData['drinks'][0]['strInstructions']
    
    
    if picture is not None:
        
        #retreive drink name from the session data
        f = open('sessiondata.txt', 'r+')
        drinkName = f.read()
        f.close()
       
        #add drink name to the drink name to the string query. Returns Json data
        drink = requests.get('https://thecocktaildb.com/api/json/v1/1/search.php?s=' + drinkName)
        
        #json data for the drink searched 
        jsonData = drink.content
        
        #parse the json data
        parseData = json.loads(jsonData)
        drinkPicture = parseData['drinks'][0]['strDrinkThumb']

    if recipe is not None:
        
        #retreive drink name from the session data
        f = open('sessiondata.txt', 'r+')
        drinkName = f.read()
        f.close()
       
        #add drink name to the drink name to the string query. Returns Json data
        drink = requests.get('https://thecocktaildb.com/api/json/v1/1/search.php?s=' + drinkName)
        
        #json data for the drink searched 
        jsonData = drink.content

        #parse the json data
        parseData = json.loads(jsonData)
        drinkIngredients = parseData['drinks'][0]
        
        #create arrays to store data
        recipe1arr = []
        recipe2arr = []

        #loop through to get ingredients
        count1 = 1
        count2 = 1
        
        for element in drinkIngredients:
            key1 = 'strIngredient' + str(count1)
            key2 = 'strMeasure' + str(count1)
            value1 = drinkIngredients[key1]
            value2 = drinkIngredients[key2]
            if value1 is None or value2 is None:
                continue
            else:
                recipe1arr.append(value1)
                recipe2arr.append(value2)
                count1 += 1
                count2 += 1
        #reset the counter and string       
        count1 = 1
        count2 = 1
       
        #retreive drink name from the session data
        f = open('sessiondata.txt', 'r+')
        drinkName = f.read()
        f.close()
        drinkData=drinkName

    
    return render_template('home.html', instructionData=instructionData, drinkPicture=drinkPicture, recipe1arr=recipe1arr, recipe2arr=recipe2arr, drinkData=drinkData)

@app.route('/browse', methods = ['POST', 'GET'])
def browse():
    
    return render_template("browse.html")
    
@app.route('/displayIndex', methods = ['POST', 'GET'])
def displayIndex():
    
    #wipe the txt file clean first
    f = open('sessiondata.txt', 'r+')
    f.truncate(0)
    f.close()

    option = request.form['option']

    index = requests.get("https://thecocktaildb.com/api/json/v1/1/search.php?f="+option)


    #json data for the letter searched 
    jsonData = index.content

    #parse the json data
    parseData = json.loads(jsonData)
    indexData = parseData['drinks']

    return render_template("browse.html", indexData=indexData)

@app.route("/searchBrowse", methods = ['POST', 'GET'])
def searchBrowse():
    
    indexBrowse = request.form.get('indexBrowse')
    print("this is the value of indexBrowse: " + str(indexBrowse))
    drinkData = indexBrowse

    f = open('sessiondata.txt', 'r+')
    f.write(drinkData)
    f.close()
    
    

    return render_template("home.html", drinkData=drinkData)

@app.route("/random", methods = ['POST', 'GET'])
def random():

    #wipe the text file clearn first
    f = open('sessiondata.txt', 'r+')
    f.truncate(0)
    f.close()

    # drink = requests.get("https://yd3bs62ieg.execute-api.us-east-2.amazonaws.com/default/randCocktail") //used with microservice
    drink = requests.get("https://www.thecocktaildb.com/api/json/v1/1/random.php")


    # json data for the drink searched 
    jsonData = drink.content

    # parse the json data
    parseData = json.loads(jsonData)

    # drinkData = parseData['Drink Details']['Cocktail Name'] // used with microservice
    drinkData = parseData['drinks'][0]['strDrink']
    f = open('sessiondata.txt', 'r+')
    f.write(drinkData)
    f.close()



    return render_template("home.html", drinkData=drinkData)

# Listener
if __name__ == "__main__":

    # run with docker 
    app.run(port=4000,debug=True, host='0.0.0.0')

    # run locally
    # app.run(port=4000,debug=True, host='127.0.0.1')

"""
#loop through to get ingredients
        count = 1
        x = ""
        recipeList = ""
        for element in drinkIngredients:
            key = 'strIngredient' + str(count)
            value = drinkIngredients[key]
            if value is None:
                continue
            else:
                x = value
                recipeList = recipeList + x
                count += 1
        #reset the counter and string       
        count = 1
        x = None
"""
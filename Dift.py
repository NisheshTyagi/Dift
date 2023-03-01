import json
def readData(file, ctype = True,seperator = ":",ignore=True) -> dict:
    """
    Read the data from a file and convert it into a dictionary

    :param file: The file to read data from
    :type file: TextIOWrapper


    :param ctype: Enable or disable the option to store int as int in dictionary
    :type ctype: bool

    :param seperator: The sign to seperate the key from the value
    :type seperator: string

    :param ignore: Ignore the error due to incorrect seperator or no value
    :type ignore: bool
    """

    #name variable for storing name of the key (temp)
    name = []
    #value variable for storing value (temp)
    value = []
    #dict to return the user
    data = dict()
    #check if current word is a Value
    isValue  = False
    isComment = False
    #if it is a json file then use json library to load it
    if ('.json' or '.Json')in file.name:
        return json.load(file)
    #if not then check every line in the file
    for line in file:
        #if the line is empty then continue to next line
        if bool(line.strip()) == False:
            continue
        #then check every word in the line
        for word in line.strip():
            #if the word is comment then skip this line and
            #set com to true
            if word == "#":
                isComment = True
                break
            #if the word isn't a seperator and is not value
            elif word != seperator and isValue == False:
                #then add the word to the name variable
                name.append(word.strip())
            #if the word is a seperator then set isvalue to true
            elif word == seperator:
                isValue = True
            #if the word is value then append the word
            #to the value variable
            elif isValue:
                value.append(word.strip())
        #after checking every word in that line add the key
        #and the value to the dict variable
        joined_name ="".join(name)
        joined_value = "".join(value)
        #if isComment is true then set it to false and 
        #go to next line
        if isComment:
            isComment = False
        #if it is not a comment and we don't have ctype enabled then
        elif isComment==False and ctype == False:
            #join the key and value and add them to dict variable and reset every variable
            joined_name ="".join(name)
            joined_value = "".join(value)
            data[joined_name.strip()] = joined_value.strip()
            name = []
            value = []
            isValue = False
            #if ignore is not enabled and the value is empty then throw and error
            if ignore == False and joined_value.strip() == '':
                raise Exception("Incorrect data in the file")
        #if is not a comment and ctype is enabled then
        elif isComment == False and ctype:
            #join the key and value
            joined_name ="".join(name)
            joined_value = "".join(value)
            #try if value is an int
            try:
                int(joined_value)
                #if it is then add them to dict variable and reset every variable 
                data[joined_name.strip()] = int(joined_value.strip())
                name = []
                value = []
                isValue = False
                #if ignore is not enabled and the value is empty then throw and error
                if ignore == False and str(joined_value.strip()) == '':
                   raise Exception("Incorrect data in the file")
            #if it is not an int then add them to dict variable and reset every variable  
            except:
                data[joined_name.strip()] = joined_value.strip()
                name = []
                value = []
                isValue = False
                if ignore == False and joined_value.strip() == '':
                   raise Exception("Incorrect data in the file")
    #after every line is checked return the user the dict variable
    return data    

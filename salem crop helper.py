from guizero import App, Box, Text, ButtonGroup, Slider, TextBox
# Included more classes from documentation so I can do more with the library

# I included 3 variables here - variable to show borders for debug purposes (gets applied to all things that are meaningful
# to show borders for debug purposes), mainHeight of the window and mainWidth of the window. I made variable out of that as 
# use those values more than once and I would cry changing them all by hand
showBorders = False
mainHeight = 360
mainWidth = 550

# That function is to act as a callback to all actions we perform in the tool - every change we make it is executed
# so the output and all textboxes are refreshed
def loopUpdate():

    output()
    textbox_update()

# That function refreshes all textboxes with values calculated later
def textbox_update():

    # First, we update the finalPlenty field, passing the value from text field 
    finalPlenty_text.value = str(calculatePlenty(fieldPlenty_box.value))

    # Now we calculate produced plants based on plenty we calculated 
    produce_result = calculateProduce(fieldPlenty_box.value)

    # Here's a tricky part - a little more advanced part of the code. That is called a ternary operator
    # It's basically making an if with the value to variable assigment in one line. I wanted to introduce 
    # something new and fun to the code. It basically does this
    # [value_on_true] if [expression] else [value_on_false] 
    # So, it's basically a code like this

    # if (produce_result != -1)
    #     produce_text.value = produce_result
    # else:
    #     produce_text.value = "No plenty constant \n for that crop"

    # Just made in one line. Take your time wrapping your head around it :P
    produce_text.value = produce_result if produce_result != -1 else "No plenty constant \n for that crop"


# That function is responsible for calculating a plenty value based on the number 
# from text box (passed in `value` parameter) and the seasonal modifier
def calculatePlenty(value):

    # We setup a variable we will use in the function to calculate the result, which we will return later
    result = 0

    # We apply the seasons modifier here, so if the value is '' (nothing entered) we still can account for it. 
    # We don't need to check for Coldsnap, as it will change nothing, so the only meaningful check is to check if it's Everbloom
    if season_but.value == "Everbloom":
        result = result + 50

    # This part makes sure that we're not calculating the plenty if nothing is entered into the field (as it will break stuff)
    # We just post result only including seasons instead
    if value == '':
        return result

    # If we have a value entered, we add it to the result
    # As we take a value from the text box, we need to convert it from text to a number, that's why we do float(value)
    # I convert it also to int, as it doesn't matter in our case as we don't have any decimal places and it makes it cleaner
    result = result + int(float(value))

    # And nowwe can make the function return the result after all calculations if it wasnt returned at value being ''
    return result 

# This function takes the plenty in 'value' parameter and checks how it applies to currently selected crop
# We search for the crop type based on what is selected in seedbox and apply a plentyConstant which is a 
# value from the wiki telling us how much plenty is needed for one crop produced
def calculateProduce(value):

    # Similar thing to result value in calculatePlenty, double conversion to make it clean
    plenty = int(float(value))

    # We introduce the needed constant, here with 0 value as initialization
    plentyConstant = 0
    
    # Now we check for what plant is selected - to handle the plants which we don't know 
    # the plentyConstant I introduced a fallback mechanism of returning -1, so we can later
    # apply special treatment if we received -1
    # If you guess the plenty constant, just replace the return -1 with `plentyConstant = value` you found
    if seedbox.value_text == "Cereal":
        plentyConstant = 50
    elif seedbox.value_text == "Cabbage":
        return -1
    elif seedbox.value_text == "Cotton":
        plentyConstant = 20
    elif seedbox.value_text == "Corn":
        return -1
    elif seedbox.value_text == "Potato":
        plentyConstant = 20
    elif seedbox.value_text == "Pumpkin":
        return -1
    elif seedbox.value_text == "Tobacco":
        plentyConstant = 50
    else:
        return -1
    
    # Here we calculate how much plants we get at the end. It will show only full plants as we converted our floats to ints
    return plenty / plentyConstant 

# This is just value assignment if baobab (yeah, the big tree)
def output():

    # I changed your repeated values in ifs to blocks so you don't need to write the condition for every case
    # This just checks first if the text is Cereal and only then checks if the values are correct for a type
    # Sorry I will not comment all of those cases now :P
    if seedbox.value_text == "Cereal":

        if red.value + pink.value <= 100:
            crop.value = "Oatmeal"
        elif red.value + pink.value >= 100 and red.value >= pink.value and red.value + pink.value <= 150:
            crop.value = "Barley"
        elif red.value + pink.value >= 100 and red.value <= pink.value and red.value + pink.value <= 150:
            crop.value = "Rye"
        elif red.value + pink.value >= 150:
            crop.value = "Wheat"

    elif seedbox.value_text == "Cabbage":

        if blue.value + pink.value <= 100:
            crop.value = "Colewort"
        if blue.value + pink.value >= 100 and blue.value >= pink.value and blue.value + pink.value <= 150:
            crop.value = "Green Cabbage"
        if blue.value + pink.value >= 100 and blue.value <= pink.value and blue.value + pink.value <= 150:
            crop.value = "White Cabbage"
        if blue.value + pink.value >= 150:
            crop.value = "Red Cabbage"

    elif seedbox.value_text == "Cotton":

        if red.value + green.value <= 100:
            crop.value = "Yellow Cotton"
        elif red.value + green.value >= 100 and red.value >= green.value and red.value + green.value <= 150:
            crop.value = "Egyptian Cotton"
        elif red.value + green.value >= 150:
            crop.value = "Sea Island Cotton"
        elif red.value + green.value >= 100 and red.value <= green.value and red.value + green.value <= 150:
            crop.value = "Indian Cotton"

    elif seedbox.value_text == "Corn":

        if red.value + blue.value <= 100:
            crop.value = "Yellow Corn"
        if red.value + blue.value >= 100 and red.value >= blue.value and red.value + blue.value <= 150:
            crop.value = "White Corn"
        if red.value + blue.value >= 100 and red.value <= blue.value and red.value + blue.value <= 150:
            crop.value = "Blue Corn"
        if red.value + blue.value >= 150:
            crop.value = "Golden Corn"

    elif seedbox.value_text == "Potato":

        if blue.value + pink.value <= 100:
            crop.value = "Brown Potato"
        if blue.value + pink.value >= 100 and blue.value >= pink.value and blue.value + pink.value <= 150:
            crop.value = "Blue Potato"
        if blue.value + pink.value >= 100 and blue.value <= pink.value and blue.value + pink.value <= 150:
            crop.value = "Yellow Potato"
        if blue.value + pink.value >= 150:
            crop.value = "Red Potato"

    elif seedbox.value_text == "Pumpkin":

        if green.value + blue.value <= 100 and pumkin_stage.value == "1":
            crop.value = "Baby Bear"
        elif green.value + blue.value <= 100 and pumkin_stage.value == "2":
            crop.value = "Autumn Gold"
        elif green.value + blue.value <= 100 and pumkin_stage.value == "3":
            crop.value = "Aspen"
        elif green.value + blue.value >= 100 and green.value >= blue.value and green.value + blue.value <= 150 and pumkin_stage.value == "1":
            crop.value = "Small Sugar"
        elif green.value + blue.value >= 100 and green.value >= blue.value and green.value + blue.value <= 150 and pumkin_stage.value == "2":
            crop.value = "Bushkin"
        elif green.value + blue.value >= 100 and green.value >= blue.value and green.value + blue.value <= 150 and pumkin_stage.value == "3":
            crop.value = "Big Autumn"
        elif green.value + blue.value >= 100 and green.value <= blue.value and green.value + blue.value <= 150 and pumkin_stage.value == "1":
            crop.value = "Sugar Treat"
        elif green.value + blue.value >= 100 and green.value <= blue.value and green.value + blue.value <= 150 and pumkin_stage.value == "2":
            crop.value = "Harvest Moon"
        elif green.value + blue.value >= 100 and green.value <= blue.value and green.value + blue.value <= 150 and pumkin_stage.value == "3":
            crop.value = "Connecticut Field"
        elif green.value + blue.value >= 150 and pumkin_stage.value == "1":
            crop.value = "Spooktacular"
        elif green.value + blue.value >= 150 and pumkin_stage.value == "2":
            crop.value = "Jack-o-Lantern"
        elif green.value + blue.value >= 150 and pumkin_stage.value == "3":
            crop.value = "Ghost Rider"

    elif seedbox.value_text == "Tobacco":

        if red.value + green.value <= 100:
            crop.value = "Broad Leaf Tobacco"
        if red.value + green.value >= 100 and red.value >= green.value and red.value + green.value <= 150:
            crop.value = "Bright Leaf Tobacco"
        if red.value + green.value >= 100 and red.value <= green.value and red.value + green.value <= 150:
            crop.value = "Shade Leaf"
        if red.value + green.value >= 150:
            crop.value = "Gold Leaf"
        
    # ...only here, as we must take care of the starting case, in which the seed type is Nothing
    else:
        crop.value = "Pick a seed!"
        
# Welcome to Application Hell! I introduced a Box class so I can manually assign parts of the application 

# Here I initialize the main app object so I can act on it later and the library also requires of me to do so :P
# I use previously set variables so if I need to change the size of the window, I can just do it there
ketchup = App(title="Farm Helper", width = mainWidth, height = mainHeight)

# ...and so it will also account for those values being used here. I also made it so showBorders is used here, so if 
# we decide we need to see borders again, we just need to switch it on the start of the file
# I made all the boxes align to the left so they follow a basic rule of aligning in a window, HTML vietnam sends regards
settings_area  = Box(ketchup, align = "left", height = mainHeight, width = 150, border=showBorders)
influence_area = Box(ketchup, align = "left", height = mainHeight, width = 200, border=showBorders)
result_area    = Box(ketchup, align = "left", height = mainHeight, width = 200, border=showBorders)

# After setting 3 main boxes for settings, influence sliders and results, I set the smaller boxes so they
# fit the parts of the bigger boxes. You see as I switched the master parameter, so now the boxes are in the app/settings_area
# part, so they're placed first in app, then in the settings area. I also made them fill the width so they stretch to
# fill the bigger box and made the last one fill also the gap by setting the height to fill also. I made it align to bottom 
# for a reason I forgot now, probably not very important
seedType_subArea = Box(settings_area, align = "top", border=showBorders, width = "fill")
pumpTier_subArea = Box(settings_area, align = "top", border=showBorders, width = "fill")
seasons_subArea  = Box(settings_area, align = "bottom", border=showBorders, width = "fill", height = "fill")

# Did the same treatment to smaller boxes in influence_area, only here I made a small adjustment to output_subArea so it sticks 
# to the bottom but also has a set height - it makes a nice space between the sliders and the output crop, that previously
# were too close to each other
influence_subArea = Box(influence_area, align = "top", border=showBorders, width = "fill") 
output_subArea    = Box(influence_area, align = "bottom", border=showBorders, width = "fill", height = 75) 

# Here's mostly your old code. I just replaced every `command = value` with loopUpdate command so we have everything streamlined
# Changed also some namings and aligns so it fits better into boxes I made. I you want old monkey names back, just let me know
# They were awesome. Oh, I also changed the master parameter (app) to appropriate boxes in which they are now
seed_lable = Text(seedType_subArea, text="Seeds", align = "top")
seedbox = ButtonGroup(seedType_subArea, options=["Nothing","Cereal","Cabbage","Cotton","Corn","Potato","Pumpkin","Tobacco"], command = loopUpdate, align = "top")

# I added a parameter to pumpkin_stage so it is drawn in horizontal button group which looks nicer
pumkin_lable = Text(pumpTier_subArea, text="Pumpkin Stage", align = "top", height="fill")
pumkin_stage = ButtonGroup(pumpTier_subArea,options = ["1","2","3"], command = loopUpdate, align = "top", horizontal=True)

red_lable = Text(influence_subArea, text= "Red", color = "red", align = "top")
red = Slider(influence_subArea, command = loopUpdate)

green_lable = Text(influence_subArea, text= "Green", color = (0,150,0), align = "top")
green = Slider(influence_subArea, command = loopUpdate)

blue_lable = Text(influence_subArea, text="Blue", color = "blue", align = "top")
blue = Slider(influence_subArea, command = loopUpdate)

pink_lable = Text(influence_subArea, text="Pink", color = "purple", align = "top")
pink = Slider(influence_subArea, command = loopUpdate)

crop_lable = Text(output_subArea, text="Output")
crop = Text(output_subArea, text="Pick a seed!")

# Here I also introduced a selected element, which makes the Coldsnap being selected by default - it's better
# than everbloom as it doesnt apply any modifiers we would need to update at the start lol
season_lable = Text(seasons_subArea, text= "Season Planted", color = (0,0,0))
season_but = ButtonGroup(seasons_subArea,options = ["Coldsnap","Everbloom"], selected="Coldsnap", command = loopUpdate)

# Changed some namings here, added 100 base plenty value to the box (as its basic plent for a field) and introduced 
# the planned produce widgets so it shows how many crops you get. I also added command to fieldPlenty_box so 
# whenever someone writes something in the box, everything gets updated
fieldPlenty_label = Text(result_area, text= "Field Plenty", color = (0,0,0))
fieldPlenty_box = TextBox(result_area, text = "100", command = loopUpdate)
finalPlenty_label = Text(result_area, text= "Calculated Plenty", color = (0,0,0))
finalPlenty_text = Text(result_area, text = "0")
produce_label = Text(result_area, text= "Estimated Crops", color = (0,0,0))
produce_text = Text(result_area, text= "0", color = (0,0,0))

# I call loopUpdate here once to apply the 100 shown in fieldPlenty_box to the final plenty and to 
loopUpdate() 

# And now I start the app ;) Yes, I changed the variable name to ketchup.
ketchup.display()
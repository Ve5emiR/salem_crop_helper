from guizero import App, Text, ButtonGroup, Slider

def output():
    if seedbox.value == "nothing":
        crop.value = "pick a seed"
###########cotton#############
    if seedbox.value == "cotton" and red.value + green.value <= 100:
        crop.value = "yellow cotton"
    if seedbox.value == "cotton" and red.value + green.value >= 100 and red.value >= green.value and red.value + green.value <= 150:
        crop.value = "egpytan cotton"
    if seedbox.value == "cotton" and red.value + green.value >= 150:
        crop.value = "sea island cotton"
    if seedbox.value == "cotton" and red.value + green.value >= 100 and red.value <= green.value and red.value + green.value <= 150:
        crop.value = "indian cotton"
##################wheat##############
    if seedbox.value == "cereal" and red.value + pink.value <= 100:
        crop.value = "oatmeal"
    if seedbox.value == "cereal" and red.value + pink.value >= 100 and red.value >= pink.value and red.value + pink.value <= 150:
        crop.value = "barley"
    if seedbox.value == "cereal" and red.value + pink.value >= 100 and red.value <= pink.value and red.value + pink.value <= 150:
        crop.value = "rye"
    if seedbox.value == "cereal" and red.value + pink.value >= 150:
        crop.value = "wheat"
############pumkins################
    if seedbox.value == "pumkin" and green.value + blue.value <= 100 and pumkin_stage.value == "1":
        crop.value = "baby bear"
    if seedbox.value == "pumkin" and green.value + blue.value <= 100 and pumkin_stage.value == "2":
        crop.value = "autumn gold"
    if seedbox.value == "pumkin" and green.value + blue.value <= 100 and pumkin_stage.value == "3":
        crop.value = "aspen"
    if seedbox.value == "pumkin" and green.value + blue.value >= 100 and green.value >= blue.value and green.value + blue.value <= 150 and pumkin_stage.value == "1":
        crop.value = "small sugar"
    if seedbox.value == "pumkin" and green.value + blue.value >= 100 and green.value >= blue.value and green.value + blue.value <= 150 and pumkin_stage.value == "2":
        crop.value = "bushkin"
    if seedbox.value == "pumkin" and green.value + blue.value >= 100 and green.value >= blue.value and green.value + blue.value <= 150 and pumkin_stage.value == "3":
        crop.value = "big autumn"
    if seedbox.value == "pumkin" and green.value + blue.value >= 100 and green.value <= blue.value and green.value + blue.value <= 150 and pumkin_stage.value == "1":
        crop.value = "sugar treat"
    if seedbox.value == "pumkin" and green.value + blue.value >= 100 and green.value <= blue.value and green.value + blue.value <= 150 and pumkin_stage.value == "2":
        crop.value = "harvest moon"
    if seedbox.value == "pumkin" and green.value + blue.value >= 100 and green.value <= blue.value and green.value + blue.value <= 150 and pumkin_stage.value == "3":
        crop.value = "connecticut field"
    if seedbox.value == "pumkin" and green.value + blue.value >= 150 and pumkin_stage.value == "1":
        crop.value = "spooktacular"
    if seedbox.value == "pumkin" and green.value + blue.value >= 150 and pumkin_stage.value == "2":
        crop.value = "jack o lanten"
    if seedbox.value == "pumkin" and green.value + blue.value >= 150 and pumkin_stage.value == "3":
        crop.value = "ghost rider"
############cabbage##################
    if seedbox.value == "cabbage" and blue.value + pink.value <= 100:
        crop.value = "colewort"
    if seedbox.value == "cabbage" and blue.value + pink.value >= 100 and blue.value >= pink.value and blue.value + pink.value <= 150:
        crop.value = "green cabbage"
    if seedbox.value == "cabbage" and blue.value + pink.value >= 100 and blue.value <= pink.value and blue.value + pink.value <= 150:
        crop.value = "white cabbage"
    if seedbox.value == "cabbage" and blue.value + pink.value >= 150:
        crop.value = "red cabbage"
################corn################
    if seedbox.value == "corn" and red.value + blue.value <= 100:
        crop.value = "yellow corn"
    if seedbox.value == "corn" and red.value + blue.value >= 100 and red.value >= blue.value and red.value + blue.value <= 150:
        crop.value = "white corn"
    if seedbox.value == "corn" and red.value + blue.value >= 100 and red.value <= blue.value and red.value + blue.value <= 150:
        crop.value = "blue corn"
    if seedbox.value == "corn" and red.value + blue.value >= 150:
        crop.value = "golden corn"
###########tatters####################
    if seedbox.value == "potato" and blue.value + pink.value <= 100:
        crop.value = "brown potato"
    if seedbox.value == "potato" and blue.value + pink.value >= 100 and blue.value >= pink.value and blue.value + pink.value <= 150:
        crop.value = "blue potato"
    if seedbox.value == "potato" and blue.value + pink.value >= 100 and blue.value <= pink.value and blue.value + pink.value <= 150:
        crop.value = "yellow potato"
    if seedbox.value == "potato" and blue.value + pink.value >= 150:
        crop.value = "red potato"
#############death################
    if seedbox.value == "death(tobaco)" and red.value + green.value <= 100:
        crop.value = "broad leaf"
    if seedbox.value == "death(tobaco)" and red.value + green.value >= 100 and red.value >= green.value and red.value + green.value <= 150:
        crop.value = "bright leaf"
    if seedbox.value == "death(tobaco)" and red.value + green.value >= 100 and red.value <= green.value and red.value + green.value <= 150:
        crop.value = "shade leaf"
    if seedbox.value == "death(tobaco)" and red.value + green.value >= 150:
        crop.value = "gold leaf"

app = App(title="farm helper", width = 470, height = 340)

seed_lable = Text(app, text="seeds", align = "left")
seedbox = ButtonGroup(app, options=["nothing","cotton","cereal","pumkin","cabbage","corn","potato","death(tobaco)"], command = output, align = "left")

pumkin_lable = Text(app, text="pumkin stage", align = "right")
pumkin_stage = ButtonGroup(app,options = ["1","2","3"], command = output, align="right")

red_lable = Text(app, text= "red", color = "red")
red = Slider(app, command = output)

green_lable = Text(app, text= "green", color = (0,150,0))
green = Slider(app, command = output)

blue_lable = Text(app, text="blue", color = "blue")
blue = Slider(app, command = output)

pink_lable = Text(app, text="pink", color = "purple")
pink = Slider(app, command = output)

crop = Text(app, text="pick a seed", align="bottom")
crop_lable = Text(app, text="output", align="bottom")

app.display()
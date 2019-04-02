from selenium import webdriver
import base64

browser = webdriver.Chrome("C:/Users/Christian/Documents/MLML/nlp_animation_generator/SpriteData/chromedriver.exe") #replace with .Firefox(), or with the browser of your choice
url = "http://gaurav.munjal.us/Universal-LPC-Spritesheet-Character-Generator/#?sex=female&legs=sara&mail=chain"
browser.get(url)
canvas = browser.find_element_by_css_selector("#spritesheet")
# get the canvas as a PNG base64 string
canvas_base64 = browser.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)

# decode
canvas_png = base64.b64decode(canvas_base64)

# save to a file
with open(r"canvas.png", 'wb') as f:
    f.write(canvas_png)
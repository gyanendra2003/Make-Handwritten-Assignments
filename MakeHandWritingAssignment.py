'''import pywhatkit as kit
text = "Hello, this is a test."
output_filename = "handwriting_output.png"
try:
    kit.text_to_handwriting(text, output_filename, rgb=[0, 0, 0])
    print(f"Handwriting image saved as {output_filename}")
except kit.core.exceptions.UnableToAccessApi as e:
    print(f"Error: Unable to access the Pywhatkit API right now. Details: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")'''
from PIL import Image, ImageDraw, ImageFont

# Create a blank image with white background
width, height = 1000, 400
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Load a handwriting-style font (you can use any TTF font)
font = ImageFont.truetype("/Users/gyanendrasingh/Downloads/a-little-sunshine/A little sunshine.ttf", size=18)

# Text to be rendered
text = """n a neural network, the activation function is responsible for transforming the summed weighted input from the node into the activation of the node or output for that input.
The rectified linear activation function or ReLU for short is a piecewise linear function that will output the input directly if it is positive, otherwise,
it will output zero. 
It has become the default activation function for many types of neural networks because a model that uses it is easier to train and often achieves better performance."""
# Position to start rendering the text
x, y = 20, 20

# Color for the text (black in RGB)
text_color = (0, 0, 138)

# Render the text on the image
draw.text((x, y), text, fill=text_color, font=font)

# Save the image
image.save("handwriting_output.png")

# Display the image (optional)
image.show()

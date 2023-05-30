from PIL import Image, ImageFilter

# Load the image
image = Image.open('CSK.png')

# Display the original image
image.show()

# Convert the image to grayscale
gray_image = image.convert('L')

# Display the grayscale image
gray_image.show()

# Apply Gaussian blur to the image
blurred_image = image.filter(ImageFilter.GaussianBlur(radius=5))

# Display the blurred image
blurred_image.show()

# Apply edge detection to the image
edges = image.filter(ImageFilter.FIND_EDGES)

# Display the edge-detected image
edges.show()

# Apply image thresholding
thresholded_image = gray_image.point(lambda x: 255 if x > 127 else 0, mode='1')

# Display the thresholded image
thresholded_image.show()

# Rotate the image
rotated_image = image.rotate(45)

# Display the rotated image
rotated_image.show()

# Resize the image
resized_image = image.resize((int(image.width / 2), int(image.height / 2)))

# Display the resized image
resized_image.show()

# Save the processed image
resized_image.save('processed_image.jpg')


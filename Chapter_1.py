import cv2
import pytesseract

# Load the image
img = cv2.imread('Resources/3.jpg')

# Check if the image is loaded successfully
if img is None:
    print("Error: Unable to load image.")
else:
    # Resize the image to improve processing
    img = cv2.resize(img, None, fx=2, fy=2)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Noise reduction (Gaussian blur)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Text region localization (contour detection)
    contours, _ = cv2.findContours(blurred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        roi = blurred[y:y + h, x:x + w]

        # Use pytesseract for text extraction
        extracted_text = pytesseract.image_to_string(roi, lang='eng', config='--psm 6')

        # Print the extracted text
        if extracted_text.strip():
            print("Extracted Text:")
            print(extracted_text)




# import cv2
# import pytesseract
# import numpy as np
#
# # Load the image
# img = cv2.imread('Resources/3.jpg')
#
# # Check if the image is loaded successfully
# if img is None:
#     print("Error: Unable to load image.")
# else:
#     # Resize the image to improve processing
#     img = cv2.resize(img, None, fx=2, fy=2)
#
#     # Convert the image to grayscale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # Noise reduction (Gaussian blur)
#     blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#
#     # Text region localization (contour detection)
#     contours, _ = cv2.findContours(blurred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     for contour in contours:
#         x, y, w, h = cv2.boundingRect(contour)
#         roi = blurred[y:y + h, x:x + w]
#         # Deskew the ROI
#         M = cv2.getRotationMatrix2D((w // 2, h // 2), 0, 1)
#         roi = cv2.warpAffine(roi, M, (w, h))
#         # Use pytesseract for text extraction
#         extracted_text = pytesseract.image_to_string(roi, lang='eng', config='--psm 6')
#         # Print the extracted text
#         if extracted_text.strip():
#             print("Extracted Text:")
#             print(extracted_text)

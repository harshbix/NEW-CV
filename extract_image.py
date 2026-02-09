from pypdf import PdfReader

def extract_images_from_pdf(path):
    reader = PdfReader(path)
    count = 0
    for page in reader.pages:
        for image_file_object in page.images:
            with open(f"profile_extracted_{count}.jpg", "wb") as fp:
                fp.write(image_file_object.data)
                print(f"Extracted image: profile_extracted_{count}.jpg")
            count += 1
    if count == 0:
        print("No images found in PDF.")

try:
    print("Attempting to extract from DOC-20231014-WA0005. (1).pdf")
    extract_images_from_pdf("DOC-20231014-WA0005. (1).pdf")
except Exception as e:
    print(f"Error: {e}")

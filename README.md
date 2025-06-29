# TEAM PSST  
[Try it here → proofa.streamlit.app](https://proofa.streamlit.app)

Check Out the Demo Video !!! - [https://drive.google.com/file/d/1uuigtH5YuXcgcPAFz71BCAsgNyj7VeaE/view?usp=sharing](https://drive.google.com/file/d/1uuigtH5YuXcgcPAFz71BCAsgNyj7VeaE/view?usp=sharing)

## Objective  
To develop a lightweight system that verifies a user's age and identity using a government-issued ID (e.g., Aadhaar) and a live selfie image.

---

## Tools & Technologies Used  
- Python  
- OpenCV  
- Tesseract OCR  
- Insightface (for face verification)  
- Streamlit (for frontend demo)

---

## Key Features  

- OCR-Based DOB Extraction  
  Used Tesseract OCR to extract Date of Birth from the uploaded Aadhaar card image.

- Age Calculation  
  Computed age from the extracted DOB and checked if the user is 18+.

- Face Verification  
  Compared the Aadhaar image with a live selfie using Insightface to verify identity.


---

## Outcome  

Successfully built a working prototype that can:

- Extract DOB and compute age from Aadhaar image  
- Check if the user is an adult (18+)  
- Match the Aadhaar photo with a selfie for identity verification  
- Run locally or via Docker using a single `docker-compose` command

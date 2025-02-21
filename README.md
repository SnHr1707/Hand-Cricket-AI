Hand Cricket game made using AI  

# Run this command to install the libraries and set up environment
python -m venv venv  

If you are using git bash:  
source venv/Scripts/activate  

If you are using powershell:  
venv\Scripts\Activate 

If you are using command prompt:  
venv\Scripts\activate 

If you are on Linux/MacOS:  
source venv/bin/activate

Then:
pip install -r requirements.txt
pip install opencv-python mediapipe==0.10.13
python main.py
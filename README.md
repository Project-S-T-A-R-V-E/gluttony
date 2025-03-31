# Installation Steps (Linux Machines Only)  
1. **Create and Activate Virtual Environment**  
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

2. **Install Required Python Packages**  
    ```bash
    pip install -r requirements.txt
    ```

3. **Install npm and Socket.IO**  
    ```bash
    sudo apt install npm
    npm install socket.io
    ```

4. **Google Maps API Key**  
    For the Google Maps API key, please contact [etjoy1@morgan.edu](mailto:etjoy1@morgan.edu).

5. **Start ngrok on Port 5000**  
    ```bash
    ngrok http 5000
    ```

6. ## Run the Python Script
    ```bash
    sudo python3 main.py
    ```
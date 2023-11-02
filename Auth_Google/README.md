# Google Login App

The repository Google Login App is a sample web application that allows users to log in using their Google account. This README will guide you through the installation and usage of the app.

## Installation

1. Clone this repository to your computer:
    ```
    https://github.com/carminecoppola/Auth_Google.git
    ```
   
2. Make sure you have **_Python_** installed on your system.

3. Create a virtual environment (optional but recommended):
    ```
    python -m venv venv
    source venv/bin/activate # Su Windows: venv\Scripts\activate
    ```
    
4. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
   
5. Configure Google OAuth2 credentials:
    - Go to [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project or use an existing one.
    - Enable the Google+ API for your project.
    - Create OAuth2 credentials. When creating the credentials, specify the redirect URI as `http://localhost:5000/callback` or the appropriate URL based on your configuration.
    - Download the JSON credentials and save the file as `client_secret.json` in the app's directory.

## Usage

1.  Run the app:
    ```
    python app.py
    ```

2. Open your browser and go to `http://localhost:5000` to access the app.

3. Click on "Login" to start the authentication process with Google. You will be redirected to the Google login page.

4. Log in with your Google account or select the account you want to use for login.

5. After authentication, you will be redirected to the main page with your name displayed.

6. You can click on "Protected Area" to access the protected area or "Logout" to log out.

## Customization

You can customize the app by modifying the source code. For example, you can add new features, change the appearance, or implement additional pages.


## License

This project is distributed under the MIT license. For more details, please refer to the LICENSE file.

### Tutorial
   ```
    https://www.youtube.com/watch?v=FKgJEfrhU1E
   ```
# Questacon App

This repository contains a Streamlit-based application designed for controlling Pepper, a humanoid robot, using predefined animations and behaviors. The app connects to Pepper and provides an interactive interface to play, stop, and manage animations.

## Features

- **Behavior Control:** Start and stop a variety of animations on Pepper.
- **Interactive UI:** Easy-to-use buttons for triggering different animation categories.
  - **Eyes** Changin colours of eyes
  - **Dialog Animations:** Space & Time, Self & Others, Affirmation, etc.
  - **Moods:** Positive, Neutral, and Negative emotional states.
  - **Pepper Speaking** Speaking behaviour
  - **Script** Questacon script

## Requirements

- [Python 3.8+](https://www.python.org/downloads/)
- [Streamlit](https://streamlit.io/)
- [Qi Framework](https://pypi.org/project/qi/)
- [Choregraphe](https://www.aldebaran.com/en/support/pepper-naoqi-2-9/downloads-softwares)

## Installation

### Steps to Install the Questacon Robot Application

1. **Open Choregraphe:**

   - Launch **Choregraphe** on your computer.
   - Connect to Pepper by entering the robot’s IP address.

2. **Load the Questacon Project:**

   - Click **File > Open project** and navigate to the `questacon` folder.
   - Open the Questacon project file (`questacon.pml`).

3. **Access the Robot Applications Panel:**

   - In Choregraphe, navigate to the **Robot Applications** panel (located on the left side of the screen).
   
4. **Install the Questacon Application:**

   - In the **Robot Applications** panel, click the **Package and install** button.

5. **Verify Installation:**

   - After installation, you should see the Questacon application listed in the **Robot Applications** panel.

Once the Questacon robot application is installed on Pepper, you will be able to use the Streamlit app to control and trigger the installed behaviors and animations on the robot.

### App installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/BuddhiGamage/questacon.git
   cd questacon

2. **Create virtual environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt

4. **Run the app:**
    
    ```bash
    streamlit run app.py

## Usage

1. **Connection Setup:**

    - The app uses the Connection class to establish a connection with the Pepper robot.
    
    - Update the IP and port if necessary:


    ```python
    ip = 'localhost'  # or the robot's IP
    port = 42535      # or the appropriate port

2. **Interactive Actions:**

    - Use the provided buttons to start animations.
Stop all animations using the "Stop Animation" button.

3. **UI Structure:**

    - Dialog Animations: Includes buttons for various communication styles.
    - Moods: Trigger animations for different emotional states.
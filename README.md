# Digital Habit Tracker with Pixela

## Overview

This Digital Habit Tracker is a Python application that uses the Pixela API to help you track and visualize your daily habits. Whether it's about coding, reading, exercising, or any other activity, this tracker is designed to log your progress and help you maintain consistency in your habits.

## Output
![image](https://github.com/sarvesh-2109/Digital-Habit-Tracker/assets/113255836/78e6d172-5641-45a2-a603-1dbf7c5d1c71)


## Features

- Create a user account on Pixela.
- Create a graph for habit tracking.
- Add pixels to the graph to represent daily habit data.
- Update existing data points.
- Delete data points if necessary.

## How it Works

The application uses the Pixela API for all operations. Pixela is a "habit tracker as a pixel art" service that turns your habit data into colorful graphs.

## Requirements

- Python 3
- Requests library

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/digital-habit-tracker.git
   ```
2. Install the required packages:
   ```bash
   pip install requests
   ```

## Configuration

1. Replace `USERNAME` and `TOKEN` with your Pixela username and token.
2. `GRAPH_ID` is the identifier for your habit graph.
3. Customize the `graph_config` dictionary to configure your graph's appearance and type.

## Usage

- Run the script and follow the prompts to log your daily habits.
- The script allows you to add, update, and delete data in your Pixela graph.
- Track your progress on the Pixela dashboard.

## Example

This application is already set up to track coding hours. You can modify it to track any habit by changing the `graph_config` and `post_pixel_config`.

## Disclaimer

Ensure to keep your Pixela token secure and avoid sharing it publicly.

## Contribution

Feel free to fork the project, make improvements, or suggest changes. Contributions are always welcome!


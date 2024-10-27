# YouTube Product Review Summarizer
### Author: Virendrasinh Chavda

<p align="justify">
This repository contains the code for an application that extracts and summarizes product reviews from YouTube videos using **Streamlit**, **AssemblyAI**, and the **YouTube Data API**. This tool saves users time by automatically generating a list of Pros and Cons for any product based on selected YouTube review videos. The app combines natural language processing and user-friendly design to make informed purchasing decisions easy and efficient.
</p>

## Table of Contents
1. [Overview](#Overview)
2. [Features](#Features)
3. [Technologies Used](#Technologies-Used)
4. [Setup and Installation](#Setup-and-Installation)
5. [Usage](#Usage)
6. [Future Enhancements](#Future-Enhancements)
7. [Contributing](#Contributing)
8. [License](#License)

## Overview
<p align="justify">
Finding reliable product information can be overwhelming with the vast number of YouTube reviews available. This app allows users to search for a product, select relevant YouTube review videos, and receive a concise summary of the product’s Pros and Cons based on these reviews. By leveraging **YouTube Data API** for video selection and **AssemblyAI** for transcription, the app provides valuable insights with minimal effort from the user.
</p>

![HomePage](/snap1.png)
![Video Selection](/snap2.png)
![Results](/snap3.png)

## Features
* **Keyword-Based Video Search**: Search for videos related to a specific product directly within the app.
* **Video Selection**: Choose from a list of the most relevant videos retrieved from YouTube.
* **Automatic Transcription**: Converts audio content to text, extracting key insights from the videos.
* **Summarized Pros and Cons**: Provides an easy-to-read summary with the product’s Pros and Cons for a quick overview.

## Technologies Used
* **Streamlit**: For building the interactive web application.
* **AssemblyAI**: For transcribing audio from YouTube videos.
* **YouTube Data API**: To search and retrieve YouTube video metadata.
* **Python**: For the core backend logic and processing.
* **yt-dlp**: For downloading audio from YouTube videos.

## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/VirendraChavda/Quick-Product-Reviews-from-YouTube.git
   cd your-repo-name
   ```
2. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set Up API Keys**
   ```bash
   YOUTUBE_API_KEY=your_youtube_api_key
   ASSEMBLYAI_API_KEY=your_assemblyai_api_key
   ```
4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## Usage
<p align="justify">
After launching the app, enter the product name and search for YouTube reviews. Select the videos you find relevant, and the app will automatically summarize the product’s Pros and Cons based on these videos. This summary provides a concise overview, helping you make quicker, more informed purchasing decisions.
</p>

## Future Enhancements
* **Multilingual Support**: Enable the app to process reviews in multiple languages.
* **Enhanced Summarization**: Utilize more advanced NLP techniques to improve summary accuracy.
* **Real-Time Updates**: Add functionality to refresh video results in real-time as new reviews are posted.

## Contributing
<p align="justify">
Contributions are welcome! Feel free to open a pull request or issue to suggest improvements or report bugs. For major changes, please discuss them in an issue first to ensure alignment with the project’s direction.
</p>

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
   

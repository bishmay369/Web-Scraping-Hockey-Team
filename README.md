🏒 Web Scraping Project: Hockey Team Data
   
   A web scraping project that extracts hockey team data such as 
   team names, years, wins, and losses using **Scrapy** and **XPath**.
   This project is designed to demonstrate how to use Scrapy for data
   extraction from websites in a structured format.
   
📋 Project Overview

   This project uses **Scrapy**, a powerful Python framework, 
   to scrape hockey team information from a specified website. 
   The project focuses on learning to navigate HTML structures 
   with **XPath** to extract specific information efficiently.

🛠️ Installation and Setup

   Step1 : First, clone this repository to your local machine:
           git clone https://github.com/bishmay369/Web-Scraping-Hockey-Team.git
                     cd Web Scraping Hockey Team

   step2 : Set Up a Virtual Environment (Optional but Recommended)
           On macOS/Linux:
                         python3 -m venv venv
                         source venv/bin/activate
           On Windows:
                      python -m venv venv
                      venv\Scripts\activate

   step3 : Install Dependencies
          pip install -r requirements.txt
                   
   step4 : Verify the Setup
         pip list
         scrapy --version

   step5 : Running the Spider
        scrapy crawl hockey_team

        This will execute the hockey_team spider, which scrapes the specified website
        and collects the desired data.

📄 Output
    The spider yields structured data in the following format:

    Team Name: The name of the hockey team.
    Team Year: The year associated with the team's record.
    Team Wins: Number of wins.
    Team Losses: Number of losses.

⚙️ Configurations
    
  If you want to customize the spider's behavior, you can modify the following settings in settings.py:

       DOWNLOAD_DELAY: Add a delay between requests to avoid overloading the server.
       USER_AGENT: Set a custom user agent for requests.
       FEEDS: Configure the output format (e.g., JSON or CSV).

 🤝 Contributing
   
    Contributions are welcome! If you have any ideas or improvements, 
    please feel free to submit a pull request.

  📧 Contact
     If you have any questions or suggestions, feel free to reach out:

     GitHub: @bishmay369
     Email: bishmay.padhi@gmail.com

                      Thank you for checking out this project! 😊
  

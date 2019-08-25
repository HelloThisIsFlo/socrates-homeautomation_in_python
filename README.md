# Home-Automation in Python - Socrates 2019

### Get started with HomeAssistant and Appdaemon

This repo is a support for a session I hosted in [#Socrates2019](https://twitter.com/hashtag/socrates2019): _"Home-Automation in Python"_

## What does it do?
The final commit contains multiple services running in Docker:
- a fully working Home-Assistant instance configured to work with MQTT
- A MQTT Broker with preconfigured username/password: `mqttuser` / `mqttpass`
- An Appdaemon configuration with 2 automations:
  - `LogText`: Simply listen to text change in an text input and log it to the appdaemon log
  - `MorseCode`: Listen for text change, and use the connected switch to display the word in Morse code

## Support Material
- **Presentation**
  - [MindMap & Presentation - iThoughtsX](/support/presentation/HomeAutomationSocrates.itmz)  
    => [Flipcharts](/support/presentation/HomeAutomation_in_Python.pdf)
  - [MindMap only - PNG](/support/presentation/MindmapAsPNG.png)
  - [Presentation only - PDF](/support/presentation/PresentationAsPDF.pdf)
- **Blog Post:** _SOON @ https://professionalbeginner.com_



## How to use it?
As mentionned this was intended as a support for a presentation I hosted. In a couple of weeks, I will publish a blog post explaining all the steps to get there that will be the equivalent of the presentation and make everything clear and easily understandable.

That being said, the repo itself is conceived in a way to make it somewhat easily understandable even without any presentation support (although it's an order of magnitude more complicated):
- **Each commit represents a significant change**
- To explore the repo:
  - **Read the commit message**
  - **See the diff to understand how that particular step was implemented**  
    _ex: `git show step-1a`_

![Steps of the tutorial](/support/presentation/hero.png)

# **10SE - Miles Cutting - 2025 - Assessment Task 1 - Data Science**

## Notes for Later Miles:
https://jokes.one/api/joke/#jodc-python


## Requirements:
***
### Functional Requirements:
* Data Retrieval: The user needs to be able to easily and effecitvely read a joke, then decide, through the use of interactive buttons, if the joke is good, and worth putting in their collection, or bad, and discarding it. After the desicion, the user is presented with a new joke. At any time, the user can look at all their jokes in their collection, which is is a table, storing their jokes, and punchlines.

* User Interface: Their needs be be several key elements for the user to interact with. The first is a 'tab' system, that has a main page, a collections page, and a help page. The main page will have text on the screen that says the joke, and underneath, it will contain a thumbs up and thumbs down button, the thumbs up button will save the joke in the users collection folder. The thumbs down button will discard the joke, then the joke disapears and a new one is added. The collections page will display a table for the user to scroll through that contains the joke and the punchline. It will have two actions that the user can interact with, A 'random button', which presents a random joke from their collection, and a 'Add Joke Button', which manually lets a user enter a joke into their collection. The help tab will be the README file printed, which will contain the instructions of the program, the user does not need to interact with anything on this tab.

* Data Display: The user needs to obtain key information from the system. On the Main tab, a visual pop-up with the joke needs to show up, the second is visual feedback on their actions with the joke, i.e If they added it to their collection, they get visual feedback to see it go into their collections, or if they discard it, they recieve visual feedback to see that it has not entered their collection. On the collections tab, the user needs clearly to see the joke they recieve when they click the random joke button. The second is visual feedback that the joke they have entered into the system, has gone into their collections folder.

### Non-Functional Requirements:
* Performance: The system needs to give the user real time feedback of what is happening. This will involve ensuring the animations and actions happen as soon as possible. This requirement will be achievable, because of the minimum processing happening on the device itself.

* Reliability: There are two parts of the software that will cause the software to become unreliable or not funciton as intended. The first of these is the user. The system will have very few points where the user can incorrectly enter information or make a mistake, this means that the software will have very few points of failure from user error. The second part that can have issues with reliability is the api. Changes with how the api functions can impact how the software will run. To ensure these possible issues are communicated to the user, an effective error message handling system is required in the final product. Another layer of protection to support the user in possible issues, is storing the collections on the individual device, which will mean that even with issues with the api, a collection of jokes will still be accessable.

* Usability and Accessibility: The system needs to be intuative enough for someone with little to no computer literacy to effecively use the software, with the only information given to them is the functionality of the software. i.e It curates and stores jokes. To accmplish this, I want to use a range of icons, and labeled buttons, such as thumbs up and thumbs down, and tabs with names, such as Main, Collection, and Help.

### Specifications:
***
### Functional Specifications:
#### User Requirements:
* Select whether a joke is good, and worth keeping in their collection, or not, and be discarded.
* View their collection of jokes in a easy to read table that seperates the main line and the punch line.
* Manually add a Joke to their collection.
* Find a random joke from their collection.

#### Inputs and Outputs:
* **Input** - The Joke from the API - **Output** - The joke in text on the main screen of the program
* **Input** - The Users Feedback on the joke, i.e Keep or Discard - **Output** - A visual representation of the joke being discarded or kept, then being replaced with a new joke
* **Input** - The user manually enters a joke into the Collection - **Output** - The collection actively updating with their joke included in it
* **Input** - The user selects the random option under the collections tab - **Output** - The user recievevs a random joke from their collection pop up on their screen.

#### Core Features and Mechanics:
* Jokes are provided to the User to store
* Jokes are 

### Non-Functional Specifications:
* First Non-Functional Specifications
* Second Non-Functional Specifications


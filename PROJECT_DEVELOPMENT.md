# <ins> **10SE - Miles Cutting - 2025 - Assessment Task 1 - Data Science** <ins>

## Notes for Later Miles:
https://jokes.one/api/joke/#jodc-python
https://github.com/public-apis/public-apis

## <ins> Requirements: <ins>
***
### Functional Requirements:
* Data Retrieval: The user needs to be able to easily and effectively read a joke, then decide, through the use of interactive buttons, if the joke is good, and worth putting in their collection, or bad, and discarding it. After the decision, the user is presented with a new joke. At any time, the user can look at all their jokes in their collection, which is is a table, storing their jokes, and punchlines.

* User Interface: Their needs be be several key elements for the user to interact with. The first is a 'tab' system, that has a main page, a collections page, and a help page. The main page will have text on the screen that says the joke, and underneath, it will contain a thumbs up and thumbs down button, the thumbs up button will save the joke in the users collection folder. The thumbs down button will discard the joke, then the joke disappears and a new one is added. The collections page will display a table for the user to scroll through that contains the joke and the punchline. It will have two actions that the user can interact with, A 'random button', which presents a random joke from their collection, and a 'Add Joke Button', which manually lets a user enter a joke into their collection. The help tab will be the README file printed, which will contain the instructions of the program, the user does not need to interact with anything on this tab.

* Data Display: The user needs to obtain key information from the system. On the Main tab, a visual pop-up with the joke needs to show up, the second is visual feedback on their actions with the joke, i.e If they added it to their collection, they get visual feedback to see it go into their collections, or if they discard it, they receive visual feedback to see that it has not entered their collection. On the collections tab, the user needs clearly to see the joke they receive when they click the random joke button. The second is visual feedback that the joke they have entered into the system, has gone into their collections folder.

### Non-Functional Requirements:
* Performance: The system needs to give the user real time feedback of what is happening. This will involve ensuring the animations and actions happen as soon as possible. This requirement will be achievable, because of the minimum processing happening on the device itself.

* Reliability: There are two parts of the software that will cause the software to become unreliable or not function as intended. The first of these is the user. The system will have very few points where the user can incorrectly enter information or make a mistake, this means that the software will have very few points of failure from user error. The second part that can have issues with reliability is the api. Changes with how the api functions can impact how the software will run. To ensure these possible issues are communicated to the user, an effective error message handling system is required in the final product. Another layer of protection to support the user in possible issues, is storing the collections on the individual device, which will mean that even with issues with the api, a collection of jokes will still be accessible.

* Usability and Accessibility: The system needs to be intuative enough for someone with little to no computer literacy to effectively use the software, with the only information given to them is the functionality of the software. i.e It curates and stores jokes. To accomplish this, I want to use a range of icons, and labeled buttons, such as thumbs up and thumbs down, and tabs with names, such as Main, Collection, and Help.

## <ins> Specifications: <ins>
***
### Functional Specifications:
#### User Requirements:
* Select whether a joke is good, and worth keeping in their collection, or not, and be discarded.
* View their collection of jokes in a easy to read table that separates the main line and the punch line.
* Manually add a Joke to their collection.
* Find a random joke from their collection.

#### Inputs and Outputs:
* **Input** - The Joke from the API - **Output** - The joke in text on the main screen of the program
* **Input** - The Users Feedback on the joke, i.e Keep or Discard - **Output** - A visual representation of the joke being discarded or kept, then being replaced with a new joke
* **Input** - The user manually enters a joke into the Collection - **Output** - The collection actively updating with their joke included in it
* **Input** - The user selects the random option under the collections tab - **Output** - The user receives a random joke from their collection pop up on their screen.

#### Core Features and Mechanics:
* Jokes are provided to the User to store
* Jokes are kept in a collection
* Jokes can manually be added to the users collection
* Random jokes can be got from the users collection

#### User Interaction:
* The User will interact with the program via a GUI made with tKinter
* To make the UI as useable as possible, their will be a large array of icons to effectively convey the utility of the button or Labeled buttons, what make it clear and evident the functionality it provides to the user

#### Error Handling:
* Their are very few points of error that could cause problems in the program. The two main points of error are the API, and the user interface. To handle problems with the API, the best solution for handling this  is the use of error messages that advise the user on how to handle the issues. These handling solutions could be to try reloading the API call, with how to do that on the Error message, or to avoid functionality the API relies on, i.e Only using the collections functionality. The main issue with the UI, is the user clicking the wrong button. To avoid this, keeping a short backlog of key information can help with ensuring the user has time to realize their mistake, and correct the dat from the backlog. To do this, keeping a backlog of the previous 3 jokes, and making them reachable to change, i.e add or remove from their collections.

### Non-Functional Specifications:
#### User Interaction:
* To keep the user satisfaction at it's highest, it is important that the program is keeping up with the user. The main bottleneck which will slow the user's experience is the API calls. If the User is making requests as they need a joke, they will be slowed by both their internet connection, and the speed of the API centre. To counter this, I can have a line up of 3 jokes before their current one, so while they are looking at a new joke, the API is calling for a new one. This means that the user is never waiting for the API to process, and will result in higher user enjoyment and satisfaction with the end product.

#### Useability / Accessibility:
* To keep the software as accessible as possible, ensuring it uses generic system level interactions, i.e Mouse and Keyboard, will mean that the software will automatically be useable with any specialty user controllers that assist in movement and useability. i.e Many people with limited movement skills uses custom controllers to navigate their computer, that have custom text inputs, and pointer inputs.

#### Reliability:
* 

## <ins> Use Cases: <ins>
***
Actor: User (A Funny Person)

Preconditions: Internet access; API with jokes is available.

Main Flow:

Search Rock/Mineral – User enters a rock/mineral name (e.g., Obsidian, Quartz); system retrieves and displays details.

Store Rock – User adds the rock to their collection; system confirms storage.

Compare Rocks – User selects rocks; system retrieves and displays comparisons (e.g., hardness, composition, rarity).

Visualise Data – System generates a graph comparing selected rocks.

Remove Rock – User deletes a rock from the collection; system updates storage.

Postconditions: Rock data is retrieved, stored, compared, or removed successfully.

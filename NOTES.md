## API Overview

- API stands for Application Programming Interface
- It is a way for two pieces of software to communicate with each other, even if they are built - different programming languages
- The API acts as an interface between the two applications, enabling them to exchange information
- A common setup is a client-server relationship, where the client consumes information from the server

## JSON

- JSON (JavaScript Object Notation) is the standard language used for APIs to communicate information
- It is a language or notation for describing information and consists of key-value pairs
- It is supported by almost all programming languages
- JSON is like an associative array or an object in JavaScript/dictionary in Python

## REST API

- REST stands for Representational State Transfer
- It is a means of communication over the internet or the web
- REST API involves making requests similar to requesting a website, but instead of HTML, you receive JSON

## Example API

- An example API is a back-end software written in Python that communicates with a database
- The back-end software communicates with the database to store all the information and data
- Other pieces of software can communicate with the back-end software by accessing API endpoints
- API endpoints are specific actions defined by the API, such as getting a list of drinks or - comments
- An example API endpoint could be "/drinks" to get a list of drinks and rate them or categorize them.

## Advantages of a Separated Front-End and Back-End Setup

- Security

      - Protects sensitive information by not exposing it directly to the client application, which is often viewable to the person using the

  software.
  Prevents unauthorized access to the database, such as tinkering around or dropping the database.

- Versatility

      - The same back-end can be shared by multiple front-end applications, leading to data

  synchronization.
  The setup allows for easy development of new front-end applications, such as mobile apps.

- Modularity

  - The separation of front-end and back-end allows for swapping out different components without necessarily breaking the application.
    Back-end changes can be made without requiring an update to the front-end application.

- Interoperability
  - Public endpoints can be exposed, allowing for third-party development of new front-end applications.
    Public APIs can be consumed by others to automate different tasks or create new and improved applications.

## Methods of Requesting Data from Server

- Get

  - Used to retrieve data from the server. Often written in all uppercase letters

- Post

  - Used to write data to the server

- Delete

  - Used to delete data from the server

- Put

  - Used to update data on the server
    Confusing for new users due to its close similarity to Post

## Difference between Post and Put

| Post                                                                                                  | Put                                                                                                      |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Used to add a new resource                                                                            | Used to replace Requires identification of the resource to be replaced, often done with an ID a resource |
| Not guaranteed to be idempotent (able to be executed multiple times without side effects) by the spec | Guaranteed to be idempotent by the spec                                                                  |

## Correlation with CRUD Operations

- Create Data: Post
- Read Data: Get
- Update Data: Put
- Delete Data: Delete

## Consuming StackOverflow API

api.stackexchange.com

https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow
Postman

# ALU-AirBnB Clone

## Project Description

The **ALU-AirBnB Clone** project focuses on developing the console part of the AirBnB clone application. This involves creating a command interpreter to manage various AirBnB objects. The primary goals are:

- **BaseModel Class:** Implement a parent class called `BaseModel` that handles initialization, serialization, and deserialization of instances.
- **Serialization/Deserialization:** Develop a simple flow for converting instances to and from JSON strings, dictionaries, and files.
- **AirBnB Classes:** Create classes representing various AirBnB entities (e.g., User, State, City, Place) that inherit from `BaseModel`.
- **File Storage Engine:** Implement a file storage system to manage object persistence.
- **Unit Testing:** Develop unit tests to validate all classes and the storage engine.

## Command Interpreter

The command interpreter is a crucial part of the AirBnB clone project. It allows for the following operations:

### How to Start It

1. Clone the Repository
2. Navigate to the Project Directory
3. Run the Command Interpreter
### How to Use It

Once the command interpreter is running, I will use it to manage AirBnB objects through various commands:

- **Create a New Object:**
  ```bash
  create <class_name> [<arguments>]
  ```
- **Retrieve an Object:**
  ```bash
  show <class_name> <object_id>
  ```
- **Update an Object:**
  ```bash
  update <class_name> <object_id> <attribute_name> <new_value>
  ```
- **Destroy an Object:**
  ```bash
  destroy <class_name> <object_id>
  ```

- **Count Objects:**
  ```bash
  count <class_name>
  ```

### Examples

- **Creating a New User:**
  ```bash
  create User name="Agape" email="agape@example.com"
  ```
  Output:
  ```
  User object created with ID: <generated_id>
  ```

- **Showing a User:**
  ```bash
  show User <generated_id>
  ```
  Output:
  ```
  User(<generated_id>) {name: "Agape", email: "agape@example.com", ...}
  ```

- **Updating a User's Email:**
  ```bash
  update User <generated_id> email "diane_new@example.com"
  ```
  Output:
  ```
  The user updated successfully.
  ```

- **Destroying a User:**
  ```bash
  destroy User <generated_id>
  ```
  Output:
  ```
  User with ID <generated_id> destroyed.
  ```

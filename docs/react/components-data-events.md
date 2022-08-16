[github reference](https://github.com/academind/react-complete-guide-code/tree/01-getting-started)
-> the github tags/branches list the code

## section 3. React basics

-> jsx is a returned html, can only have 1 html element
-> component import/export
-> passing data via props


## section 4. user interaction and state

### eventListener and eventHandler

see Expenseitem.js

- onClick -> eventListener
- calls the handler

```
const ExpenseItem = (props) => {
    const clickHandler = () => {
        ...
    };
    return (
        ...
            <button onClick={clickHandler}>Change title</button>
    )
}
```

### change what shows up on the screen

see Expenseitem.js

- component is a function 
  - someone need to call it
  - we need to tell react about it
  - this is what State is about

import useState

```
import React, { useState } from "react";
```

call useState in a react component; useState is:
- registers some state for the component instance in which it is called
  - only the instance is executed again
  - react knows is sueState was initialy initialized or not
- special type of variable
- give it initial state
- give it a new value by calling it a function
- returns an array of 2 elements
  - 1st element: value
  - 2nd element: function to update it

```
const ExpenseItem = (props) => {
    const [title, setTitle] = useState(props.title);

    const clickHandler = () => {
        setTitle('Updated!');
        console.log(title);
    };
    ...
}
```

### add new expense

see NewExpense directory

### get new user input

- add onchange eventHandler pinting to a fn
- the fn uses the event object
  - event object has manay attributes, we are interested in event.target.value
  - changes at every keystroke

onChange

```
  return (
    <form>
      <div className="new-expense__controls">
        <div className="new-expense_control">
          <label>Title</label>
          <input type="text" onChange={titleChangeHandler} />
    ...
```

event Handler

```
const titleChangeHandler = (event) => {
    console.log(event.target.value);
  };
```

### what do we do with the value

- we need to store it so we can use it
- use the useState -> import and initialize the value/function returned
- we store it in a variable that is detached from the component

```
import React, {useState} from "react";
```

```
    const [enteredTitle, setEnteredTitle] = useState("");

    const titleChangeHandler = (event) => {
        setEnteredTitle(event.target.value);
    };
```

-> multiple state updates have different options, preferred is the one not commented out

see ExpenseForm.js

```
const ExpenseForm = () => {
  const [enteredTitle, setEnteredTitle] = useState("");
  const [enteredAmount, setEnteredAmount] = useState("");
  const [enteredDate, setEnteredDate] = useState("");
  /*
  const [userInput, setUserInput] = useState({
    enteredTitle: "",
    enteredAmount: "",
    enteredDate: "",
  });
  */

  const titleChangeHandler = (event) => {
    setEnteredTitle(event.target.value);
    /*
    setUserInput({
      ...userInput, // keep the value and dont overrride -> we depend on the previous state snapshot
      enteredTitle: event.target.value,
    });
    */
    /*
    setUserInput((prevState) => {
      return { ...prevState, enteredTitle: event.target.value };
    }); // this is the better code, since the previous state is always the latest, if state update depends on previous state
    */
  };

  const amountChangeHandler = (event) => {
    setEnteredAmount(event.target.value);
    /*
    setUserInput({
      ...userInput, // keep the value and dont overrride -> we depend on the previous state snapshot
      enteredAmount: event.target.value,
    });
    */
    /*
    setUserInput((prevState) => {
        return { ...prevState, enteredAmount: event.target.value };
      }); // this is the better code, since the previous state is always the latest, if state update depends on previous state
      */
  };

  const dateChangeHandler = (event) => {
    setEnteredDate(event.target.value);
    /*
    setUserInput({
      ...userInput, // keep the value and dont overrride -> we depend on the previous state snapshot
      enteredDate: event.target.value,
    });
    */
    /*
    setUserInput((prevState) => {
        return { ...prevState, enteredDate: event.target.value };
      }); // this is the better code, since the previous state is always the latest, if state update depends on previous state
      */
  };

```

### do something with the input

- add onsubmit button
  - avoid reloading the page once the button is pressed which is the default js behavior
- keep the data in an Object that uses the enteredData

```
    const submitHandler = (event) => {
      event.preventDefault(); // avoids to reload the page on submit botton

      const expenseData = {
          title: enteredTitle,
          amount: enteredAmount,
          date: new Date(enteredDate)
      }

      console.log(expenseData)
  }

```

### 2way binding -> to clear the input

- by using state we can implement 2-way binding -> pass a new value back to the input
- for input we just dont listen but we can resubmit the input
  - this is useful to reset the data in the form once submitted

1. add a value attribute to the input
2. clear the input upon call

### child to Parent component communication

we are able to gather the data and clear the input -> but we need the data in App.js iso in the ExpenseForm
+ we want to enrich it, but given it an id

how?
- create an eventProp
- pass a fn as a value
- pass fn from child -> parent
- when fn is called -> data can be gathered


in the parent Component

1. add the on... element which has a function pointer ->

```
 <ExpenseForm onSaveExpenseData={saveExpenseDataHandler}/>
```

2. define the function

```
const saveExpenseDataHandler = (entereredExpenseData) => {
        const expenseData = {
            ...entereredExpenseData,
            id: Math.random().toString()
        }
        console.log(expenseData)
    }
```

in the child component

3. add props to the component to receive the fucntion
4. in the submit Handler callprops.onSaveExpenseData(expenseData);
  - onSaveExpenseData name is matching the original name in step 1


Terminology
- stateful components -> manage state, state is distributed to props
  - Expenses
  - ExpenseForm
- stateless components -> focus on output
  - ExpenseItem

## section 5. rendering lists and conditional content

Expense.js

### we want to render the list dynamically

- use a dynamic expression {}
- in the dynamic expression use a jsarray.map function which creates a new array from the original array
  - we transform to a JSX element

```
  return (
    ...
        {props.items.map((expense) => (
          <ExpenseItem
            title={expense.title}
            amount={expense.amount}
            date={expense.date}
          />
        ))}
    ...
```

### we want to add items to the list

- in App.js
- add a const outside the function that sets the initial data
- use state to handle dynamic state
  - create const for newState and update function
  - call function to update the state -> use a function for THIS !! as per below

```
setExpense((prevExpenses) => {
      return [expense, ...prevExpenses]
    })
```

### key warning

in expense.js

add uuid in the list with the key
-> add a key to the list of items to assist react in updating where and entry should be listed

```
key={expense.id}
```

### conditional content

see Expenses.js

different output under different conditions
e.g. list items but when there is no data -> we should give a message

- define a variable with JSX content
- perform if statement to see which content to render
- render the result which could be either content

```
// store JSX content in a variable
  let expensesContent = <p>No expenses found.</p>;

  if (filteredExpenses.length > 0) {
    expensesContent = filteredExpenses.map((expense) => (
      <ExpenseItem
        key={expense.id}
        title={expense.title}
        amount={expense.amount}
        date={expense.date}
      />
    ))
  }
```

new approach with ExpensesList.js


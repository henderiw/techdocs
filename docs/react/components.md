# react component

all user interfaces are made up of components
what make up a component
- html
- css (least important in react)
- javascript

why
- reusability (dont repeat yourself)
- seperation of concerns (keeping it small and managable)

declarative approach
- define the desired target state
- react figures actual javascript DOM instructions

A COMPONENT IS A JS FUNCTION -> FUNCTIONAL COMPONENT
-> param: props
-> retrn JSX

## App.js is a root component

rendered in a single html page

## class based components

Section 13
project: 13-class-based-components
file: App.js, Login.js

this is used a lot in the past -> should no longer be used
- A component can also be class based components

### what and why

they are an alternative to functional components
-> called: CLASS BASED COMPONENTS 

they were required before react 16.8
-> you had to use them with state, useEffects, etc
-> class-based component can't be used with react hooks

```
class Product extend Component {
    render() {
        return <h2>A Product!</h2>
    }
}
```

[code examples](https://github.com/academind/react-complete-guide-code/tree/13-class-based-cmp)

FUNCTIONAL COMPONENT can interact with FUNCTIONAL COMPONENTS

### how to transform from functional componentn to class base components

class is a js construct

original functional component

```
const User = (props) => {
  return <li className={classes.user}>{props.name}</li>;
};
```

class based component

```
// to get props access
import {Component} from 'react'

class User extends Component{
  // no constructor initialialization
  //constructor(){}

  render() {
    // this.props is available because
    return <li className={classes.user}>{this.props.name}</li>;
  }
}

```

### state in class based components

in class based component
- state has to be an object and there is only 1

functional based component

```
const Users = () => {
  const [showUsers, setShowUsers] = useState(true);

  const toggleUsersHandler = () => {
    setShowUsers((curState) => !curState);
  };

  const usersList = (
    <ul>
      {DUMMY_USERS.map((user) => (
        <User key={user.id} name={user.name} />
      ))}
    </ul>
  );

  return (
    <div className={classes.users}>
      <button onClick={toggleUsersHandler}>
        {showUsers ? 'Hide' : 'Show'} Users
      </button>
      {showUsers && usersList}
    </div>
  );
};
```

class based component

[this explained](https://academind.com/tutorials/this-keyword-function-references)

```
class Users extends Component {
  constructor() {
    super();
    this.state = {
      showUsers: true,
      more: 'Test', // exmaple to show the state object is flexible
    }
  }
  toggleUsersHandler() {
    // react merges the object the old state Object
    this.setState((curState) => {
      return {showUsers: !curState.showUsers}
    })
  }

  render() {
    const usersList = (
      <ul>
        {DUMMY_USERS.map((user) => (
          <User key={user.id} name={user.name} />
        ))}
      </ul>
    );

    return (
      <div className={classes.users}>
        <button onClick={this.toggleUsersHandler.bind(this)}>
          {this.state.showUsers ? 'Hide' : 'Show'} Users
        </button>
        {this.state.showUsers && usersList}
      </div>
    );
  }
}
```

### lifecycle methods - side effects

componentDidMount() 
- called once component was mounted (was evaludate & rendered)
- similar to useEffect(..., [])

componentDidUpdate()
- called once component updated (was evaluated &rendered)
- similar to useEffect(..., [someValue])

componentWillUnmount()
- called right before component is unmounted (removed from the DOM
- similar to cleanup in useEffect

see: UserFinder.js

```

```

### context in class based component

there can only be 1 staticContext connected to a comp

see example
- store/user-context.js
- App.js
- UserFinder.js

### error boundaries

see Users.js

error thrown in parent component
-> componentDidCatch lifecycle method makes this component an Error Boundary
-> this can only be used in CLASS BASED COMPONNET
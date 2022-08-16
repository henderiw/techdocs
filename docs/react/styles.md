## 06 styling

3 approaches
- css only -> seeprate css files
- styled components -> no need for seperate css files
- css modules -> preffered approach (keep seperate css files with a x.module.css name)

### how to change styles dynamically

#### using in-line styles

uses 02-course-goal-tracker
component: CourseInput.js

if input is invalid represnt this to the user

1. define a state which track the input is valid or not

```
const [isValid, setIsValid] = useState(true)
```

2. modify the state based on invalid input

```
 const formSubmitHandler = event => {
    event.preventDefault();
    // check if the goal enterValue is empty
    if (enteredValue.trim().length === 0) {
      setIsValid(false);
      return;
    }
    props.onAddGoal(enteredValue);
  };
```

3. modify the state if input is vald

```
const goalInputChangeHandler = event => {
    //
    if (event.target.value.trim().length > 0) {
      setIsValid(true);
    }
    setEnteredValue(event.target.value);
  };
```

4. change in-line styles based on the state of isValid

style needs an object and style elements are lowerCamelCase

```
return (
    <form onSubmit={formSubmitHandler}>
      <div className="form-control">
        <label style={{ color: !isValid ? 'red' : 'black' }}>Course Goal</label>
        <input style={{ borderColor: !isValid ? 'red' : 'black', background: !isValid ? 'salmon' : 'transparent' }} type="text" onChange={goalInputChangeHandler} />
      </div>
      <Button type="submit">Add Goal</Button>
    </form>
  );
```

#### using dynamic classes

1. add in .css file the following

```
.form-control.invalid input {
  border-color: red;
  background: #ffc7d7;
}

.form-control.invalid label {
  color: red;
}
```

2. use the dynamic css classes using backticks

`` : backticks -> javascript template literal
- returns a regular string
- you can inject dynamic values with ${...}
  - within the {} -> javascript expression

```
return (
    <form onSubmit={formSubmitHandler}>
      <div className={`form-control &{!isValid ? 'invalid' : ''}`}>
        <label >Course Goal</label>
        <input type="text" onChange={goalInputChangeHandler} />
      </div>
      <Button type="submit">Add Goal</Button>
    </form>
  );
```

### styled components

.css classes are global -> not scoped
we can use selectors carefully, so we need to be carefull here

2 approaches

#### approach1: package styled components

[styled components](https://styled-components.com)

components that have styled attached to them:

install

```
npm install --save styled-components
```

see button.js

- remove css and react import
- import styled from 'styled-components';
- remove jsx code
- inset the following code
    - button is a method on the styled component
    - `` -> js syntax: tagged template literal
    - what we paste in between `` we pass to the button method
    - the css styles
      - remove button
      - replace button with & for 
```
const Button = styled.button`
  font: inherit;
  padding: 0.5rem 1.5rem;
  border: 1px solid #8b005d;
  color: white;
  background: #8b005d;
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.26);
  cursor: pointer;

  &:focus {
    outline: none;
  }

  &:hover,
  &:active {
    background: #ac0e77;
    border-color: #ac0e77;
    box-shadow: 0 0 8px rgba(0, 0, 0, 0.26);
  }
`;
```

exmaple coureInput.js

- remove css and react import
- import styled from 'styled-components';
- add style component

```
const FormControl = style.div` 
  margin: 0.5rem 0;
  
  & label {
    font-weight: bold;
    display: block;
    margin-bottom: 0.5rem;
  }
...
```

- add Component iso div style
  - on invalid is to be added

```
return (
    <form onSubmit={formSubmitHandler}>
      <FormControl className={!isValid && 'invalid'}>
        <label >Course Goal</label>
        <input type="text" onChange={goalInputChangeHandler} />
      </FormControl>
      <Button type="submit">Add Goal</Button>
    </form>
  );
```

Other option is using props with backticks

- use invalid props

```
  return (
    <form onSubmit={formSubmitHandler}>
      <FormControl invalid={!isValid}>
        <label >Course Goal</label>
        <input type="text" onChange={goalInputChangeHandler} />
      </FormControl>
      <Button type="submit">Add Goal</Button>
    </form>
  );
```

- consume the props within the backticks

```
const FormControl = styled.div` 
  margin: 0.5rem 0;
  
  & label {
    font-weight: bold;
    display: block;
    margin-bottom: 0.5rem;
    color: ${props => (props.invalid ? 'red' : 'black')};;
  }

  & input {
    display: block;
    width: 100%;
    border: 1px solid ${props => (props.invalid ? 'red' : '#ccc')};
    background: ${props => (props.invalid ? '#ffc7d7' : 'transparent')};;
    font: inherit;
    line-height: 1.5rem;
    padding: 0 0.25rem;
  }

  & input:focus {
    outline: none;
    background: #fad0ec;
    border-color: #8b005d;
  }
`
```

using media queries -> see button.js

- between ``
  - default width: 100%
  - 

#### approach2: css modules

only available in projects that are configured to use css modules

see button.js

- import react again
- change css import to -> import styles from './Button.module.css';
- change the css filename to Button.module.css
- change the Buton component to use the styles

```
const Button = props => {
  return (
    <button type={props.type} className={styles.button} onClick={props.onClick}>
      {props.children}
    </button>
  );
};
```
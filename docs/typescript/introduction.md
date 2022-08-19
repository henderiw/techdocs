## what is typescript

extends javascript

[typescript docs](https://www.typescriptlang.org)

adds static typing to javascript -> to prevent errors
javascript is dynamically typed

DOES NOT RUN in the broser
-> we need to compile TS to JS to run in the browser

[course examples](https://github.com/academind/react-complete-guide-code/tree/27-react-typescript)

## install

npm install typescript

compile

npx tsc
-> requires a configuration file

npx tsc with-typescript.ts

## props

use generics



```
import Todo from '../models/todo'
// the base prop always has children -> use generic types
// + set the concrete type for this generic FC type
const Todos: React.FC<{ items: Todo[] }> = (props) => {
  return (
    <ul>
      {props.items.map((item) => (
        <li key={item.id}>{item.text}</li>
      ))}
    </ul>
  );
};

export default Todos;
```

## data model

```

# react context

section: 10
project: 06-useredeucer-starting-project
file: App.js, Login.js

## what

- passing a lot of data between lots of components using props -> this is a bit to much if we just forward the data
- data is needed in another component -> we can lift state up, but it can become cumbersome
- avoids props chains

with context


## how

add folder in components -> store

file auth-context.js -> this is not a component

```
import React, { useState, useEffect } from 'react';

// contains an object
// providing and consuming
const AuthContext = React.createContext({
    isLoggedIn: false,
    onLogout: () => { }, // this is added for IDE auto-completion
    onLogin: (email, password) => { }
});
```


- AuthContext is not a component, but will contain a component -> we export this, so we provide it

1. provider ctx -> all component that are wrapped to in get access to it 
   - needed when context value/data changes
2. consume ctx -> AuthContext.Consumer or useContext hook

in App.js -> provider

```
import AuthContext from './store/auth-context';

see later optimized example
```

in Navigaton.js -> consumer

there is 2 ways to consume context.
- AuthContext.Consumer
- useContext hook


AuthContext.Consumer example
```
const Navigation = (props) => {
    return (
        <AuthContext.Consumer>
            {(ctx) => {
                return (

                )
            }}
        </AuthContext.Consumer>
    )
}
```

useContext hook

```
import React, {useContext} from 'react';

import classes from './Navigation.module.css';
import AuthContext from '../../store/auth-context';

const Navigation = () => {
  // ctx is a context value
  const ctx = useContext(AuthContext);
  return (
    <nav className={classes.nav}>
      <ul>
        {ctx.isLoggedIn && (
          <li>
            <a href="/">Users</a>
          </li>
        )}
        {ctx.isLoggedIn && (
          <li>
            <a href="/">Admin</a>
          </li>
        )}
        {ctx.isLoggedIn && (
          <li>
            <button onClick={ctx.onLogout}>Logout</button>
          </li>
        )}
      </ul>
    </nav>
  );
};

export default Navigation;
```

### centralize all authentication code in 1 place

in authContext.js

```
import React, { useState, useEffect } from 'react';

// contains an object
// providing and consuming
const AuthContext = React.createContext({
    isLoggedIn: false,
    onLogout: () => { }, // this is added for IDE auto-completion
    onLogin: (email, password) => { }
});

// this is a real provider component, we can import useState 
// we manage the complete authentication state here
// clean logic from the App.js code
export const AuthContextProvider = (props) => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    useEffect(() => {
        const storedUserLoggedInInformation = localStorage.getItem('isLoggedIn');
    
        if (storedUserLoggedInInformation === '1') {
          setIsLoggedIn(true);
        }
      }, []);

    const logoutHandler = () => {
        // We should of course check email and password
        // But it's just a dummy/ demo anyways
        localStorage.setItem('isLoggedIn', '1');
        setIsLoggedIn(false);
    }

    const loginHandler = () => {
        localStorage.removeItem('isLoggedIn');
        setIsLoggedIn(true);
    }

    return <AuthContext.Provider value={{ isLoggedIn: isLoggedIn, onLogout: logoutHandler, onLogin: loginHandler }}>{props.children}</AuthContext.Provider>
}
```

in index.js -> import the AuthContextProvider and wrap App inside it to give it access to the authentication context

```
import React from 'react';
import ReactDOM from 'react-dom/client';

import './index.css';
import App from './App';
import { AuthContextProvider } from './store/auth-context';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <AuthContextProvider>
        <App />
    </AuthContextProvider>
);

```

in App.js

we need to useContext and pass the AuthContext object

```
import React, {useContext} from 'react';

import Login from './components/Login/Login';
import Home from './components/Home/Home';
import MainHeader from './components/MainHeader/MainHeader';
import AuthContext from './store/auth-context';

function App() {
  const ctx = useContext(AuthContext);

  return (
    <React.Fragment>
      <MainHeader />
      <main>
        {!ctx.isLoggedIn && <Login />}
        {ctx.isLoggedIn && <Home />}
      </main>
    </React.Fragment>
  );
}

export default App;
```

also tap in authContext in Home and Login components

### limitations

- ctx is great for app wide state
- not usable for component configuration -> so the button can only be used for 1 thing, button should be reusable
  - used for login component
  - used for logout
  - props is much better here
- Ctx is not optimized for high frequency changes (multiple changes per second)
- 
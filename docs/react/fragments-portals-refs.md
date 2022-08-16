# react

## fragments

- JSX limitation
  - if we have adjacent root level elements we get an error
    -> option1: workaround is mapping it into a div or any element
        we can end up with div soup
    -> option2: use an array but this is getting other challanges       
        -> we need a key on all the element in a list of data
        -> we could use hardcoded keys
    -> option 3: creating a wrapper component 9see (03-user-input)
- option 3 comes from react -> React.Fragment

return


## portals

- get a cleaner dom
- modal is an overlay on the entire page -> it is above everything else

in public/index.html add

```
    <div id="backdrop-root"></div>
    <div id="overlay-root"></div>
```

in ErrorModal

- define 2 new components
- create Portal -> moves the component somewhere else

```
const Backdrop = props => {
    return <div className={styles.backdrop} onClick={props.onConfirm}></div>;
}

const ModelOverlay = props => {
    return <Card className={styles.modal}>
        <header className={styles.header}>
            <h2>{props.title}</h2>
        </header>
        <div className={styles.content}>
            <p>{props.message}</p>
        </div>
        <footer className={styles.actions}>
            <Button onClick={props.onConfirm}>Okay</Button>
        </footer>
    </Card>

}

const ErrorModal = (props) => {
    // this is a reusable module that expects the following attributes from props
    // -> title
    // -> message

    // there are 2 onClick -> one for the backdrop and one for the button
    return (
        <React.Fragment>
            {ReactDOM.createPortal(
                <Backdrop onConfirm={props.onConfirm} />,
                document.getElementById('backdrop-root')
            )}
            {ReactDOM.createPortal(
                <ModelOverlay 
                    title={props.title} 
                    message={props.message} 
                    onConfirm={props.onConfirm} 
                />,
                document.getElementById('overlay-root')
            )}

        </React.Fragment>

    )
}
```

## refs

see AddUser.js in 03-user-input

refs -> references

-> allow us to get access to other doms and work with them
e.g. we listen to every keystroke on user input in order to get access to all the input parameters in the add user form, we store this in the state
-> setup a conn between a html element and other js code

useRefs() -> uses a default value (not used), allows to ref the html element
-> uses the current prop -> it is the real dom node -> you can manipulate it but you should not do this

-> ref prop in html element; similar to the key prop they are always defined
-> set the value in the value equal to the html element


-> This is called an UNCONTROLLED component
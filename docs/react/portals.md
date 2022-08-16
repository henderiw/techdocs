# react portals

section: 09
project: 03-user-input
files: 
- public/index.html
- components/UI/ErrorModal.js

Goal:
- get a cleaner dom
- move the react component to another place in the DOM
- modal is an overlay on the entire page -> it is above everything else -> if it is nested it is not good code and can lead to issues with styling, etc


2 things are needed:
1. place to port the component to -> public/index.html (backdrop-root, overlay-root)
2. let the component know where to go

in public/index.html add

```
    <div id="backdrop-root"></div>
    <div id="overlay-root"></div>
```

in ErrorModal

- define 2 new components: Backdrop, modelOverlay
- create Portal -> moves the component somewhere else
  - ReactDOM.createPortal -> reactDom is the react part that intercat with
    - createPortal: uses 2 argument
      1. react component in JSX format
      2. pointer to the container in the real DOM the component needs to render to -> we select the elemnt to render to we defined in public/index.html
         - document.getElementById('backdrop-root')
         - this is not react

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
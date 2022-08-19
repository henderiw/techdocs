# react animations

section 24

- css transitions and animation
- 3rd part libraries

[sample code](https://github.com/academind/react-complete-guide-code/tree/24-animations)

## what

## css transitions

- fine way in animating
- display option cannot e used

limitation:
- modal div and backdrop div are always visible -> it is in the dom but not visible
  - slows it down
- css animation and transitions can give issues

## ReactTransitionGroup

[react-transition-group](https://reactcommunity.org/react-transition-group/)

- library: not an official react package
- Transiton component -> controls the transition of the wrapped elements

```
<Transition in={this.state.showBlock} timeout={1000}>
    { state => (
        <div
            opactiy: state === 'existed' ? 1 : 0
        />
    )}
</Transition>
```

transitionEvent
- onEnter
- onEntering
- onEnter
- onExist
- onExiting
- onExited

## CCSTransition Component

part of the previous 
-> no function required unlike the 
-> classNames defines the css classes to be added on the element

trunk name for css and we can add more granular classes

-> more control on which css classes to use

## TransitionGroup

-> animates lists

alternative packages
- react-motion
- react-move
- react-router-transation (animating switching of pages)

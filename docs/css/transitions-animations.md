# transitions and animations

transitions
- built in animations
- transition property
  - which properties to watch and animated if it changes
  - how to animate it
  - how fast to change
animation

[css transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions)
[css animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations)
[transitionable properties](https://www.w3.org/TR/css-transitions-1/#animatable-properties)

## transition

.modal {
  position: fixed;
  /*display: none;*/
	opacity: 0;
	transform: translateY(-3rem);
  z-index: 200;
  top: 20%;
  left: 30%;
  width: 40%;
  background: white;
  padding: 1rem;
  border: 1px solid #ccc;
  box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.5);
}

## transiton property

```
The transition  property is used as see in the previous video:

transition: WHAT DURATION DELAY TIMING-FUNCTION; 

Example:

transition: opacity 200ms 1s ease-out; 

Can be translated to: "Animate any changes in the opacity  property (for the element to which the transition  property is applied) over a duration of 200ms. Start fast and end slow, also make sure to wait 1s before you start".

Instead of this shorthand, you can also specify the four individual properties:

1) transition-property  (https://developer.mozilla.org/en-US/docs/Web/CSS/transition-property => transition-property: opacity; 

2) transition-duration  (https://developer.mozilla.org/en-US/docs/Web/CSS/transition-duration) => transition-duration: 200ms; 

3) transition-timing-function  (https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function) => transition-timing-function: ease-out; 

Possible timing function values are: ease-out , ease-in , linear , cubic-bezier()  and a couple of others. See the above link as well as the next lecture for more details.

4) transition-delay  (https://developer.mozilla.org/en-US/docs/Web/CSS/transition-delay) => transition-delay: 1s; 

You can read the official MDN article on CSS transitions here: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions
```

## display function

incompatible with transition

## animations

keyframe with start and end state

```
@keyframes wiggle {
	from {
		transform: rotateZ(0);
	}
	to {
		transform: rotateZ(10deg);
	}
}
```

## animation property

```
.main-nav__item--cta {
	animation: wiggle 200ms 3s;
}
```

```
The animation  property is used as see in the previous video:

animation: NAME DURATION DELAY TIMING-FUNCTION ITERATION DIRECTION FILL-MODE PLAY-STATE; 

Example:

animation: wiggle 200ms 1s ease-out 8 alternate forwards running; 

Can be translated to: "Play the wiggle keyframe set (animation) over a duration of 200ms. Between two keyframes start fast and end slow, also make sure to wait 1s before you start. Play 8 animations and alternate after each animation. Once you're done, keep the final value applied to the element. Oh, and you should be playing the animation - not pausing."

Instead of this shorthand, you can also specify the individual properties:

1) animation-name  (https://developer.mozilla.org/en-US/docs/Web/CSS/animation-name => animation-name: wiggle; 

2) animation-duration  (https://developer.mozilla.org/en-US/docs/Web/CSS/animation-duration) => animation-duration: 200ms; 

3) animation-timing-function  (https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timing-function) => animation-timing-function: ease-out; 

Possible timing function values are: ease-out , ease-in , linear , cubic-bezier()  and a couple of others. See the above link for more details.

4) animation-delay  (https://developer.mozilla.org/en-US/docs/Web/CSS/animation-delay) => animation-delay: 1s; 

5) animation-iteration-count  (https://developer.mozilla.org/en-US/docs/Web/CSS/animation-iteration-count) => animation-iteration-count: 8; 

6) animation-direction  (https://developer.mozilla.org/en-US/docs/Web/CSS/animation-direction) => animation-direction: alternate; 

7) animation-fill-mode  (https://developer.mozilla.org/en-US/docs/Web/CSS/animation-fill-mode) => animation-fill-mode: forwards; 

8) animation-play-state  (https://developer.mozilla.org/en-US/docs/Web/CSS/animation-play-state) => animation-play-state: running; 

You can read the official MDN article on CSS animations here: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations
```

## multiple steps

```
@keyframes wiggle {
	0% {
		transform: rotateZ(0deg);
	}
	50% {
		transform: rotateZ(5deg);
	}
	100% {
		transform: rotateZ(10deg);
	}
}
```

## javascript

see js file


## react useCallback

## fragments

section: 12
project: 12-how-react-works
file: App.js

## react memo

react reevalutes the components whenever prpos, state or ctx changes
-> react executes component functions
-> a parent reevaluation will also reevaluate all children -> is this not creating to much work
  ->  React.memo(DemoOutput) allows to skip component reevaluation that avoids react component reevaluation is props dont change
  -> this has a cost since now react has to store props -> so it depends on the component if this is usefull
  -> a function if defined it is recreated -> this reevaluates the component
    because react compares props, bool works, fn does not work as they are seen as an Object
  -> solution: useCallback: the fn are stored a fn in react storage to allow the comparison to succeed
only if changes happens the realDOM will be updated

so it does virtual DOM diffing

## useCallback

works in combination with React.memo

[info](https://academind.com/tutorials/reference-vs-primitive-values)

stores the function in global state to be able to compare.
Since js uses closuresm the variables would be stored from the beginning -> allowToggle dependencies allows to work around with this

[closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)

```
const toggleParagraphHandler = useCallback(() => {
    if (allowToggle) {
      setShowParagraph((prevShowParagraph) => !prevShowParagraph);
    }
  }, [allowToggle])

  const allowToggleHandler = () => {
    setAllowToggle(true);
  }
```


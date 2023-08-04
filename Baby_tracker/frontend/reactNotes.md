# useState
Is a Hook that allows you to add state to functional components.It lets you declare a state variable and provide a way to update its value triggering a re-render of the component

```javascript
import React, {useState} from 'react';

function Counter() {
    // Declare a state variable named "count" with an initial value of 0
    const [count, setCount] = useState(0);

    // Event handler function to increment the count
    const increment = () => {
        setCount(count + 1);
    };

    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={increment}>Increment</button>
        </div>
    );
}

export default Counter;
```
useState function returns an array with two elements
- The current state value
- A function that allows you to update the state
When you call useState() function, you pass in the initial value for the state.This initial value sets the initial state of your component

The updater function returned by 'useState' accepts a new value, which represents the updated state which you want to set.
When you call this updater function with a new value, React will re-render your component with the updated state, causing any relevant UI changes to be reflected.

# break down of how it works
- `useState(initialValue)` returns an array with the current state value and the updater function e.g `useState(0)` returns `[0, updaterFunction]`
- You can use array destructuring to extract the current state value and the updater function into separate variables. e.g `const [count, setCount] = useState(0);`
- To update the state, you call the updater function e.g `setCount(newValue)` passing in the new value that you want to set for the state variable.

# useEffect

`useEffect` hook is used to perform side effects in functional components.Side effects can include tasks like data fetching, DOM manipulation, subscriptions, and more.`useEffect` allows you to manage these side effects in a way that is consistent with the component's lifecycle.

- The `useEffect` hook allows you to perform side effects in functional components.It runs after the component has rendered, and you can use it to manage tasks that should occur outside the normal rendering flow.

```javascript
import React, {useState, useEffect } from 'react';

function RandomQuote() {
    const [quote, setQuote] = useState('');
    // useEffect is used to fetch a random quote once the component has rendered
    useEffect(() => {
        fetch('https://api.quotable.io/random')
        .then(response => response.json())
        .then(data => {
            setQuote(data.content);
        });
    },[]); //The empty depedence array means this effect runs once, similar to componentDidMount

    return (
        <div>
          <h2>Random Quote:</h2>
          <blockquote>{quote}</blockquote>
        </div>
    );
}

export default RandomQuote;
```
- import the `useState` and `useEffect` hooks from the 'react' library.
- Inside the `RandomQuote` component, we declare a state varibale named `quote` using the `useState` hook.This variable will hold the fetched quote.
- Use the `useEffect` hook to perform a side effect - fetching a random quote from the API.The `useEffect` function takes two arguments:a callback function and a depedency array.The callback function contains the code that will be executed as the side effect.The depedency array specifies which values this effect depends on.
- Inside the `useEffect` callback, we use the `fetch` function to make a GET request to the API.When the response is received, we extract the quote content and update the `quote` state using the `setQuote` function.
- The depedency array is provided as an empty array `[]`.This means that the effect will run only once, similar to how `componentDidMount` works in class components.If you provide values in the depedency array, the effect will run whenever any of those elements change.
- In the JSX, we render the fetched quote inside a `<blockquote>` element.

When the `RandomQuote` compenent renders, the `useEffect` hook will run after the initial render and fetch a random quote from the API.The fetched quote will be displayed on the screen.
import React, {useState} from 'react';
import './Counter.css';

export default function Counter() {
    const [counter, setCounter] = useState(0);


    const incrementCounter = () => {
        setCounter((counter) => counter >= 10 ? counter :counter + 1);
    }

    const decrementCounter = () => {
        setCounter((counter) => counter <= 0 ? counter :counter - 1);
    }




  return (
    <div className='couter-container '>
        <h1>{counter}</h1>
        <button onClick={incrementCounter}>+</button>
        <button onClick={decrementCounter}>-</button>

      
    </div>
  )
}

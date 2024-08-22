import React, { useState } from "react";
import Button from "./Button/Button";
import "./CounterTrails.css";

export default function CounterTrail() {
  const [counter, setCounter] = useState(0);
  const [timer, setTimer] = useState();
  const [direction, setDirection] = useState(true);

  const startCounter = () => {
    if (direction) {
      setTimer(
        setInterval(() => {
          setCounter((counter) => counter + 1);
        }, 1)
      );
    } else {
      setTimer(
        setInterval(() => {
          setCounter((counter) => counter - 1);
        }, 1)
      );
    }
  };

  const pauseCounter = () => {
    clearInterval(timer);
    setTimer();
  };

  const changeDirection = () => {
    setDirection((direction) => !direction);
  };

  return (
    <div>
      <h1>{counter}</h1>
      <div className="button-outer-container">
        <Button onClickHandler={startCounter}>Start</Button>
        <Button onClickHandler={pauseCounter}> Pause</Button>
        <Button onClickHandler={changeDirection}>
          {direction ? "Forward" : "Backword"}
        </Button>
      </div>
    </div>
  );
}

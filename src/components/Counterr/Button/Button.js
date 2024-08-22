import React from 'react';
import './Button.css'

export default function Button({children, onClickHandler }) {
  return (
    <div className='button-container'>
      <button onClick={onClickHandler}>{children}</button>
    </div>
  )
}

import React from 'react'
import './ProfileCard.css'

export default function ProfileCard({heading, email}) {

  return (
    <div className='profileCard-container'>
        <h1 className='profileCard-heading'>{heading}</h1>
        <p className='profileCard-para'>Email:{email}</p>
      
    </div>
  )
}

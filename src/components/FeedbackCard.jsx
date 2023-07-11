import React from 'react'
import { avatar, quotationMark } from '../assets'

const FeedbackCard = () => {
  return (
    <div className='bg-white p-8 rounded-3xl shadow-xl my-8 mx-2'>
      <div className='flex justify-between'>
        <div className='flex gap-4'>
                <img src={avatar} />
                <div>
                    <h1>Jenny Wilson</h1>
                    <p>UI-UX Designer</p>
                </div>
            
            </div>
            <img className='h-8' src={quotationMark} />
      </div>

      <div className='py-8'>
        <h3 className='text-lg'>I no longer have to disturb other artists for opinion. I've found the great stories on VOOCH. Creative.</h3>
      </div>
    </div>
  )
}

export default FeedbackCard
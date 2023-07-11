import React from 'react';
import { voochm } from '../assets';
import  {AiOutlineSearch} from 'react-icons/ai'

const Hero = () => {
  return (
    <div className='w-full bg-blue-200 py-24'>


        <div className='md:max-w-[1480px] m-auto grid md:grid-cols-2 max-w-[600px]  px-4 md:px-0'>
            
            <div className='flex flex-col justify-start gap-4'>
            <h1 className="text-8xl font-bold text-green text-center">
                Saving <br /> Money, &Time, <br /> Always.</h1>

                <div className='flex justify-center gap-4 py-4'>
                <button className="px-6 py-2 text-lg font-semibold bg-gray-800 text-white rounded-lg hover:bg-gray-700">
                    <i className="fab fa-apple mr-2"></i> UPLOAD
                </button>
                <button className="px-6 py-2 text-lg font-semibold border border-white text-white rounded-lg hover:bg-gray-100 hover:text-gray-800">
                    <i className="fab fa-google-play mr-2"></i> REVIEW
                </button>
                </div>
                
                

            </div>
            
            <img src={voochm} className="md:order-last  order-first" />



        </div>
        

    </div>
  )
}

export default Hero
import React from 'react';
import { voochm } from '../assets';
import  {AiOutlineSearch} from 'react-icons/ai'

const Hero = () => {
  return (
    <div className='w-full bg-white py-24'>
        <div className='md:max-w-[1480px] m-auto grid md:grid-cols-2 max-w-[600px]  px-4 md:px-0'>
            
            <div className='flex flex-col justify-start gap-4'>
                <p className='py-2 text-2xl text-[#EA3434] font-bold'>NO MORE GUESSWORK</p>
                <h1 className='md:leading-[72px] py-2 md:text-6xl text-5xl font-semibold'>Start to <span className='text-[#367DE8]'>SAVE</span> Courses
                    from <span  className='text-[#367DE8]'>300</span> Instructors 
                    & Institutions
                </h1>
                <p className='py-2 text-lg text-blue-600'>Helping you save Money and time, Always.</p>
                
                <form className='bg-white border max-w-[500px] p-4 input-box-shadow rounded-md flex justify-between'>
                    <input 
                        className='bg-white'
                        type="text"
                        placeholder='Browse category?'
                    />
                    <button>
                        <AiOutlineSearch 
                            size={20}
                            className="icon"
                            style={{color:'#000'}}

                        />

                    </button>
                </form>
            </div>
            
            <img src={voochm} className="md:order-last  order-first" />



        </div>
        

    </div>
  )
}

export default Hero
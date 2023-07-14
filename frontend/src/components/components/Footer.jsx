import React from 'react'
import { logo, vlogo } from '../assets'
import {FaFacebookF,FaDribbble,FaLinkedinIn,FaInstagram,FaBehance} from 'react-icons/fa'

const Footer = () => {
  return (
    <div className='w-full bg-white py-24'>
        <div className='md:max-w-[1480px] m-auto grid md:grid-cols-5 max-[780px]:grid-cols-2  gap-8 max-w-[600px]  px-4 md:px-0'>
            
            <div className='col-span-2'>
                <img src={vlogo} className="h-[80px] w-[100px]"/>
                <h3 className='text-2xl font-bold mt-10'>Contact Us</h3>
                <h3 className='py-2 text-[#6D737A]'>Call : 079999666</h3>
                <h3 className='py-2 text-[#6D737A]'>We have all the Arts, the best of arts. <br></br> Guaranteed value of your work or get your money back.</h3>
                <h3 className='py-2 text-[#363A3D]'>Email: vooch@mail.com</h3>
                <div className='flex gap-4 py-4'>
                        <div className='p-4 bg-[#D9D9D9] rounded-xl'><FaFacebookF size={25} style={{color:'#367DE8'}} /></div>
                        <div className='p-4 bg-[#D9D9D9] rounded-xl'><FaDribbble size={25} style={{color:'#367DE8'}} /></div>
                        <div className='p-4 bg-[#D9D9D9] rounded-xl'><FaLinkedinIn size={25} style={{color:'#367DE8'}} /></div>
                        <div className='p-4 bg-[#D9D9D9] rounded-xl'><FaInstagram size={25} style={{color:'#367DE8'}} /></div>
                        <div className='p-4 bg-[#D9D9D9] rounded-xl'><FaBehance size={25} style={{color:'#367DE8'}} /></div>

                </div>

            </div>

            <div>
                <h3 className='text-2xl font-bold'>Explore</h3>
                <ul className='py-6 text-[#6D737A]'>
                    <li className='py-2'>Home</li>
                    <li className='py-2'>About</li>
                    <li className='py-2'>Course</li>
                    <li className='py-2'>Blog</li>
                    <li className='py-2'>Contact</li>

                </ul>
            </div>

            <div>
                <h3 className='text-2xl font-bold'>Category</h3>
                <ul className='py-6 text-[#6D737A]'>
                    <li className='py-2'>Design</li>
                    <li className='py-2'>Development</li>
                    <li className='py-2'>Marketing</li>
                    <li className='py-2'>Business</li>
                    <li className='py-2'>Lifestyle</li>
                    <li className='py-2'>Photography</li>
                    <li className='py-2'>Music</li>

                </ul>
            </div>

            <div className='max-[780px]:col-span-2'>
                <h3 className='text-2xl font-bold'>Subscribe</h3>
                <h3 className='py-2 text-[#6D737A]'>To get our current trends and updates <br></br> Enter your email to get a montly Newsletter</h3>
                <form className='py-4'>
                    <input 
                        className='bg-[#F2F3F4] p-4 w-full rounded' 
                        placeholder='Email here' 
                    />
                    <button className='max-[780px]:w-full my-4 px-5 py-3 rounded-md bg-[#367DE8] text-white font-medium'>Subscribe Now</button>

                </form>


            </div>
        
        </div>
    </div>
  )
}

export default Footer
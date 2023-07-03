import React, { useState } from 'react';
import { logo, lock, hamburgerMenu, close } from '../assets';

const Navbar = () => {
  const [toggle, setToggle] = useState(false);
  const handleClick = () => setToggle(!toggle);

  return (
    <div className="w-full h-16 bg-white border-b">
      <div className="max-w-7xl mx-auto px-4 flex justify-between items-center h-full">
        <img src={logo} className="h-6" />

        <div className="hidden md:flex items-center space-x-4">
          <ul className="flex gap-4">
            <li>Home</li>
            <li>About</li>
            <li>Support</li>
          </ul>
        </div>

        <div className="hidden md:flex">
          <button className="flex items-center bg-transparent px-6 gap-2">
            <img src={lock} alt="Lock Icon" />
            Login
          </button>
          <button className="px-8 py-3 rounded-md bg-green-500 text-white font-bold">Sign Up For Free</button>
        </div>

        <div className="md:hidden" onClick={handleClick}>
          <img src={toggle ? close : hamburgerMenu} alt="Menu Icon" />
        </div>
      </div>

      <div className={toggle ? 'p-4 bg-white w-full border-b block' : 'hidden'}>
        <ul>
          <li className="p-4 hover:bg-gray-100">Home</li>
          <li className="p-4 hover:bg-gray-100">About</li>
          <li className="p-4 hover:bg-gray-100">Support</li>
          <div className="flex flex-col my-4 gap-4">
            <button className="border border-green-500 flex justify-center items-center bg-transparent px-6 gap-2 py-4">
              <img src={lock} alt="Lock Icon" />
              Login
            </button>
            <button className="px-8 py-5 rounded-md bg-green-500 text-white font-bold">Sign Up For Free</button>
          </div>
        </ul>
      </div>
    </div>
  );
};

export default Navbar;

import React from 'react';
import { Hero, Navbar, Companies, Courses, Achievement, Categories, Feedback, CTA, Footer, RegistrationForm } from './components';
import './App.css';

const App = () => {
  return (
    <div>
      <Navbar />
      <Hero />
      <Companies />
      <Courses />
      <Achievement />
      <Categories />
      <Feedback />
      <CTA />
      <div className="registration-section">
        <h2>Registration</h2>
        <RegistrationForm />
      </div>
      <Footer />
    </div>
  );
};

export default App;
